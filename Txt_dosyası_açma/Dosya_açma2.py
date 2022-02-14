dosya2 = open("kişisel_bilgiler.txt","w")
print("Havvanur Bozkurt",file=dosya2)
print("Öğrenci : üniversite 1. sınıf",file=dosya2)
print("Bu kadar bilgi yeter!!",file=dosya2, flush=False)

import os
os.getcwd()

"""
flush=True olduğu için dosyayı kapatmaya gerek yok, flush = True olduğu sürece
yazılanlar dosyaya aktarılır. 
flush = False veya sadece flush yazılmamış olsaydı, dosya boş olacaktı, kapatmak gerekecekti.
"""