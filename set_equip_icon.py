import os
from PIL import Image, ImageDraw

font = []
back_font = []
equip_type = "face"
font_index = int("0xD400", 16)

if not os.path.isdir(f"MapleCraft resource pack/assets/ui/textures/font/window/equip/icon/{equip_type}"):
	os.mkdir(f"MapleCraft resource pack/assets/ui/textures/font/window/equip/icon/{equip_type}")
for w in os.walk(f"MapleCraft resource pack/assets/minecraft/textures/item/equip/{equip_type}"):
	for file in w[2]:
		img = Image.open(os.path.join(w[0], file))
		size = ((img.size[0]+1)//4*4+2, (max(img.size[1], 36)+3)//4*4)
		parent = os.path.basename(w[0])
		if not os.path.isdir(f"MapleCraft resource pack/assets/ui/textures/font/window/equip/icon/{equip_type}/" + parent):
			os.mkdir(f"MapleCraft resource pack/assets/ui/textures/font/window/equip/icon/{equip_type}/" + parent)
			
		if size[1] > 40:
			print(w[0], file)
		if size[1] > 36:
			new_img_t = Image.new("RGBA", (size[0], size[1]//2))
			new_img_d = Image.new("RGBA", (size[0], size[1]//2))
			new_img_t.paste(img, ((size[0]-img.size[0]+1)//2, (size[1]-img.size[1]+1)//2))
			new_img_d.paste(img, ((size[0]-img.size[0]+1)//2, (size[1]-img.size[1]+1)//2 - size[1]//2))
			ImageDraw.Draw(new_img_t).point((size[0]-1, size[1]//2-1), fill=(255,255,255,10))
			ImageDraw.Draw(new_img_d).point((size[0]-1, size[1]//2-1), fill=(255,255,255,10))
			new_img_t.save(f"MapleCraft resource pack/assets/ui/textures/font/window/equip/icon/{equip_type}/" + parent + "/top_" + file)
			new_img_d.save(f"MapleCraft resource pack/assets/ui/textures/font/window/equip/icon/{equip_type}/" + parent + "/down_" + file)
			font.append(f'''		{{
			"type": "bitmap",
			"file": "ui:font/window/equip/icon/{equip_type}/{parent}/top_{file}",
			"ascent": 9,
			"height": {size[1]//4},
			"chars": [
				"\\u{hex(font_index)[2:].rjust(4, "0")}"
			]
		}},
		{{
			"type": "bitmap",
			"file": "ui:font/window/equip/icon/{equip_type}/{parent}/down_{file}",
			"ascent": 8,
			"height": {size[1]//4},
			"chars": [
				"\\u{hex(font_index+1)[2:].rjust(4, "0")}"
			]
		}}''')
		else:
			new_img = Image.new("RGBA", size)
			new_img.paste(img, ((size[0]-img.size[0]+1)//2, (size[1]-img.size[1]+1)//2))
			draw = ImageDraw.Draw(new_img)
			draw.point((size[0]-1, 0), fill=(255,255,255,10))
			draw.point((size[0]-1, size[1]-1), fill=(255,255,255,10))
			new_img.save(f"MapleCraft resource pack/assets/ui/textures/font/window/equip/icon/{equip_type}/" + parent + "/" + file)
			font.append(f'''		{{
			"type": "bitmap",
			"file": "ui:font/window/equip/icon/{equip_type}/{parent}/{file}",
			"ascent": 8,
			"height": 9,
			"chars": [
				"\\u{hex(font_index)[2:].rjust(4, "0")}",
				"\\u{hex(font_index+1)[2:].rjust(4, "0")}"
			]
		}}''')
		
		back_font.append(f'''		{{
			"type": "bitmap",
			"file": "space:font/space_split.png",
			"ascent": -32768,
			"height": -{(size[0]+2)//4+2},
			"chars": [
				"\\u{hex(font_index)[2:].rjust(4, "0")}"
			]
		}}''')
		
		font_index += 2

with open("C:/users/user/desktop/icon.json", "w") as f:
	f.write(",\n".join(font))
with open("C:/users/user/desktop/icon_back.json", "w") as f:
	f.write(",\n".join(back_font))
