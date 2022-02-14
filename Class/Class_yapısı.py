# "Class" yapısı ile kendimiz yeni ir type, değişken oluştururuz. 

# class

# Boş bir class tanımladık. Eğer içerisinde attributes veya method bulunmuyorsa içine 'pass' methodunu koyarak hatadan kurtulabiliriz.

"""
class person:
    # pass

    # class attributes
    adress = "No information"

        # constructor (yapıcı metod)
    
    def __init__(self, name, year):                     # self ==> Oluşturduğumuz classtan türetilen herhangi bir objeyi emsil eder.
                                            # selften sonra objelerin üzerine hangi attributeleri kullanmak istiyorsak selften sonra parantezin içine eklicez.
        # object attributes                 # self kelimesi yerine this gibi başka bir kelime de kullanılabilir.
        self.name = name
        self.year = year
    
    # instance method
    def intro(self):
        print("Hello there. I'm " + self.name +".")

    def calculateAge(self):
        return 2021 - self.year

# object (instance)


p1 = person("Ali",1999)    # person classtında p1 adlı bir obje türettik.
p2 = person(name = "Ahmet",year = 1995)
p3 = person("Aslı",2002)
p4 = person("Aleyna",2017)

p4.adress = "Kocaeli"

print(p1)    # <__main__.person object at 0x0000024A8DD87280>   bize bir adres belirtti.
print(p2)    # <__main__.person object at 0x000002F80A72A550>   bu da farklı bir adreste.

print(type(p1))    # <class '__main__.person'>

print(f"p1; name: {p1.name}, year: {p1.year}")   # p1; name: Ali, year:1999
print(f"p2; name: {p2.name}, year: {p2.year}")   # p2; name: Ahmet, year:1995
print(f"p3; name: {p3.name}, year: {p3.year}, adress: {p3.adress}")   # p3; name: Aslı, year: 2002, adress: No information
print(f"p4; name: {p4.name}, year: {p4.year}, adress: {p4.adress}")   # p4; name: Aleyna, year: 2017, adress: Kocaeli


p1.intro()  # Hello there. I'm Ali.
p2.intro()  # Hello there. I'm Ahmet.

print(f"Hello my name is {p3.name} and i am {p3.calculateAge()} years old.")  # Hello my name is Aslı and i am 19 years old.
print(f"Hello my name is {p4.name} and i am {p4.calculateAge()} years old.")  # Hello my name is Aleyna and i am 4 years old.


print("\n\n")
"""


class Cars:
    def __init__ (self, name, types, model):
        self.name = name
        self.type = types
        self.model = model

car = Cars("Taksi","Fiat","2002")    # Yukarıdaki bilgilere göre dolu olmalı eksik olursa TypeError hatası verir.

print(car.name)       # Taksi

print(type(car))      # <class '__main__.Cars'>    type'nı verdi
a = 3
print(type(a))


print("\n\n")
"""
"""
class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

c1 = Circle()  # yaricap = 1
c2 = Circle(5)

print(f"c1 : çevre = {c1.cevre_hesapla()} , alan = {c1.alan_hesapla()}")   # c1 : çevre = 6.28 , alan = 3.14
print(f"c2 : çevre = {c2.cevre_hesapla()} , alan = {c2.alan_hesapla()}")   # c2 : çevre = 31.400000000000002 , alan = 78.5

print("\n\n")





# *** INHERITANCE (KALITIM  = Class'ların birbirinden mirasalması) ***