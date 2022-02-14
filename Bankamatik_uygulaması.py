# BANKAMATİK UYGULAMASI

hesapA = {
    "ad" : "Ali Akar",
    "hesapNo" : "1234",
    "bakiye" : 3000,
    "ekHesap" : 2000
    }


hesapB = {
    "ad" : "Veli Akar",
    "hesapNo" : "4321",
    "bakiye" : 2000,
    "ekHesap" : 1000
    }

def paraÇek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")


    if hesap["bakiye"] >= miktar:

        kalanBakiye = hesap["bakiye"] - miktar

        print(f"{hesap['hesapNo']} nolu hesabınızdan {miktar} TL parayı alabilirsiniz.")
        print(f"Kalan bakiyeniz {kalanBakiye} TL'dir.")

        KalanToplamMiktar = kalanBakiye + hesap["ekHesap"]
        print(f"{hesap['hesapNo']} nolu hesabınızdan kalan para toplam {KalanToplamMiktar} TL'dir.")

        hesap["bakiye"] = kalanBakiye

    else:

        print(f"Üzgünüz {hesap['hesapNo']} nolu hesabınızda yeterli bakiye bulunmamaktadır.Hesabınızdaki bakiye {hesap['bakiye']} TL'dir.")

        toplam = hesap["bakiye"] + hesap["ekHesap"]
        

        if toplam >= miktar:

            ekHesapKullanımı = input("Ek hesap kullanılsın mı? (e/h)")

            if ekHesapKullanımı == "e":

                ekHesapKullanılacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0

                hesap["ekHesap"] -= ekHesapKullanılacakMiktar
            
                print(f"{hesap['hesapNo']} nolu hesabınızdan {miktar} TL parayı alabilirsiniz.")
                KalanToplamMiktar = toplam - miktar
                print(f"{hesap['hesapNo']} nolu hesabınızdan kalan para toplam {KalanToplamMiktar} TL'dir.")
                
            
            elif ekHesapKullanımı == "h":
                print(f"Üzgünüz {hesap['hesapNo']} nolu hesabınızdan para çekişi yapamazsınız. Hesabınızdaki bakiye {hesap['bakiye']} TL'dir.")
                print(f"{hesap['hesapNo']} nolu hesabınızdan kalan para toplam {toplam} TL'dir.")

            

        else:
            print(f"Üzgünüz {hesap['hesapNo']} nolu hesabınızda yeterli para bulunmamaktadır.Hesabınızdaki bakiye {hesap['bakiye']} TL'dir.")
            print(f"{hesap['hesapNo']} nolu hesabınızdan kalan para toplam {toplam} TL'dir.")
        


def bakiyeSorgula(hesap):
    print(f"Merhabab {hesap['ad']} bey.")
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bakiye bulunmaktadır. Ek hesabınızda ise {hesap['ekHesap']} TL bulunmaktadır.")


print("\n---------------------------\n")

bakiyeSorgula(hesapB)

print("\n")

bakiyeSorgula(hesapA)

print("\n---------------------------\n")

paraÇek(hesapA,900)

print("\n---------------------------\n")

paraÇek(hesapA,4000)

print("\n---------------------------\n")

paraÇek(hesapA,300)

print("\n---------------------------\n")

bakiyeSorgula(hesapA)

"""
Eğer böyle bu uygulamadaki gibi hesapA'yı obje şeklinde tanımlayınca bakiye mitav ve benzer
değişkenler fonksiyon içerisinde yapılan değişiklik adrestekini değiştirdiğinden 
obje içerisindeki bilgi de değişir. 

Ama bu bakiye miktar gibi değişkenleri ayrı ayrı tanımlasaydık 
fonksiyon içerisindeki değişiklik o dışardaki bilgiyi değiştiremezdi.

"""