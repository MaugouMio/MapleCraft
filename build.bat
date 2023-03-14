mcdp make MapleCraft data pack
rd /S /Q "C:\Users\MaugouMio\AppData\Roaming\.minecraft\saves\MapleCraft test\datapacks\MapleCraft data pack"
xcopy "C:\Users\MaugouMio\Desktop\MapleCraft\MapleCraft data pack\build\MapleCraft data pack" "C:\Users\MaugouMio\AppData\Roaming\.minecraft\saves\MapleCraft test\datapacks\MapleCraft data pack" /E /Y /I /Q
copy /Y "C:\Users\MaugouMio\Desktop\MapleCraft\pack.mcmeta" "C:\Users\MaugouMio\AppData\Roaming\.minecraft\saves\MapleCraft test\datapacks\MapleCraft data pack\pack.mcmeta"
rd /S /Q "C:\Users\MaugouMio\Desktop\MapleCraft\MapleCraft data pack\build\MapleCraft data pack"
pause