
from calcs import calcs_class
import matplotlib.pyplot as plt

r0 = 6571000
mu = 398600.4415 * (10 ** 9)



acc = 0.0000812431



calcs = calcs_class(acc)


a =  1
b =  4
c = 1

calcs.fit()



#p, r = calcs.rungekutta4(a,b,c)

#plt.polar(p,r)
#plt.show()

