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
	"name": "minecraft:warped_fungus_on_a_stick",
	"functions": [
		{
			"function": "minecraft:set_nbt",
			"tag": ""
		}
	]
}
CHANCE_TEMPLATE = {
	"condition": "minecraft:random_chance_with_looting",
	"chance": 0,
	"looting_multiplier": 1.0
}
COUNT_TEMPLATE = {
	"function": "minecraft:set_count",
	"count": 1
}
MESO_TEMPLATE = {
	"type": "minecraft:item",
	"name": "minecraft:diamond",
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
		id = dataFrame["索引"][i]
		itemDatas[id] = nbt

LoadItem(sh[PAGE_WEAPON].get_as_df())
LoadItem(sh[PAGE_EQUIP1].get_as_df())
LoadItem(sh[PAGE_EQUIP2].get_as_df())
LoadItem(sh[PAGE_EQUIP3].get_as_df())
LoadItem(sh[PAGE_PROJECTILE].get_as_df())
LoadItem(sh[PAGE_POTION].get_as_df())
LoadItem(sh[PAGE_SCROLL].get_as_df())
LoadItem(sh[PAGE_CHAIR].get_as_df())
LoadItem(sh[PAGE_ETC].get_as_df())

def GetItemID(index):
	if index > 33000:
		return "minecraft:stick"
	return "minecraft:warped_fungus_on_a_stick"
	
def GenerateEntry(id, weight = 1, min_num = 1, max_num = 1):
	if id == 0:  # 楓幣
		entry = deepcopy(MESO_TEMPLATE)
		amount = entry["functions"][0]["modifiers"][0]["amount"]
		amount["min"] = min_num * 0.001
		amount["max"] = max_num * 0.001
	else:
		entry = deepcopy(ENTRY_TEMPLATE)
		entry["name"] = GetItemID(pool_id)
		entry["functions"][0]["tag"] = itemDatas[pool_id]
		if min_num > 1 or max_num > 1:
			count_obj = deepcopy(COUNT_TEMPLATE)
			if min_num == max_num:
				count_obj["count"] = int(min_num)
			else:
				count_obj["count"] = { "min": int(min_num), "max": int(max_num) }
			entry["functions"].append(count_obj)
			
	if weight > 1:
		entry["weight"] = int(weight)
		
	return entry

def SetChance(entry, chance):
	chance_obj = deepcopy(CHANCE_TEMPLATE)
	chance_obj["looting_multiplier"] = chance
	entry["conditions"] = [chance_obj]

# 建立掉落池表
poolDatas = dict()
loot_pool_df = sh[PAGE_LOOT_POOL].get_as_df()
for i in range(loot_pool_df.shape[0]):
	pool_id = loot_pool_df["索引"][i]
	if pool_id == "":
		continue
	
	entries = []
	for j in range(60):
		id_col = j * 4 + 2
		id = loot_pool_df.iloc[i, id_col]
		if id == "":
			break
		min_num = loot_pool_df.iloc[i, id_col + 1]
		max_num = loot_pool_df.iloc[i, id_col + 2]
		weight = loot_pool_df.iloc[i, id_col + 3]
		entries.append(GenerateEntry(id, weight, min_num, max_num))
		
	poolDatas[pool_id] = entries

# 輸出掉落表
loot_df = sh[PAGE_LOOT].get_as_df()
for i in range(loot_df.shape[0]):
	path = "../MapleCraft data pack/data/" + loot_df["路徑"][i].replace(":", "/loot_tables/") + ".json"
	dir_name = os.path.dirname(path)
	if not os.path.isdir(dir_name):
		os.makedirs(dir_name)
	
	data = deepcopy(ROOT_TEMPLATE)
	for j in range(60):
		pool_col = j * 3 + 1
		pool_id = loot_df.iloc[i, pool_col]
		if pool_id == "":
			break
		chance = loot_df.iloc[i, pool_col + 2]
		
		pool = deepcopy(POOL_TEMPLATE)
		pool["rolls"] = int(loot_df.iloc[i, pool_col + 1])
		entries = pool["entries"]
		if pool_id > 40000:  # 真的是掉落池表的內容
			if chance < 1:
				pool["entries"] = deepcopy(poolDatas[pool_id])
				for entry in pool["entries"]:
					SetChance(entry, chance)
			else:
				pool["entries"] = poolDatas[pool_id]
		else:  # 單一道具編號
			entry = GenerateEntry(pool_id)
			if chance < 1:
				SetChance(entry, chance)
			pool["entries"] = [GenerateEntry(pool_id, chance)]
		
		data["pools"].append(pool)
	
	with open(path, "w") as f:
		f.write(json.dumps(data))

os.system("pause")