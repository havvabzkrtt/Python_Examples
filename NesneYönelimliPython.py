
# Boş bir class tanımladık. Bu tüzden hata almadık.
"""
class person:
    pass
"""
"""
if a > 10:
    pass     # Bu şekilde de hata almamak için pass keyword ünü kullanabiliriz.
"""

"""
class Car:
    def __init__  (self, brand,model,year):       # __init__  ---> Oluşturduğumuz nesneyi başlatmamıza yarar.
        self.brand = brand
        self.model = model          # self ---> O sırada oluşturulan nesneye ait özellikleri gösterir.
        self.year = year            # self ---> Kendisine ait olan.
                                    # self ---> Yerine " myObjetct"  veya başka bir şey de yazabilirdik.

    def brandmodel(self): 
        return f"Araba markası : {self.brand} ve modeli : {self.model}"    # Metod oluşturduk.


car_1 = Car("BMW","i5",2010)        # Yukarıdaki sıraya göre özellikleri yerleştirdik.
car_2 = Car("Audi","x6",2012)

#
car_1.brand = "BMW"
car_1.model = "i5"
car_1.year = 2010                # Burda yazdıklarımızı yukarda class ile yazdık.
                     
car_2.brand = "Audi"
car_2.model = "x6" 
car_2.year = 2012
#

print(car_1)           # <__main__.Car object at 0x000002851BBBFB50>  yazar.  car_1 bir Car nesnesidir.
print(car_1.brand)     # BMW

print(car_1.brandmodel())         # Metodu çağırdık.  # Araba markası : BMW ve modeli : i5
"""
"""

class Movie:
    def __init__(self, name, director):
        self.name = name
        self.director = director


movie_1 = Movie("Full Metal Jacget", "Kubrick")
movie_2 = Movie("Babel","Irarutu")

print(movie_1.director)
print(movie_2.director)

print(movie_1.name)
print(movie_2.name)
"""



class Students:


    school_name = "X Lisesi"

    number_of_students = 0


    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades
        Students.number_of_students += 1    # Her öğrenci oluşturulduğunda bu bir artsın.

        
    def average (self):          # metot
        return sum(self.grades) / len(self.grades)

    def schoolName(self):
        return f"Okulumuzun adı {self.school_name}"

print(Students.number_of_students)  # 0

student_1 = Students("ayşe",18, [14,26,72,84])
student_2 = Students("fatma",23,[20,40,70,90])

print(Students.number_of_students)   # 2    # İki öğrenci oluşturduk.

print(student_1.average())   # 49.0
print(student_2.average())   # 55.0



# instance (nesne) ---> studen_1 , student_2
# instance değişkenleri (instance properties) ---> name , age , grades


print(student_1.school_name)    # X Lisesi
print(student_2.school_name)    # X Lisesi
print(Students.school_name)     # X Lisesi


print(student_1.schoolName())  # Okulumuzun adı X Lisesi
print(student_2.schoolName())  # Okulumuzun adı X Lisesi
# print(Students.schoolName())   hata veriyor


print(student_1.__dict__)   # Nesnenin özelliklerini ve değerlerini verir.
# {'name': 'ayşe', 'age': 18, 'grades': [14, 26, 72, 84]}


print(Students.__dict__)    # Sınıf içerdiği özellikleri ve özelliklerin değerlerini gösterir.

# {'__module__': '__main__', 'school_name': 'X Lisesi', '__init__': <function Students.__init__ 
# at 0x0000023C8F0A25E0>, 'average': <function Students.average at 0x0000023C8F0A2670>, 'schoolName': <function Students.schoolName at 0x0000023C8F0A2700>, '__dict__': <attribute '__dict__' 
# of 'Students' objects>, '__weakref__': <attribute '__weakref__' of 'Students' objects>, '__doc__': None}
# *** "school_name" de buraya geldi.










