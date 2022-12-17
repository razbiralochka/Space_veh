
from calcs import calcs_class
import matplotlib.pyplot as plt

r0 = 6571000
mu = 398600.4415 * (10 ** 9)
r_0 = 1

phi_0 = 0
acc = 0.000081328



calcs = calcs_class(acc, r_0)






p,r = calcs.rungekutta4(0,0)


plt.polar(p,r)
plt.show()




