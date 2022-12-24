
from calcs import calcs_class
import matplotlib.pyplot as plt

r0 = 6571000
mu = 398600.4415 * (10 ** 9)


acc = 0.0000812431

acc = 0.002

calcs = calcs_class(acc)


a = 92.3299923511243
b = 17.4976861851753
c = -47.978397734728915

#calcs.fit()



p,r,tl,ul,u2= calcs.rungekutta4(a,b,c)

plt.polar(p,r)
plt.show()

plt.plot(tl,ul)
plt.show()
plt.plot(tl,u2)
plt.show()
