import sqlite3

baglanti2 = sqlite3.connect("deneme2.db")
    
imlec = baglanti2.cursor()

"""
imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT, yas INT, cinsiyet TEXT)")    #

imlec.execute("INSERT INTO ekip VALUES('İlkin', 22, 'Erkek')")  
imlec.execute("INSERT INTO ekip VALUES('Eva', 19, 'Kadın')")
imlec.execute("INSERT INTO ekip VALUES('Ahmet', 21, 'Erkek')")
imlec.execute("INSERT INTO ekip VALUES('Elif', 20, 'Kadın')")
imlec.execute("INSERT INTO ekip VALUES('Erdem', 25, 'Erkek')")
"""

## VERİ SEÇME ##

"""
***
imlec.execute("SELECT * from ekip")  # Ekip'ten bütün verileri seçtik.

# ** imlec.fetchall()    # Seçilen bütün verileri liste içerisinde toplar.
# print(imlec.fetchall())    # Seçilen bütün verileri liste halinde ekrana yazdırır.

for veri in imlec.fetchall():
    # print(veri)   # Bütün verileri yazdı.
    # print(veri[1])  # Verilerin 1. indeksteki elemanlarını yazdı. Yani yaşları.
    if veri[1] > 22:
        print(veri[0])   # Yaşı 22'den büyü olanların ismi ekrana yazdırıldı.
"""       
"""
***
imlec.execute("SELECT yas from ekip")    # Ekip'ten yas verilerini çektik.

print(imlec.fetchall())  # Seilen yas verilerinin tümünü ekrana liste halinde yazdırdı.

imlec.execute("SELECT isim, yas from ekip")  # Ekip'ten isim ve yas verilerini seçti.
"""

# Parantez içindeki komutları, SQL komutlarını internetten bulabiliriz.
"""
***
# BİR ŞART İLE ÇEKME

imlec.execute("SELECT * from ekip WHERE yas > 20")  # Ekip'ten yası 20 den küçük olanları seçtik.

print(imlec.fetchall())

"""
"""
***
imlec.execute("SELECT * from ekip WHERE yas <20 AND cinsiyet == 'Kadın' ")

print(imlec.fetchall())    # [('Eva', 19, 'Kadın')]
"""


## VERİ TABANINDAKİ BİR DEĞERİ GÜNCELLEME ## 
"""
imlec.execute("UPDATE ekip SET yas=20 WHERE isim = 'Eva'")   # Eva'nın yaşını değiştirdik.
"""
# VERİYİ SİLME
"""
imlec.execute("DELETE FROM ekip WHERE isim = 'Ahmet'")  # Ahmet'in satırını komple sildik.
"""

# Büyük harfle yazılan bu komutlar küçük harfle de yazılabilir.

baglanti2.commit() 

baglanti2.close() 




















