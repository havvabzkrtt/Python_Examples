dosya2 = open("kişisel_bilgiler.txt","w")
print("Havvanur Bozkurt",file=dosya2)
print("Öğrenci : üniversite 1. sınıf",file=dosya2)
print("Bu kadar bilgi yeter!!",file=dosya2, flush=True)

import os
os.getcwd()