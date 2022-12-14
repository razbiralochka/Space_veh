import numpy as np

from calcs import calcs_class
import  matplotlib.pyplot as plt


r_0 = (6371+200)/42164
vphi_0 = 1/np.sqrt(r_0)
vr_0 = 0
r_k = 1
v_phi_k= 1
vr_k = 0



calcs = calcs_class(r_0, vphi_0, vr_0, r_k, v_phi_k, vr_k)






x,y = calcs.rungekutta4()


plt.plot(x,y)
plt.axis('equal')
plt.grid()
plt.show()


