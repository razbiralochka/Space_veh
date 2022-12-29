from calcs import calcs_class
import matplotlib.pyplot as plt
import numpy as np
r0 = 6571000
mu = 398600.4415 * (10 ** 9)


acc = 0.0000812431

acc = 0.001


calcs = calcs_class(acc)

a = 100
b = 1
c = 1

#calcs.fit()

p,r,tl,ul,u2= calcs.rungekutta4(a,b,c)

plt.polar(p,r)
plt.show()

n = [0.5*elem/np.pi for elem in p]

plt.plot(n, r)
plt.plot(n, ul)
plt.grid()
plt.show()
plt.plot(n,u2)
plt.show()
