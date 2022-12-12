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
    1 - angle
    2 - radial speed
    3 - angular speed
    4 - mass
    '''

    mu = 398.6e12
    mass = 20000
    thrust = 100
    alpha = 0
    acc = 0
    vars = np.zeros(5)
    vars[0] = (6371 + 10000) * 1000
    vars[3] = np.sqrt(mu / vars[0])
    t = 0
    h = 20

    k = np.zeros((5, 4))

    while t < 100*86400:


        print(h)
        x.append(vars[0] * np.cos(vars[1])/1000)
        y.append(vars[0] * np.sin(vars[1])/1000)
        acc = 0

        k[:, 0] = diffs(vars)
        k[:, 1] = diffs(vars + k[:, 0] / 2)*2
        k[:, 2] = diffs(vars + k[:, 1] / 2)*2
        k[:, 3] = diffs(vars + k[:, 2])



        k *= h/6

        dvars = [sum(elem) for elem in k]

        vars += dvars

        if vars[0] > 42000000 or vars[0] < 0:
            break

        t += h

    return x, y


def diffs(args):

    r_ = args[0]
    phi_ = args[1]
    Vr_ = args[2]
    Vphi_ = args[3]
    mass_ = args[4]
    dr_ = Vr_
    dphi_ =  Vphi_/r_
    dVr_ = (Vphi_ ** 2) / r_ - mu / pow(r_, 2) + np.sin(alpha) * acc
    dVphi_ = -(Vr_*Vphi_)/r_+np.cos(alpha)*acc
    res = np.array([dr_, dphi_, dVr_, dVphi_, mass_])
    return res












