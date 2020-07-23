import os, json

files = os.listdir(r"MapleCraft resource pack\assets\minecraft\textures\skill\icon")
icon_list = []

id = 1
for f in files:
	if f.endswith(".png"):
		name = f[:-4]
		icon_list.append([name, id])
		id += 1
		
		with open(f"MapleCraft resource pack/assets/minecraft/models/item/skill/icon/{name}.json", "w") as model:
			model_dict = {
				"parent": "item/generated",
				"textures": {
					"layer0": ""
				},
				"display": {
					"gui": {
						"rotation": [ 0, 0, 0 ],
						"translation": [ 0, 0, 0 ],
						"scale":[ 1, 1, 1 ]
					},
					"ground": {
						"rotation": [ 0, 0, 0 ],
						"translation": [ 0, 0, 0],
						"scale":[ 0, 0, 0 ]
					},
					"head": {
						"rotation": [ 0, 0, 0 ],
						"translation": [ 0, 0, 0],
						"scale":[ 0, 0, 0 ]
					},
					"thirdperson_righthand": {
						"rotation": [ 0, 0, 0 ],
						"translation": [ 0, 0, 0 ],
						"scale": [ 0, 0, 0 ]
					},
					"thirdperson_lefthand": {
						"rotation": [ 0, 0, 0 ],
						"translation": [ 0, 0, 0 ],
						"scale": [ 0, 0, 0 ]
					},
					"firstperson_righthand": {
						"rotation": [ 0, 0, 0 ],
						"translation": [ 0, 0, 0 ],
						"scale": [ 0, 0, 0 ]
					},
					"firstperson_lefthand": {
						"rotation": [ 0, 0, 0 ],
						"translation": [ 0, 0, 0 ],
						"scale": [ 0, 0, 0 ]
					}
				}
			}
			model_dict["textures"]["layer0"] = f"skill/icon/{name}"
			model.write(json.dumps(model_dict))

with open("MapleCraft resource pack/assets/minecraft/models/item/carrot_on_a_stick.json", "r") as f:
	carrot_on_a_stick = json.loads(f.read())
	
carrot_on_a_stick["overrides"] = []
for icon in icon_list:
	new_model = {"predicate": {"custom_model_data": 1}, "model": "item/skill/icon/2001005"}
	new_model["predicate"]["custom_model_data"] = icon[1]
	new_model["model"] = f"item/skill/icon/{icon[0]}"
	carrot_on_a_stick["overrides"].append(new_model)
	
with open("MapleCraft resource pack/assets/minecraft/models/item/carrot_on_a_stick.json", "w") as f:
	f.write(json.dumps(carrot_on_a_stick))

with open("skill_icons.csv", "w") as f:
	f.write("\n".join([f"{icon[0]},{icon[1]}" for icon in icon_list]))