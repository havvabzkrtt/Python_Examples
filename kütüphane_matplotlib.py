from matplotlib import pyplot as plt
from matplotlib import style

x = [1,2,3]
y = [3,2,1]


#plt.plot([1,2,3],[3,2,1])   # x,y
plt.plot(x,y)
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.title("denemee")        # Başlık

plt.show()

style.use('ggplot')

x = [1,2,3]
y = [3,2,1]
x1 = [1,2,3]
y1 = [5,6,7]

plt.plot(x,y,'g', label = 'birinci çizgi', linewidth = 6)   # linewidth ==>> çizginin kalınlığını ayarlar.  g c ==> çizgi renkleri
plt.plot(x1,y1,'c', label = 'ikinci çizgi', linewidth = 6)
plt.title("Style ile denemee")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.legend()
plt.grid(True, color = 'k')

plt.show()