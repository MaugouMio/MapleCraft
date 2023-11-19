import os, json
from PIL import Image

DEFAULT_TRANSLATION = {
	"spear": [0, 3, -0.5],
	"polearm": [0, 3, -3],
	"staff": [0, 0, 0.5],
	"wand": [0, 0, 0.5],
	"bow": [0, -1.5, 2],
	"crossbow": [0, 1, 0],
	"claw": [0.5, -2, 1],
	"dagger": [0, -2, -2],
	"oh_sword": [0, 4.5, -1],
	"th_sword": [0, 8, -2],
	"oh_axe": [0, 4.5, -1],
	"th_axe": [0, 4, -3],
	"oh_blunt": [0, 4, -1],
	"th_blunt": [0, 4, -1]
}

DEFAULT_ROTATION = {
	"spear": [-20, 110, 90],
	"polearm": [-20, 110, 90],
	"staff": [-15, 110, 90],
	"wand": [-15, 110, 90],
	"bow": [0, 90, 90],
	"crossbow": [-90, 0, -45],
	"claw": [0, 90, 90],
	"dagger": [0, 90, 90],
	"oh_sword": [-20, 110, 90],
	"th_sword": [-20, 100, 90],
	"oh_axe": [-20, 100, 90],
	"th_axe": [-20, 100, 90],
	"oh_blunt": [-20, 100, 90],
	"th_blunt": [-20, 100, 90]
}

def generateBoarderIcon():
	dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	icon = Image.new("RGBA", (42, 42))
	for i in range(4):
		idx = 0
		maxIdx = (41 - i * 2) * 4
		dirIdx = 0
		axis = [i, i]
		for k in range(4):
			for j in range(i, 41 - i):
				icon.putpixel(tuple(axis), (255, 255, 254, idx * 255 // maxIdx))
				axis[0] += dir[dirIdx][0]
				axis[1] += dir[dirIdx][1]
				idx += 1
			dirIdx += 1
	return icon

for item_type in ["weapon"]:
	texture_folder = "../MapleCraft resource pack/assets/minecraft/textures/item/" + item_type
	model_folder = "../MapleCraft resource pack/assets/minecraft/models/item/" + item_type
	
	if not os.path.isdir(model_folder):
		os.mkdir(model_folder)
		
	try:
		for folder in os.listdir(texture_folder):
			texture_parent_path = os.path.join(texture_folder, folder)
			if os.path.isdir(texture_parent_path):
				model_parent_path = os.path.join(model_folder, folder)
				if not os.path.isdir(model_parent_path):
					os.mkdir(model_parent_path)
					
				for file in os.listdir(texture_parent_path):
					file_path = os.path.join(texture_parent_path, file)
					if not os.path.isdir(file_path):
						file = file[:file.find('.')]
						icon = Image.open(file_path)
						img_size = icon.size
						with open(os.path.join(model_parent_path, file + ".json"), "w") as f:
							model = {
								"parent": "minecraft:item/generated",
								"textures": {
									"layer0": f"minecraft:item/{item_type}/{folder}/{file}"
								},
								"display": {
									"ground": {
										"rotation": [ 0, 0, 0 ],
										"translation": [ 0, 2, 0 ],
										"scale": [ 0.5 * img_size[0] / 32, 0.5 * img_size[1] / 32, 0.5 ]
									},
									"gui": {
										"rotation": [ 0, 0, 0 ],
										"translation": [ 0, 0, 0 ],
										"scale": [ 1 * img_size[0] / 32, 1 * img_size[1] / 32, 1 ]
									},
									"thirdperson_righthand": {
										"rotation": [ 0, 0, 0 ],
										"translation": [ 0, 3, 1 ],
										"scale": [ 0.55 * img_size[0] / 32, 0.55 * img_size[1] / 32, 0.55 ]
									},
									"firstperson_righthand": {
										"rotation": [ 0, -90, 25 ],
										"translation": [ 1.13, 3.2, 1.13],
										"scale": [ 0.68 * img_size[0] / 32, 0.68 * img_size[1] / 32, 0.68 ]
									}
								}
							}
							f.write(json.dumps(model))
							
						if item_type == "weapon":
							# 包含提示外框的 icon 圖片
							boarder_icon = generateBoarderIcon()
							boarder_icon.paste(icon, ((boarder_icon.size[0]-icon.size[0]+1)//2, (boarder_icon.size[1]-icon.size[1]+1)//2), icon)
							target_texture_path = os.path.join(texture_parent_path, "equip")
							if not os.path.isdir(target_texture_path):
								os.mkdir(target_texture_path)
							boarder_icon.save(os.path.join(target_texture_path, file + ".png"))
						
							# 裝飾用武器模型 (只是生成一個大略的模型，生成完還是要進遊戲確認調整)
							model_img_path = os.path.join(texture_parent_path, "equip/" + file + "_m.png")
							if not os.path.isfile(model_img_path):  # 有圖片才生模型
								continue
							model_path = os.path.join(model_parent_path, "equip/" + file + ".json")
							if os.path.isfile(model_path):  # 已經生成的模型不要蓋掉
								continue
							model_img = Image.open(model_img_path)
							img_size = model_img.size
							with open(model_path, "w") as f:
								thickness = 1
								if folder == "crossbow" or folder == "oh_blunt":
									thickness = 1.5
								elif folder == "th_blunt":
									thickness = 2
								elif folder == "claw":
									thickness = 4
									
								model = {
									"parent": "minecraft:item/weapon/base",
									"textures": {
										"layer0": f"minecraft:item/{item_type}/{folder}/equip/{file}_m",
										"layer1": f"minecraft:item/{item_type}/{folder}/equip/{file}"
									},
									"display": {
										"thirdperson_lefthand": {
											"rotation": DEFAULT_ROTATION[folder],
											"translation": DEFAULT_TRANSLATION[folder],
											"scale": [ img_size[0] / 32, img_size[1] / 32, thickness ]
										}
									}
								}
								f.write(json.dumps(model))
						
	except Exception as e:
		print(e)
		os.system("pause")