
from calcs import calcs_class
import matplotlib.pyplot as plt

r0 = 6571000
mu = 398600.4415 * (10 ** 9)



acc = 0.0000812431

acc = 0.01

calcs = calcs_class(acc)




a = -2.645520628082462
b = -2.528914258395517
c = -5.463660896314998


calcs.fit()

'''
p,r,t,u,u2 = calcs.rungekutta4(0.8, 0, 1)

plt.polar(p,r)
plt.show()
plt.plot(t, u)
plt.grid()
plt.show()
plt.plot(t, u2)
plt.grid()
plt.show()
'''