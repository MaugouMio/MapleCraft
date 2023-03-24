data merge entity @s {text:'{"text":"0","font":"skill:230/1002/hit/0"}',Tags:['{"text":"","font":"skill:230/1002/hit/0"}', '{"text":"","font":"skill:230/1002/hit/1"}'],billboard:"vertical",background:0}
execute store result entity @s text_opacity byte 1 run scoreboard players get #DEFAULT_SIZE temp
scoreboard players set @s max_life 18
scoreboard players set @s type 1
