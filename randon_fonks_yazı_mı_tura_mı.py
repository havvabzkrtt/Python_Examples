
# YAZI MI TURA MI?

import random

para = ["yazı","tura"]
sonuc = random.choice(para)

secim = input("Yazı mı tura mı?\n")

if secim == sonuc :
    print("Kazandın! Para " + sonuc +  "geldi.")

else:
    print("Kaybettin! Para " + sonuc +  "geldi.")
