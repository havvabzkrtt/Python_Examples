from tkinter import font
import turtle
import time   # programın hızını ayarlamak için
import random

from matplotlib.font_manager import FontProperties

hiz = 0.10

# Pencere
pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('lightgreen')
pencere.setup(width=600, height=600)
pencere.tracer(0)


# Yılanın Kafası
kafa = turtle.Turtle()
kafa.speed(0)  # Hızı 0
kafa.shape('square') # şekli kare
kafa.color('black')  
kafa.penup()  # hareket ederken herhangi bir şey yazmıcak
kafa.goto(0, 100)  # 0 a 100 noktasına götürdük
kafa.direction = 'stop' # ilk başta yönünü sıfır olarak belirliyoruz


# Yem 

yem = turtle.Turtle()
yem.speed(0)  # Hızı 0
yem.shape('circle') # şekli daire
yem.color('red')  
yem.penup()  # hareket ederken herhangi bir şey yazmıcak
yem.goto(0, 0)  # 0 a 0 noktasına götürdük
yem.shapesize(0.80 , 0.80)  # büyüklüğü


# Kuyruk Ekleme


kuyruklar = []

# Puan Sistemi

puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('white')
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle() # herhangi bir şekli olmayacağından şekli kapattık
yaz.write('Puan: {}'.format(puan), align='center' , font=('Coruier',24,'normal'))  # tipi normal




# Hareket Sitemi

def move():
    if kafa.direction == 'up':   # kafanın yönü yukarı doğruysa yukarı doğru hareket ettirmemiz lazım 
        y = kafa.ycor()  # y koordinatını öğrenmemiz lazım 
        kafa.sety(y + 20) # y koordinatını arttırıyoruz

    # Diğer yönler için de aynı şekilde

    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 20)  # y koordinatını azaltıyoruz 

    if kafa.direction == 'right':
        x = kafa.xcor()  # sağ taraf için x noktasını alıyoruz
        kafa.setx(x + 20) # x koordinatını arttırıyoruz 
    
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 20) # x koordinatını azaltıyoruz


def goUp():  # kafanın yönü down değilse bu fonksiyonla up yapılacak
    if kafa.direction != 'down':  
        kafa.direction = 'up'


def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'

def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'

def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'



# Klavye Kontrolü

pencere.listen()
pencere.onkey(goUp, 'Up')
pencere.onkey(goDown, 'Down')
pencere.onkey(goRight, 'Right')
pencere.onkey(goLeft, 'Left')


while 1:
    pencere.update()
    
    # Kafa Kenarlara Çarparsa Oyunu Sıfırlama

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = 'stop'

        # kuyruklar pencerenin dışına taşınır
        for kuyruk  in kuyruklar:
            kuyruk.goto(1000, 1000)

        kuyruklar = []  # listeyi sıfırlıyoruz
        hiz = 0.10 # hızı tekrar eski haline getirdik

        puan = 0 # puan sıfırlanacak ve tekrar yazdırıyoruz
        yaz.clear()
        yaz.write('Puan: {}'.format(puan), align='center' , font=('Coruier',24,'normal'))



    # Kafa yemi yerse

    if kafa.distance(yem) < 20:  # kafa ile yem arasındaki mesafe 20den azsa
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yem.goto(x, y)  # yemi bu noktaya getiririz

        hiz = hiz - 0.001  # her yemi yemede hızı düşürürüz

        puan = puan + 10  # yemi yedikçe puan artacak
        yaz.clear()  # önceki yazıyı sildiriyoruz
        yaz.write('Puan: {}'.format(puan), align='center' , font=('Coruier',24,'normal'))  # yeni yazıyı yazdırıyoruz

        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0) 
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()  # hareket ederken herhangi bir çizgi çizmeyecek
        kuyruklar.append(yeniKuyruk)

    
    # Kuyruklar listesindeki her bir kuyruk bir öncekinin yerini alacak,
    # en son kuyruk da kafanın yerine geçeçek.

    for i in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[i - 1].xcor()  # bir öncekinin x koordinatı
        y = kuyruklar[i - 1].ycor()  # bir öncekinin y koordinatı
        kuyruklar[i].goto(x, y)    # i inci kuyruk bir öncdeki kuyruğun yerini alıyor

    if len(kuyruklar) > 0:
        x = kafa.xcor()  # kafanın xkoordinatı 
        y = kafa.ycor()  # kafanın y koordinatı
        kuyruklar[0].goto(x, y)  # kuyrukların en başındaki kafanın yerini alır


    move()
    time.sleep(hiz)  # programı yavaşlatmak için