class Uçuş():
    havayolu = "THY"   
    # "havayolu" attribute'si ==> Bu class'ın bütün objeleri için ortak özellik. class'a özgü attribute'tur.
    
    def __init__(self, kod, kalkış, varış, süre, kapasite, yolcu): # Burdaki attributler her obje için farklıdır. Objeye özgü attribute'tur.
        self.kod = kod                                             
        self.kalkış = kalkış
        self.varış = varış
        self.süre = süre
        self.kapasite = kapasite
        self.yolcu = yolcu
        
    # METOD OLUŞTURALIM
    def anons_yap(self):   # self olmalı, yanında başka parametreler de olabilir normal fonksiyonlarda olduğu gibi.
            return "{} sefer sayılı {}-{} uçuşumuz {} dakika sürecektir".format(
                self.kod,
                self.kalkış,
                self.varış,
                self.süre)             # Paranteze uygun özellikleri sıraya göre yerleştiriryoruz.
        
"""   
uçuş1 = Uçuş()  # def __init__ olmadan böyle yazılınca haat vermez.
print(uçuş1.havayolu)   # THY   (THY => Türk Hava Yolları)     ** Bütün objeler için ortak.
"""

# uçuş2 = Uçuş()   # Böyleyken TypeError hatası verir. İçini doldurmak lazım.
# uçuş2 = Uçuş("TK123", "İstanbul", "Ankara","60","300") # Bir tane bile eksik olsa TypeError hatası verir.

uçuş2 = Uçuş("TK123", "İstanbul", "Ankara","60","300","50") 
# Böylece uçuş2 iki isimli Uçuş class'ına ait oje oluşturduk.

# Şimdi her bir attribute'ye ulaşabiliriz. uçuş1'de ulaşabildiğimiz gibi.

print(uçuş2.kod)       # TK123
print(uçuş2.varış)     # Ankara
print(uçuş2.yolcu)     # 50
print(uçuş2.havayolu)  # THY     ** Bütün objeler için ortak.


uçuş3 = Uçuş("TK142", "İzmir", "Antalya","70","200","100") 

print(uçuş3.kod)       # TK142
print(uçuş3.varış)     # Antalya
print(uçuş3.yolcu)     # 70
print(uçuş3.havayolu)  # THY     ** Bütün objeler için ortak.


print(uçuş3.anons_yap())     
# anons_yap fonksiyonunun içini boş bıraktık, çünkü self'ten başka herhangi bir parametre almadı. 
# Fonksiyonun ikinci bir parametresi olsaydı ona karşılık gelen bir parametre girmemiz gerekirdi.
# self, bahsedilen objenin devamlılığını yani ona refere ettiğini söylemek için oluturulan bir şeydir.
