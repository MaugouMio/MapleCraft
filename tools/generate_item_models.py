import os, json
from PIL import Image

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
					if os.path.isdir(file_path):
						# TODO: spawn handheld model
						pass
					else:
						icon = Image.open(file_path)
						img_size = icon.size
						file = file[:file.find('.')]
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
							
						# weapon need to generate extra icon with boarder
						if item_type == "weapon":
							boarder_icon = generateBoarderIcon()
							boarder_icon.paste(icon, ((boarder_icon.size[0]-icon.size[0]+1)//2, (boarder_icon.size[1]-icon.size[1]+1)//2), icon)
							target_texture_path = os.path.join(texture_parent_path, "equip")
							if not os.path.isdir(target_texture_path):
								os.mkdir(target_texture_path)
							boarder_icon.save(os.path.join(target_texture_path, file + ".png"))
						
	except Exception as e:
		print(e)
		os.system("pause")