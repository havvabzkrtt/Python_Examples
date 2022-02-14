import csv
with open('deneme.csv', 'w', newline='') as file:
    Baslik_isimleri = ['Sporcu_ismi', 'Yasi']
    writer = csv.DictWriter(file, fieldnames=Baslik_isimleri)
    writer.writeheader() # Belirlediğimiz başlık isimlerini "writeheader()" fonksiyonuna bildir.
    writer.writerow({'Sporcu_ismi': 'Meryem Boz', 'Yasi': 33}) # Her satır için "writerow()" fonksiyona bildir.
    writer.writerow({'Sporcu_ismi': 'Yusuf Yazici', 'Yasi': 24})
    writer.writerow({'Sporcu_ismi': 'Cedi Osman', 'Yasi': 25})