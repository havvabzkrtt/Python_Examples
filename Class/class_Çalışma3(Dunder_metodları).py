# DUNDER METODLAR

class Uçuş():
    havayolu = "THY"   

    def __init__(self, kod, kalkış, varış, süre, kapasite, yolcu): 
        self.kod = kod                                             
        self.kalkış = kalkış
        self.varış = varış
        self.süre = süre
        self.kapasite = kapasite
        self.yolcu = yolcu
        
    def __repr__(self):
        return "{} sefer sayılı uçuş, sistemde oluşturulmuştur..".format(self.kod)        
  
            
        
# *** __repr__() metodu için fonksiyon oluşturulmasaydı ***           

"""            
uçuş1 = Uçuş("TK123", "İstanbul", "Ankara", 60, 150, 70)

print(uçuş1.__dir__())    # Uçuş'a ait methodları, attribüte'ları, özellikleri görürüz.

print(uçuş1)   # <__main__.Uçuş object at 0x0000020ECA1747F0>
# Bellekte tutulduğu yeri gösterir.
# __repr__() komutu da aynı işlevi yapar.
print(uçuş1.__repr__())  # <__main__.Uçuş object at 0x0000020ECA10F610>
"""

# *** __repr__() metodu için fonksiyon oluşturuldu ***

uçuş1 = Uçuş("TK123", "İstanbul", "Ankara", 60, 150, 70)

print(uçuş1)   # TK123 sefer sayılı uçuş, sistemde oluşturulmuştur..

print(uçuş1.__repr__())   # TK123 sefer sayılı uçuş, sistemde oluşturulmuştur..

