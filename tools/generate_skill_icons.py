import os, json

files = os.listdir(r"..\MapleCraft resource pack\assets\minecraft\textures\skill\icon")
icon_list = []

id = 1
for f in files:
	if f.endswith(".png"):
		name = f[:-4]
		icon_list.append([name, id])
		id += 1
		
		with open(f"../MapleCraft resource pack/assets/minecraft/models/item/skill/icon/{name}.json", "w") as model:
			model_dict = {
				"parent": "item/skill/icon",
				"textures": {
					"layer0": f"skill/icon/{name}"
				}
			}
			model.write(json.dumps(model_dict))

with open("../MapleCraft resource pack/assets/minecraft/models/item/carrot_on_a_stick.json", "r") as f:
	carrot_on_a_stick = json.loads(f.read())
	
carrot_on_a_stick["overrides"] = []
for icon in icon_list:
	new_model = {"predicate": {"custom_model_data": 1}, "model": "item/skill/icon/2001005"}
	new_model["predicate"]["custom_model_data"] = icon[1]
	new_model["model"] = f"item/skill/icon/{icon[0]}"
	carrot_on_a_stick["overrides"].append(new_model)
	
with open("../MapleCraft resource pack/assets/minecraft/models/item/carrot_on_a_stick.json", "w") as f:
	f.write(json.dumps(carrot_on_a_stick))

with open("skill_icons.csv", "w") as f:
	f.write("\n".join([f"{icon[0]},{icon[1]}" for icon in icon_list]))