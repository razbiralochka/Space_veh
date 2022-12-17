
from calcs import calcs_class
import matplotlib.pyplot as plt

r0 = 6571000
mu = 398600.4415 * (10 ** 9)



acc = 0.000081328



calcs = calcs_class(acc)






p,r,t,v = calcs.rungekutta4(0,0)


plt.polar(p,r)
plt.show()

plt.plot(t,v)
plt.grid()
plt.show()



