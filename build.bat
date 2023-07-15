@set target_datapack=%appdata%\.minecraft\saves\MapleCraft test\datapacks\MapleCraft data pack

tools\mcdp.py make MapleCraft data pack
rd /S /Q "%target_datapack%"
xcopy "MapleCraft data pack\build\MapleCraft data pack" "%target_datapack%" /E /Y /I /Q
copy /Y "MapleCraft data pack\pack.mcmeta" "%target_datapack%\pack.mcmeta"
rd /S /Q "MapleCraft data pack\build\MapleCraft data pack"
pause