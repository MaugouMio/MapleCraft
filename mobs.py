mob_dict = {}
# 殭屍菇菇
mob_dict["2230101"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["new_enemy","heal_target","holy_weakness"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:24,hp_max:500,mp_max:55,accuracy:50,avoidability:8,weapon_defense:20,magic_defense:30,kb:1,speed:100,exp:42,height:2,hurt_sound:1,die_sound:2},steal_loot:"skill:steal/20_29/zombie_mushroom",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.3}],DeathLootTable:"skill:mob/20_29/zombie_mushroom",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{CustomModelData:10000,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["new_enemy","original","heal_target"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:7.5}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 鱷魚 KPQ
mob_dict["9300001"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["kpq_mob","new_enemy","no_jump","fire_weakness","ice_resist","freeze_immune"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:32,hp_max:1000,mp_max:80,accuracy:140,avoidability:10,weapon_defense:90,magic_defense:80,kb:1,speed:60,exp:120,hurt_sound:1,die_sound:3},steal_loot:"skill:steal/special/coupon_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.23238}],DeathLootTable:"skill:mob/special/coupon_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["kpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{CustomModelData:10004,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["kpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:7.5}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 青蛇 KPQ
mob_dict["9300000"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["kpq_mob","new_enemy","no_jump"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:21,hp_max:320,mp_max:40,accuracy:240,avoidability:15,weapon_defense:60,magic_defense:60,kb:50,speed:110,exp:240,hurt_sound:1,die_sound:4},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.31464}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["kpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{CustomModelData:10008,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["kpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:0.4,Attributes:[{Name:"generic.attack_damage",Base:8.0}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 風獨眼獸 KPQ
mob_dict["9300002"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["kpq_mob","new_enemy","poison_resist","poison_immune"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:35,hp_max:2000,mp_max:130,accuracy:120,avoidability:8,weapon_defense:90,magic_defense:140,kb:1,speed:85,exp:280,width:2,height:2,hurt_sound:1,die_sound:5},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.27659}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["kpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{CustomModelData:10012,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["kpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:10.0}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 超級綠水靈
mob_dict["9300003"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["kpq_mob","new_enemy","dead_effect","king_slime","ice_resist","fire_resist","lightning_resist","holy_resist","freeze_immune"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:40,hp_max:8000,mp_max:100,accuracy:140,avoidability:10,magic_attack:165,weapon_defense:165,magic_defense:160,kb:300,speed:80,exp:800,width:5,height:8,hurt_sound:2,die_sound:6,skill_id:1},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.26833}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["kpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:21,stand_frame:11},CustomModelData:10016,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["kpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:4.0,Attributes:[{Name:"generic.attack_damage",Base:11.0}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 綠水靈
mob_dict["0210100"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["new_enemy","lightning_weakness"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:6,hp_max:50,mp_max:35,accuracy:35,avoidability:1,weapon_defense:5,magic_defense:10,kb:1,speed:80,exp:10,width:1,height:2,hurt_sound:3,die_sound:6},steal_loot:"skill:steal/0_9/slime",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.26833}],DeathLootTable:"skill:mob/0_9/slime",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:21,stand_frame:15},CustomModelData:10107,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:2.2}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 綠菇菇
mob_dict["1110100"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["new_enemy","no_jump","poison_s_resist","poison_immune"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:15,hp_max:250,mp_max:25,accuracy:45,avoidability:5,weapon_defense:12,magic_defense:40,kb:1,speed:80,exp:26,height:1,hurt_sound:1,die_sound:7},steal_loot:"skill:steal/10_19/green_mushroom",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.26833}],DeathLootTable:"skill:mob/10_19/green_mushroom",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{CustomModelData:10145,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:6.2}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 刺菇菇
mob_dict["2110200"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["new_enemy","no_jump"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:22,hp_max:300,mp_max:35,accuracy:55,avoidability:7,weapon_defense:30,magic_defense:0,kb:1,speed:80,exp:35,height:1,hurt_sound:1,die_sound:7},steal_loot:"skill:steal/20_29/horny_mushroom",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.26833}],DeathLootTable:"skill:mob/20_29/horny_mushroom",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{CustomModelData:10149,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:7.0}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 小石球 新手訓練
mob_dict["9300018"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["new_enemy","no_jump"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:1,hp_max:15,mp_max:0,accuracy:0,avoidability:0,weapon_defense:0,magic_defense:0,kb:1,speed:40,exp:3,hurt_sound:4,die_sound:8},steal_loot:"skill:steal/special/jr_sentinel_train",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.18974}],DeathLootTable:"skill:mob/special/jr_sentinel_train",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:8,stand_frame:22},CustomModelData:10153,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["new_enemy","no_body_attack","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:0.4,Attributes:[{Name:"generic.attack_damage",Base:0.0}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 白色發條鼠 LDPQ
mob_dict["9300005"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy","no_jump"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:32,hp_max:3700,mp_max:0,accuracy:80,avoidability:13,weapon_defense:85,magic_defense:95,kb:0,speed:90,exp:260,hurt_sound:6,die_sound:9},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.2846}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{CustomModelData:10185,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:0.4,Attributes:[{Name:"generic.attack_damage",Base:9.2}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 黑色發條鼠 LDPQ
mob_dict["9300006"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy","no_jump"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:34,hp_max:4300,mp_max:0,accuracy:90,avoidability:14,weapon_defense:95,magic_defense:95,kb:0,speed:100,exp:280,hurt_sound:6,die_sound:9},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.3}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{CustomModelData:10189,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:10.5}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 機械章魚 LDPQ
mob_dict["9300007"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:35,hp_max:4900,mp_max:0,accuracy:100,avoidability:15,weapon_defense:120,magic_defense:150,kb:0,speed:90,exp:288,height:1,hurt_sound:7,die_sound:10},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.2846}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{stand_frame:35},CustomModelData:10193,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:9.5}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 次元之哀目
mob_dict["9300008"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","ldpq_eye","new_enemy","no_anger","no_jump"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{move_speed:0.1,info:{level:43,hp_max:7100,mp_max:0,accuracy:120,avoidability:18,weapon_defense:470,magic_defense:70,kb:200,speed:60,exp:340,width:1,height:2,hurt_sound:8,die_sound:11},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.0},{Name:"generic.follow_range",Base:0.0}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","ldpq_eye","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:113,stand_frame:61},CustomModelData:10407,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:11.0}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 次元之怒目
mob_dict["9300014"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","ldpq_eye","new_enemy","no_anger","no_jump","ice_resist","lightning_resist","fire_resist","holy_resist","freeze_immune"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{move_speed:0.112,info:{level:43,hp_max:6500,mp_max:0,accuracy:120,avoidability:18,weapon_defense:70,magic_defense:470,kb:200,speed:70,exp:340,width:1,height:2,hurt_sound:8,die_sound:11},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.0},{Name:"generic.follow_range",Base:0.0}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","ldpq_eye","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:113,stand_frame:61},CustomModelData:10231,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:11.0}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 積木泥人王 LDPQ
mob_dict["9300013"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy","no_jump"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:200,hp_max:99999,mp_max:0,accuracy:999,avoidability:999,weapon_defense:999,magic_defense:999,kb:99999,speed:60,exp:1,width:3,height:6,hurt_sound:9,die_sound:13},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.23238}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:28,stand_frame:14},CustomModelData:10583,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:3.0,Attributes:[{Name:"generic.attack_damage",Base:97.9}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 積木泥人 LDPQ
mob_dict["9300009"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy","no_jump","fire_weakness","ice_resist","lightning_resist"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:40,hp_max:6500,mp_max:0,accuracy:150,avoidability:12,weapon_defense:130,magic_defense:110,kb:300,speed:40,exp:408,width:3,height:6,hurt_sound:9,die_sound:12},AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.18974}],Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:28,stand_frame:14},CustomModelData:10627,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:3.0,Attributes:[{Name:"generic.attack_damage",Base:12.5}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 泥人領導者 LDPQ
mob_dict["9300010"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy","boss","no_jump"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:47,hp_max:33000,mp_max:220,accuracy:150,avoidability:18,magic_attack:195,weapon_defense:185,magic_defense:200,kb:1000,speed:50,exp:850,width:3,height:6,hurt_sound:10,die_sound:14,skill_id:2},steal_loot:"skill:steal/special/pass_pq",AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.21213}],DeathLootTable:"skill:mob/special/pass_pq",Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:28,stand_frame:14},CustomModelData:10671,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","boss","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:3.0,Attributes:[{Name:"generic.attack_damage",Base:15.5}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 妖魔 LDPQ
mob_dict["9300015"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy","no_jump","heal_target"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:37,hp_max:2750,mp_max:30,accuracy:135,avoidability:22,weapon_defense:90,magic_defense:120,kb:0,speed:80,exp:82,height:1,hurt_sound:11,die_sound:15},AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.26833}],Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:16,stand_frame:16},CustomModelData:10770,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","heal_target","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:9.7}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 進化妖魔 LDPQ
mob_dict["9300016"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy","no_jump","heal_target"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:41,hp_max:3050,mp_max:50,accuracy:145,avoidability:24,magic_attack:142,weapon_defense:130,magic_defense:160,kb:0,speed:85,exp:99,height:2,hurt_sound:11,die_sound:16},AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.27659}],Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:16,stand_frame:16},CustomModelData:10804,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","heal_target","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:10.5}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''
# 妖魔隊長 LDPQ
mob_dict["9300017"] = '''summon ocelot ~ ~ ~ {%(prefix)sTags:["ldpq_mob","new_enemy","no_jump","heal_target"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{level:46,hp_max:3600,mp_max:70,accuracy:155,avoidability:26,magic_attack:160,weapon_defense:170,magic_defense:200,kb:300,speed:90,exp:115,height:2,hurt_sound:11,die_sound:17},AttributeModifiers:[{AttributeName:"generic.movement_speed",Name:"slow",Amount:0,Operation:2,UUID:[I;0,2,0,2]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Age:-2147483648,Trusting:1,Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.movement_speed",Base:0.2846}],Invulnerable:1b,OnGround:1b,Team:"enemy",Passengers:[{id:"minecraft:zombified_piglin",Tags:["ldpq_mob","new_enemy"%(add_tag)s],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{info:{move_frame:16,stand_frame:16},CustomModelData:10869,CustomPotionColor:0}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Attributes:[{Name:"generic.attack_damage",Base:0.0},{Name:"generic.follow_range",Base:0.0}],Invulnerable:1b,AngerTime:2147483647,Team:"enemy"},{id:"minecraft:magma_cube",Tags:["ldpq_mob","new_enemy","heal_target","original"%(add_tag)s],NoAI:1,Invulnerable:1,Size:1.0,Attributes:[{Name:"generic.attack_damage",Base:11.0}],ArmorItems:[{},{},{},{id:"minecraft:potion",Count:1b,tag:{AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"disorder",Amount:0,Operation:0,UUID:[I;0,1,0,1]}]}}],ArmorDropChances:[0.0,0.0,0.0,0.0],Silent:1,PersistenceRequired:1,Team:"enemy",CustomName:'{"text":"2","font":"space:default"}',CustomNameVisible:1b}]}'''

def spawn_mob(id, is_summon=False, uuid=None, prefix=None):
	args = {
		"add_tag": '',
		"prefix": ''
	}
	if is_summon:
		args["add_tag"] = ',"new_summon"'
	if uuid:
		args["prefix"] += f"UUID:[I;1,0,1,{uuid}],"
	if prefix:
		args["prefix"] += prefix
	return (mob_dict[id] %args)