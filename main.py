import numpy as np

from calcs import calcs_class
import matplotlib.pyplot as plt


r_0 = 1
vphi_0 = 1/np.sqrt(r_0)
vr_0 = 0
r_k = 42164/(6371+200)
v_phi_k= 1/np.sqrt(r_k)

vr_k = 0
acc = 0.000081328



calcs = calcs_class(acc, r_0, vphi_0, vr_0, r_k,v_phi_k, vr_k)






x,y = calcs.rungekutta4()


plt.polar(x, y)

plt.grid()
plt.show()


