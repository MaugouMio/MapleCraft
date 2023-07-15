import xml.etree.cElementTree as ET
import PIL.Image
import base64, io, math, os, json, shutil
import numpy as np
from subprocess import Popen, PIPE, STDOUT
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter import Scale

def mkdir(path):
	if os.path.exists(path):
		return
	
	parent = os.path.dirname(path)
	if not os.path.exists(parent):
		mkdir(parent)
	
	os.mkdir(path)

def getJavaSetOrder(str_list):
	p = Popen("PrintSet", stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
	print_stdout = p.communicate(input = str_list.encode())[0]
	return print_stdout.decode().split()

#################################################################

def getPageInfo(effect_life, folder):
	page_amount = effect_life // 10
	if effect_life % 10 > 0:
		page_amount += 1
	page_names = [f'{{"text":"","font":"skill:{folder}/{i}"}}' for i in range(page_amount)]

	page_file_names = dict()
	for i in range(page_amount):
		page_file_names[page_names[i]] = f"{folder}/{i}.json"
	page_order = getJavaSetOrder(" ".join(page_names))
	
	return page_file_names, page_order
	
def insertWordInfo(font_files, frame, page_file_names, page_order, folder, delay_index, ascents, image_heights):
	sub_num = frame % 10
	page = frame // 10
	
	page_file_name = page_file_names[page_order[page]]
	if page_file_name not in font_files:
		font_files[page_file_name] = {"providers": []}
	
	word_info = {
		"type": "bitmap",
		"file": f"skill:font/{folder}/{delay_index}.png",
		"ascent": int(ascents[delay_index] / 1.2),
		"height": int(image_heights[delay_index] / 1.2),
		"chars": [str(sub_num)]
	}
	font_files[page_file_name]["providers"].append(word_info)

def generateThresholdDelay(delays, folder, image_heights, ascents):
	font_files = dict()
	delays = np.array(delays, dtype=int)
	effect_life = math.ceil(delays.sum() / 50)
	page_file_names, page_order = getPageInfo(effect_life, folder)

	used_imgs = set()
	delay_index = 0
	for i in range(effect_life):
		while i * 50 >= delays[:(delay_index + 1)].sum():
			delay_index += 1
			
		used_imgs.add(delay_index)
		insertWordInfo(font_files, i, page_file_names, page_order, folder, delay_index, ascents, image_heights)
	
	return page_order, effect_life, font_files, used_imgs

def generateMinDistDelay(delays, folder, image_heights, ascents):
	font_files = dict()
	frame_amounts = np.array([max(round(delay / 50), 1) for delay in delays], dtype=int)
	effect_life = frame_amounts.sum()
	page_file_names, page_order = getPageInfo(effect_life, folder)
	
	delay_index = 0
	for i in range(effect_life):
		if i == frame_amounts[:(delay_index + 1)].sum():
			delay_index += 1
		
		insertWordInfo(font_files, i, page_file_names, page_order, folder, delay_index, ascents, image_heights)
	
	return page_order, effect_life, font_files

def generateFont(resourcepack_path, xml_files, anchor, formula):
	if len(xml_files) == 0:
		return
	
	for xml_file in xml_files:
		file_name = os.path.basename(xml_file)
		file_name = file_name[:file_name.find('.')]
		folder = file_name[:3] + '/' + file_name[3:7] + '/' + file_name[7:]
		
		texture_path = f"{resourcepack_path}/assets/skill/textures/font/{folder}"
		if os.path.exists(texture_path):
			shutil.rmtree(texture_path)
		mkdir(texture_path)
		
		font_directory = f"{resourcepack_path}/assets/skill/font/{folder}"
		if os.path.exists(font_directory):
			shutil.rmtree(font_directory)
		mkdir(font_directory)

		tree = ET.ElementTree(file = xml_file)
		root = tree.getroot()[0]

		delays = []
		image_heights = []
		images = []
		for i in range(len(root)):
			child_of_root = root[i]
			if child_of_root.tag != "canvas":
				continue
			
			size = (int(child_of_root.attrib["width"]), int(child_of_root.attrib["height"]))
			for vec in child_of_root.findall("vector"):
				if vec.attrib["name"] == "origin":
					ori_x = int(vec.attrib["x"])
					ori_y = int(vec.attrib["y"])
					if ori_x < size[0] - ori_x:
						new_width = (size[0] - ori_x) * 2
						offset_x = size[0] - ori_x * 2
					else:
						new_width = ori_x * 2
						offset_x = 0
					
					if ori_y < size[1] - ori_y:
						new_height = (size[1] - ori_y) * 2
						offset_y = size[1] - ori_y * 2
					else:
						new_height = ori_y * 2
						offset_y = 0
					
					new_size = (new_width, new_height)
					offset = (offset_x, offset_y)
					break
					
			img_delay = 100
			for c in child_of_root.findall("int"):
				if c.attrib["name"] == "delay":
					img_delay = int(c.attrib["value"])
					break
			delays.append(img_delay)
			
			img = PIL.Image.open(io.BytesIO(base64.b64decode(child_of_root.attrib["basedata"])))
			new_img = PIL.Image.new(img.mode, new_size)
			
			new_img.paste(img, (offset[0], offset[1], offset[0] + size[0], offset[1] + size[1]))
			
			image_heights.append(new_size[1])
			
			images.append(new_img)
		
		anchor_required_height = round(float(np.array(image_heights).max() * abs(anchor - 0.5) * 2))
		ascents = []
		for i in range(len(images)):
			img = images[i]
			if img.size[1] < anchor_required_height:
				new_size = (img.size[0], anchor_required_height)
				height_offset = (anchor_required_height - img.size[1]) // 2
				
				new_img = PIL.Image.new(img.mode, new_size)
				new_img.paste(img, (0, height_offset, img.size[0], height_offset + img.size[1]))
				img = new_img
				
				image_heights[i] = anchor_required_height
				if anchor < 0.5:
					ascents.append(0)
				else:
					ascents.append(anchor_required_height)
			else:
				ascent = (img.size[1] - anchor_required_height) // 2
				if anchor < 0.5:
					ascents.append(ascent)
				else:
					ascents.append(img.size[1] - ascent)
					
			resize_scale = min(256 / img.size[0], 256 / img.size[1])
			if resize_scale < 1:
				scaled_size = (math.floor(img.size[0] * resize_scale), math.floor(img.size[1] * resize_scale))
				img = img.resize(scaled_size)
			
			img.putpixel((0,				0				), (1,3,5,1))
			img.putpixel((0,				img.size[1] - 1	), (1,3,5,1))
			img.putpixel((img.size[0] - 1,	0				), (1,3,5,1))
			img.putpixel((img.size[0] - 1,	img.size[1] - 1	), (1,3,5,1))
			
			images[i] = img

		if formula == 0:
			page_order, effect_life, font_files, used_imgs = generateThresholdDelay(delays, folder, image_heights, ascents)
			for i in range(len(images)):
				if i in used_imgs:
					images[i].save(f"{texture_path}/{i}.png")
		elif formula == 1:
			page_order, effect_life, font_files = generateMinDistDelay(delays, folder, image_heights, ascents)
			for i in range(len(images)):
				images[i].save(f"{texture_path}/{i}.png")

		with open("MapleCraft data pack/data/skill/functions/summon_font_effect/" + file_name + ".mcfunction", "w") as f:
			initial_name = page_order[0].replace('"text":""', '"text":"0"')
			tags = ",".join(page_order)
			f.write('''data merge entity @s {text:'%s',Tags:%s,billboard:"center",text_opacity:10,background:0}\n''' %(initial_name, tags))
			f.write('''scoreboard players set @s max_life %s\n''' %effect_life)
			f.write('''scoreboard players set @s type 1\n''')

		for font in font_files:
			with open(f"{resourcepack_path}/assets/skill/font/{font}", "w") as f:
				f.write(json.dumps(font_files[font], indent=4))
	
	messagebox.showinfo(title="完成", message="完成")

#########################################

win = Tk()
win.title("xml2font")
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
window_width, window_height = (600, 240)
size = "%dx%d+%d+%d" % (window_width, window_height, (screenwidth - window_width)/2, (screenheight - window_height)/2)
win.geometry(size)
win.resizable(0, 0)

resourcepack_path = StringVar(win, os.path.abspath(os.path.expandvars("%HOMEPATH%/Desktop")) + r"\MapleCraft\MapleCraft resource pack")
anchor_value = DoubleVar(win, 0.5)
formula_value = IntVar(win, 0)

##### Resource Pack Directory Frame #####
# Frame of widgets
set_dir_frame = Frame(win)
set_dir_frame.pack(side=TOP, pady=10)
# Label
build_description = Label(set_dir_frame, text="資源包資料夾")
build_description.pack(side=LEFT)
# Entry
build_dest_entry = Entry(set_dir_frame, textvariable = resourcepack_path, width=60)
build_dest_entry.pack(side=LEFT, padx=10)
# Select Button
select_folder_btn = Button(set_dir_frame, text="...", width=3, command = lambda entry=resourcepack_path: entry.set(filedialog.askdirectory(initialdir=os.path.abspath(os.path.expandvars("%APPDATA%\\.minecraft\\resourcepacks")))))
select_folder_btn.pack(side=LEFT)

##### Main Frame #####
# Frame of widgets
main_frame = Frame(win)
main_frame.pack(side=TOP)

# Frame of Options
option_frame = Frame(main_frame)
option_frame.pack(side=TOP, pady=10)
# Anchor Slider
anchor_frame = Frame(option_frame)
anchor_frame.pack(side=LEFT, padx=50)
Label(anchor_frame, text="圖片錨點(旋轉中心)").pack(side=TOP)
anchor_scale = Scale(anchor_frame, orient="vertical", from_=0, to=1, resolution=0.05, variable=anchor_value)
anchor_scale.pack(side=TOP)
# Formula selection
formula_frame = Frame(option_frame)
formula_frame.pack(side=RIGHT, padx=100)
Label(formula_frame, text="幀分割公式").pack(side=TOP, pady=10)
Radiobutton(formula_frame, text="時間門檻法", variable=formula_value, value=0).pack(side=TOP, anchor="w")
Radiobutton(formula_frame, text="最小間距差法", variable=formula_value, value=1).pack(side=TOP, anchor="w")

# Generate Button
generate_font_btn = Button(main_frame, text="從xml檔建立",
	command = lambda rp=resourcepack_path, anchor=anchor_value: generateFont(
		rp.get(),
		filedialog.askopenfilenames(initialdir=os.path.expandvars("%HOMEPATH%/Desktop"),
		filetypes=[('xml檔', '.xml'), ('all files', '.*'),]),
		anchor.get(),
		formula_value.get()
	)
)
generate_font_btn.pack(side=TOP, pady=10)

#########################################

win.mainloop()