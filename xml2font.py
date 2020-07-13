import xml.etree.cElementTree as ET
import PIL.Image, PIL.ImageDraw
import base64, io, math, os, json
import numpy as np
from subprocess import Popen, PIPE, STDOUT
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import *

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

def generateFont(resourcepack_path, xml_files):
	if len(xml_files) == 0:
		return
	
	for xml_file in xml_files:
		file_name = os.path.basename(xml_file)
		folder = file_name[:3] + '/' + file_name[3:7] + '/' + file_name[7:file_name.find('.')]

		tree = ET.ElementTree(file = xml_file)
		root = tree.getroot()[0]

		delays = []
		image_heights = []
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
					
			for c in child_of_root.findall("int"):
				if c.attrib["name"] == "delay":
					delays.append(int(c.attrib["value"]))
					break
			
			img = PIL.Image.open(io.BytesIO(base64.b64decode(child_of_root.attrib["basedata"])))
			new_img = PIL.Image.new(img.mode, new_size)
			
			new_img.paste(img, (offset[0], offset[1], offset[0] + size[0], offset[1] + size[1]))
			draw = PIL.ImageDraw.Draw(new_img)
			draw.point([new_size[0] - 1, new_size[1] - 1], (255, 255, 255, 12))
			
			image_heights.append(new_size[1])
			resize_scale = min(256 / new_size[0], 256 / new_size[1])
			if resize_scale < 1:
				scaled_size = (math.floor(new_size[0] * resize_scale), math.floor(new_size[1] * resize_scale))
				new_img = new_img.resize(scaled_size)
			
			parent_path = f"{resourcepack_path}/assets/skill/textures/font/{folder}"
			mkdir(parent_path)
			new_img.save(f"{parent_path}/{i}.png")

		delays = np.array(delays, dtype=int)
		effect_life = math.ceil(delays.sum() / 50)

		page_amount = effect_life // 10 + 1
		page_names = [f'{{"text":"","font":"skill:{folder}/{i}"}}' for i in range(page_amount)]

		page_file_names = dict()
		for i in range(page_amount):
			page_file_names[page_names[i]] = f"{folder}/{i}.json"
		page_order = getJavaSetOrder(" ".join(page_names))

		font_files = dict()
		delay_index = 0
		for i in range(effect_life):
			sub_num = i % 10
			page = i // 10
			
			if i * 50 > delays[:(delay_index + 1)].sum():
				delay_index += 1
			
			page_file_name = page_file_names[page_order[page]]
			if page_file_name not in font_files:
				font_files[page_file_name] = {"providers": []}
			
			word_info = {
				"type": "bitmap",
				"file": f"skill:font/{folder}/{delay_index}.png",
				"ascent": image_heights[delay_index] // 4,
				"height": image_heights[delay_index] // 2,
				"chars": [str(sub_num)]
			}
			font_files[page_file_name]["providers"].append(word_info)

		font_directory = f"{resourcepack_path}/assets/skill/font/{folder}"
		mkdir(font_directory)
		with open(font_directory + "/summon.txt", "w") as f:
			page_order.append("new")
			initial_name = page_order[0].replace('"text":""', '"text":"0"')
			initial_name = f'[{{"text":"F","font":"space:default"}},{initial_name},{{"text":"F","font":"space:default"}}]'
			f.write(f'summon minecraft:area_effect_cloud ~ ~ ~ {{CustomName:\'{initial_name}\',CustomNameVisible:1,Duration:{effect_life},Tags:{page_order}}}\n')
			f.write("scoreboard players set @e[type=area_effect_cloud,tag=new,limit=1] type 1\n")
			f.write("tag @e[type=area_effect_cloud,tag=new,limit=1] remove new\n")

		for font in font_files:
			with open(f"{resourcepack_path}/assets/skill/font/{font}", "w") as f:
				f.write(json.dumps(font_files[font], indent=4))
	
	messagebox.showinfo(title="完成", message="完成")

#########################################

win = Tk()
win.title("xml2font")
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
window_width, window_height = (600, 90)
size = "%dx%d+%d+%d" % (window_width, window_height, (screenwidth - window_width)/2, (screenheight - window_height)/2)
win.geometry(size)
win.resizable(0, 0)

resourcepack_path = StringVar()
resourcepack_path.set(os.path.abspath(os.path.expandvars("%HOMEPATH%/Desktop")) + r"\MapleCraft\MapleCraft resource pack")

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
select_folder_btn = Button(set_dir_frame, text="...", width=3, command = lambda entry=resourcepack_path: entry.set(filedialog.askdirectory()))
select_folder_btn.pack(side=LEFT)

##### Generate Button #####
generate_font_btn = Button(win, text="從xml檔建立", command = lambda rp=resourcepack_path: generateFont(rp.get(), filedialog.askopenfilenames(initialdir=os.path.expandvars("%HOMEPATH%/Desktop"), filetypes=[('xml檔', '.xml'), ('all files', '.*'),])))
generate_font_btn.pack()

#########################################

win.mainloop()