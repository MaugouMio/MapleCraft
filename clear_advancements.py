import os

for dirPath, dirNames, fileNames in os.walk("MapleCraft data pack/data/minecraft/advancements/"):
	for file in fileNames:
		with open(os.path.join(dirPath, file), "w") as f:
			f.write('{"criteria":{"impossible": {"trigger": "minecraft:impossible"}}}')

os.system("pause")