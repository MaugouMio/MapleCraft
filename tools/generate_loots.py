import os, json, pygsheets
from copy import deepcopy

PAGE_WEAPON		= 0
PAGE_EQUIP1		= 1
PAGE_EQUIP2		= 2
PAGE_EQUIP3		= 3
PAGE_PROJECTILE	= 4
PAGE_POTION		= 5
PAGE_SCROLL		= 6
PAGE_CHAIR		= 7
PAGE_ETC		= 8
PAGE_LOOT		= 9
PAGE_LOOT_POOL	= 10

ROOT_TEMPLATE = {
	"pools": []
}
POOL_TEMPLATE = {
	"rolls": 1,
	"entries": []
}
ENTRY_TEMPLATE = {
	"type": "minecraft:item",
	"weight": 1,
	"name": "minecraft:warped_fungus_on_a_stick",
	"functions": [
		{
			"function": "minecraft:set_nbt",
			"tag": ""
		}
	]
}
MESO_TEMPLATE = {
	"type": "minecraft:item",
	"name": "minecraft:diamond",
	"conditions": [
		{
			"condition": "minecraft:random_chance_with_looting",
			"chance": 0,
			"looting_multiplier": 0.65
		}
	],
	"functions": [
		{
			"function": "minecraft:set_attributes",
			"modifiers": [
				{
					"name": "meso",
					"attribute": "minecraft:generic.attack_damage",
					"operation": "addition",
					"amount": {
						"min": 0.001,
						"max": 0.001
					},
					"slot": "head"
				}
			]
		},
		{
			"function": "minecraft:set_name",
			"name": ""
		},
		{
			"function": "minecraft:set_nbt",
			"tag": "{HideFlags:127}"
		}
	]
}


gc = pygsheets.authorize(service_account_file = "../maplecraft_key.json")
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1j9Ft-OW0SnFODV9K9vcjB3j3hOa0N5o4Fvroih1AnTY/edit#gid=303406431")

itemDatas = dict()
def LoadItem(dataFrame):
	for i in range(0, dataFrame.shape[0]):
		nbt = dataFrame["nbt標籤"][i]
		if nbt == "":
			continue
		itemDatas[dataFrame["索引"][i]] = nbt

LoadItem(sh[PAGE_WEAPON].get_as_df(include_tailing_empty=True))
LoadItem(sh[PAGE_EQUIP1].get_as_df(include_tailing_empty=True))
LoadItem(sh[PAGE_EQUIP2].get_as_df(include_tailing_empty=True))
LoadItem(sh[PAGE_EQUIP3].get_as_df(include_tailing_empty=True))
LoadItem(sh[PAGE_PROJECTILE].get_as_df(include_tailing_empty=True))
LoadItem(sh[PAGE_POTION].get_as_df(include_tailing_empty=True))
LoadItem(sh[PAGE_SCROLL].get_as_df(include_tailing_empty=True))
LoadItem(sh[PAGE_CHAIR].get_as_df(include_tailing_empty=True))
LoadItem(sh[PAGE_ETC].get_as_df(include_tailing_empty=True))

def GetItemID(index):
	if index > 33000:
		return "minecraft:stick"
	return "minecraft:warped_fungus_on_a_stick"

# 建立掉落池表
loot_pool_df = sh[PAGE_LOOT_POOL].get_as_df(include_tailing_empty=True)

# 輸出掉落表
loot_df = sh[PAGE_LOOT].get_as_df(include_tailing_empty=True)
for i in range(loot_df.shape[0]):
	path = "../MapleCraft data pack/data/" + loot_df["路徑"][i].replace(":", "/loot_tables/") + ".json"
	os.makedirs(os.path.dirname(path))
	
	data = deepcopy(ROOT_TEMPLATE)
	# do something
	with open(path, "w") as f:
		f.write(json.dumps(data))