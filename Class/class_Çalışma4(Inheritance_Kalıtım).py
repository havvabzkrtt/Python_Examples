# INHERITANCE (KALITIM)

"""
İnsan diye üst class; bu class'ın altında öğrenci ve profesör diye alt class'lar var.
Süper class (İnsan class'ı) kalıtım yoluyla kendi attribute ve metodlarını alt classlara
(öğrenci ve profesör class'ları) aktarabilir. Alt class'lar da kendine ait attribute ve 
metodlara sahip olabilir.
"""

# ** Üst class **

class Seyahat():
    
    def __init__(self,kalkış,varış):
        self.kalkış = kalkış
        self.varış = varış
        
    def anons(self):
        return "{}-{} seyehatine hoşgeldiniz..".format(self.kalkış,self.varış)
 
# ** Alt class **

class Otobüs(Seyahat):    # Parantez içine üst class'ı yazarak derleyiciye bağlantıyı gösterdik.
    
    def __init__(self,mola_durakları):
        Seyahat.__init__(self,"İstanbul","Ankara")   # *****kalkış ve varış ı biz elle vermiş olduk.
        self.mola_durakları = mola_durakları
        
        
seyahat1 = Seyahat("Antalya","Bodrum")

print(seyahat1.kalkış)     # Antalya
print(seyahat1.anons())    # Antalya-Bodrum seyehatine hoşgeldiniz..


oto1 = Otobüs(["Fethiye","Alanya"])

print(oto1.mola_durakları)     # ['Fethiye', 'Alanya']

# Seyahat class'ına ait attribute ve metodlara da sahiptir.
print(oto1.kalkış)    # İstanbu
print(oto1.varış)     # Ankara
print(oto1.anons())   # İstanbul-Ankara seyehatine hoşgeldiniz..

#########################################################################################333

# ** Üst class **

class Seyahat():
    
    def __init__(self,kalkış,varış):
        self.kalkış = kalkış
        self.varış = varış
        
    def anons(self):
        return "{}-{} seyehatine hoşgeldiniz..".format(self.kalkış,self.varış)
 
# ** Alt class **

class Otobüs(Seyahat):    # Parantez içine üst class'ı yazarak derleyiciye bağlantıyı gösterdik.
    
    def __init__(self,mola_durakları,kalkış,varış):
        Seyahat.__init__(self,kalkış,varış)   # ***** kalkış ve varış için parametre girişi yaptırdık 
        self.mola_durakları = mola_durakları
        
        
seyahat1 = Seyahat("Ankara","Kars")

print(seyahat1.kalkış)     # Ankara
print(seyahat1.anons())    # Ankara-Kars seyehatine hoşgeldiniz..


oto1 = Otobüs(["Fethiye","Alanya"],"İstanbul","İzmir")

print(oto1.mola_durakları)     # ['Fethiye', 'Alanya']

# Seyahat class'ına ait attribute ve metodlara da sahiptir.
print(oto1.kalkış)    # İstanbul
print(oto1.varış)     # İzmir
print(oto1.anons())   # İstanbul-İzmir seyehatine hoşgeldiniz..
