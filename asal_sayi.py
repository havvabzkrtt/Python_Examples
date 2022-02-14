# GİRİLEN SAYININ ASAL OLUP OLMAMASI

sayi = int(input("Bir sayı giriniz: "))
asalmi = True

if sayi == 1:
    asalmi = False

if sayi == 2:
    asalmi = True

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break
    
if asalmi:
    print(f"{sayi} sayısı bir asal sayıdır.")
else: 
    print(f"{sayi} sayısı bir asal sayı değildir.")