import numpy as np

from calcs import calcs_class
import matplotlib.pyplot as plt


r_0 = 1
r_k = 42164/(6371+200)
phi_0 = 0
acc = 0.000081328



calcs = calcs_class(acc)






x,y = calcs.rungekutta4()


plt.polar(x, y)

plt.grid()
plt.show()


