import xml.etree.cElementTree as ET
import base64, io, json, os
from PIL import Image

equip_type = "eye"

if not os.path.isdir(f"MapleCraft resource pack/assets/minecraft/textures/item/equip/{equip_type}"):
	os.mkdir(f"MapleCraft resource pack/assets/minecraft/textures/item/equip/{equip_type}")

try:
	tree = ET.ElementTree(file = "C:/users/user/desktop/img.xml")
	root = tree.getroot()[0]
	img_dict = dict()
	for i in range(len(root)):
		child_of_root = root[i]
		flag = False
		for imgdir in child_of_root.findall("imgdir"):
			if imgdir.attrib["name"] == "info":
				for canvas in imgdir.findall("canvas"):
					if canvas.attrib["name"] == "iconRaw":
						img_dict[child_of_root.attrib["name"][1:-4]] = Image.open(io.BytesIO(base64.b64decode(canvas.attrib["basedata"])))
						flag = True
						break
				if flag:
					break
	
	tree = ET.ElementTree(file = "C:/users/user/desktop/string.xml")
	root = tree.getroot()[0]
	id_dict = dict()
	for imgdir in root.findall("imgdir"):
		for name in imgdir.findall("string"):
			if name.attrib["name"] == "name":
				if name.attrib["value"] not in id_dict:
					id_dict[name.attrib["value"]] = [imgdir.attrib["name"]]
				else:
					id_dict[name.attrib["value"]].append(imgdir.attrib["name"])

	with open("C:/users/user/desktop/translate.json", "r") as f:
		equip_names = json.loads(f.read())
	for key in equip_names:
		job = key.split(".")[-2]
		if not os.path.isdir(f"MapleCraft resource pack/assets/minecraft/textures/item/equip/{equip_type}/{job}"):
			os.mkdir(f"MapleCraft resource pack/assets/minecraft/textures/item/equip/{equip_type}/{job}")
		for id in id_dict[equip_names[key]]:
			if id in img_dict:
				img_dict[id].save(f"MapleCraft resource pack/assets/minecraft/textures/item/equip/{equip_type}/{job}/{key.split('.')[-1]}.png")
				break

except Exception as e:
	print(e)
	os.system("pause")