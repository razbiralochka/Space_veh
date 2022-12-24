
from calcs import calcs_class
import matplotlib.pyplot as plt

r0 = 6571000
mu = 398600.4415 * (10 ** 9)



acc = 0.0000812431

acc = 0.01

calcs = calcs_class(acc)


a = -17.725650336335367
b = -19.435330862104223
c = 22.42872260036432

calcs.fit()


'''
p,r,tl,ul,u2= calcs.rungekutta4(0.5,0.707,0.707)

plt.polar(p,r)
plt.show()

plt.plot(tl,ul)
plt.show()
plt.plot(tl,u2)
plt.show()
'''