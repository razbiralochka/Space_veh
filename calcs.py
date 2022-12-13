import numpy as np


def core(x,y):
    global mu
    global mass
    global thrust
    global vars
    global alpha
    global acc

    '''
    0 - radius
    1 - time
    2 - radial speed
    3 - angular speed
    4 - mass
    '''

    mu = 398.6e12
    mass = 20000
    thrust = 100
    alpha = np.pi/2
    acc = 0
    vars = np.zeros(5)
    vars[0] = (6371 + 400) * 1000
    vars[3] = np.sqrt(mu / vars[0])
    angle = 0
    h = 5*np.pi/180

    k = np.zeros((5, 4))

    while vars[0] <= 42164000:

        x.append(vars[0]/1000 * np.cos(angle))
        y.append(vars[0]/1000 * np.sin(angle))

        #acc =  5.4*2 / 20_000
        acc = 1*10 / 20_000
        k[:, 0] = diffs(vars)
        k[:, 1] = diffs(vars + k[:, 0] / 2)*2
        k[:, 2] = diffs(vars + k[:, 1] / 2)*2
        k[:, 3] = diffs(vars + k[:, 2])

        k *= h/6

        dvars = [sum(elem) for elem in k]

        vars += dvars



        angle += h
    print(vars[1]/86400)
    return x, y


def diffs(args):
    r_ = args[0]
    time_ = args[1]
    Vr_ = args[2]
    Vphi_ = args[3]

    mass_ = args[4]
    dr_ = Vr_*r_/Vphi_
    dtime_ =  r_/Vphi_
    dVr_ = Vphi_-mu/(r_*Vphi_)+np.cos(alpha)*acc*r_/Vphi_
    dVphi_ = -Vr_+np.sin(alpha) * acc * r_/Vphi_
    res = np.array([dr_, dtime_, dVr_, dVphi_, mass_])

    return res












