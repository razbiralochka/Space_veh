from calcs import core
import  matplotlib.pyplot as plt





x = list()
y = list()


x,y = core(x,y)


plt.plot(x,y)
plt.axis('equal')
plt.grid()
plt.show()