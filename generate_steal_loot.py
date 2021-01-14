import os, json
from copy import deepcopy
from PIL import Image

for w in os.walk("MapleCraft data pack/data/skill/loot_tables/mob"):
	if w[0][-7:] == "special":
		continue
	
	try:
		for file in w[2]:
			with open(os.path.join(w[0], file)) as f:
				loot_table = json.loads(f.read())
			
			steal_loot = {"pools":[{"rolls": 1.0, "entries": []}]}
			for pool in loot_table["pools"]:
				copied_entry = deepcopy(pool["entries"][0])
				copied_entry["weight"] = int(copied_entry["conditions"][0]["looting_multiplier"] * 1000)
				del copied_entry["conditions"]
				if copied_entry["name"] == "minecraft:diamond":
					copied_entry["functions"][0]["modifiers"][0]["amount"]["min"] /= 2
					copied_entry["functions"][0]["modifiers"][0]["amount"]["max"] /= 2
				steal_loot["pools"][0]["entries"].append(copied_entry)
			
			with open(os.path.join(w[0], file).replace("loot_tables/mob", "loot_tables/steal"), "w") as f:
				f.write(json.dumps(steal_loot, indent=2))
						
	except Exception as e:
		print(e)
		os.system("pause")