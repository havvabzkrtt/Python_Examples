# def İLE METHOD OLUŞTURMA

class Uçuş():
    havayolu = "THY"   

    
    def __init__(self, kod, kalkış, varış, süre, kapasite, yolcu): 
        self.kod = kod                                             
        self.kalkış = kalkış
        self.varış = varış
        self.süre = süre
        self.kapasite = kapasite
        self.yolcu = yolcu
        
  
    def anons_yap(self):   
            return "{} sefer sayılı {}-{} uçuşumuz {} dakika sürecektir".format(
                self.kod,
                self.kalkış,
                self.varış,
                self.süre)     
        
        
    def koltuk_sayısı_güncelle(self):
        return self.kapasite - self.yolcu
    
    
    def biletSatış(self, bilet_adedi = 1):
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi
            self.koltuk_sayısı_güncelle() 
            print("{} adet bilet satılmıştır. Kalan koltuk sayısı {}'tür. {} tane yolcu seyehat edecektir.".format(
                bilet_adedi,
                self.koltuk_sayısı_güncelle(),
                self.yolcu)) 
                # return yerine böyle de yazabiliriz.
        else:
            print("İşlem gerçekleştirilemedi. Yetersiz koltuk sayısı...")
            
            
            
    def bilet_iptal(self, bilet_adedi = 1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            print("{} adet bilet iptal edilmiştir. Güncel koltuk sayısı {}'tür. {} tane yolcu seyehat edecektir.".format(
                bilet_adedi,
                self.koltuk_sayısı_güncelle(),
                self.yolcu))
        else:
            print("İşlem gerçekleştirilemedi. İptal edilecek kadar yolcu yok...")
            
            
#####
uçuş1 = Uçuş("TK123", "İstanbul", "Ankara", 60, 150, 70) 

print(uçuş1.koltuk_sayısı_güncelle())  # 80

#####
uçuş2 = Uçuş("TK123", "İzmir", "Antalya", 40, 200 , 140)

print(uçuş2.biletSatış(7))    # 7 adet bilet satılmıştır. Kalan koltuk sayısı 53'tür. 147 tane yolcu seyehat edecektir.
# Eğer parantez içi boş bırakılsaydı bilet_adedi 1 olaaktı.

print(uçuş2.biletSatış(10))   # 10 adet bilet satılmıştır. Kalan koltuk sayısı 43'tür. 157 tane yolcu seyehat edecektir.
# Önceki işlemin üzerine devam etti.

""" *** class yapısıyla bilgi saklanır ve devamlılığı sağlanır. *** """

print(uçuş2.biletSatış(50))   # İşlem gerçekleştirilemedi. Yetersiz koltuk sayısı...
# Fonksiyonun içindeki if koşulu sağlanmadığı için fonksiyon içindeki işlemler yapılmadı.

print(uçuş2.koltuk_sayısı_güncelle())   # 43
# 50 bileti satamadığından yani işlem gerçekleşemediğinden koltuk sayısı 43 kaldı.


#####
uçuş3 = Uçuş("TK41", "İstanbul", "İzmir", 50, 150 , 50)

print(uçuş3.bilet_iptal(4))  # 4 adet bilet iptal edilmiştir. Güncel koltuk sayısı 104'tür. 46 tane yolcu seyehat edecektir.

print(uçuş3.koltuk_sayısı_güncelle())  # 104

print(uçuş3.bilet_iptal(55)) # İşlem gerçekleştirilemedi. İptal edilecek kadar yolcu yok...

# Bu işlemleri arka arkaya yaptı, üzerine ekleyerek.

"""
class yapısı; her işlemden sonra o güncel değerin saklanması ve o güncel değer üzerine update,
güncelleme almasını, o devamlılığı sağlar.
"""


