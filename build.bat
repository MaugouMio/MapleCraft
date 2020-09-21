mcdp make MapleCraft data pack
rd /S /Q "C:\Users\user\AppData\Roaming\.minecraft\saves\MapleCraft test\datapacks\MapleCraft data pack"
xcopy "C:\Users\user\Desktop\MapleCraft\MapleCraft data pack\build\MapleCraft data pack" "C:\Users\user\AppData\Roaming\.minecraft\saves\MapleCraft test\datapacks\MapleCraft data pack" /E /Y /I /Q
rd /S /Q "C:\Users\user\Desktop\MapleCraft\MapleCraft data pack\build\MapleCraft data pack"
pause