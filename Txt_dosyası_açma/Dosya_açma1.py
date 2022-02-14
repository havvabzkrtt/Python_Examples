"""
Öncelikle deneme.txt adli bir dosya olusturduk.
Bu dosyayi dosya adli bir degiskene atadik.
"open()" nın simdilik bu sekilde dosya olusturuldugunu bilelim yeter.
Gördügünüz gibi fonksiyonu da tipki type(), len(), open() pow() ve print()
fonksiyonları gibi birtakım parametreler alıyor.
"""
# deneme1.txt
"""
Bu fonksiyonun ilk parametresi
“deneme1.txt” adli bir karakter dizisi.
Iste bu karakter dizisi bizim olusturmak istedigimiz
dosyanin adini gösteriyor.
"""

# w
"""
Ikinci parametre ise “w” adli baska bir karakter dizisi. Bu da
deneme.txt dosyasinin yazma kipinde (modunda) açilacagini gösteriyor.
"""

# Here we go!

dosya = open("deneme1.txt", "w")
print("Ben Python , Monty Python", file=dosya)
dosya.close()

# Sonuç
"""
Herhangi bir çikti almadiniz, degil mi? Evet. Çünkü yazdigimiz bu kodlar sayesinde
print()
fonksiyonu, çiktilarini deneme1.txt adli bir dosyaya yazdirdi.
"""
"""
Gördügünüz gibi, gerçekten de Python dosyaya yazdirmak istedigimiz bütün verileri önce
tamponda bekletti, daha sonra dosya kapatilinca tamponda bekleyen bütün verileri dosyaya
bosaltti.
"""

# Oluşturduğumuz dosya nerede?
"""
Olusturdugumuz bu deneme.txt adli dosya, o anda bulundugunuz dizin içinde olusacaktir.
Bu dizinin hangisi oldugunu ögrenmek için su komutlari verebilirsiniz:
"""
import os
os.getcwd()

# c:/users/hp/appdata/local/programs/python/python39/python.exe "c:/Users/HP/Documents/PYTHON/DOSYA AÇMA/Dosya_açma1.py"