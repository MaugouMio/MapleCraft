import os, json
from PIL import Image

for item_type in ["equip/pants"]:
	texture_folder = "MapleCraft resource pack/assets/minecraft/textures/item/" + item_type
	model_folder = "MapleCraft resource pack/assets/minecraft/models/item/" + item_type

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
					img_size = Image.open(os.path.join(texture_parent_path, file)).size
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
						
	except Exception as e:
		print(e)
		os.system("pause")