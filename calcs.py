import numpy as np

class calcs_class():
    def __init__(self, acc, radius, speedAng, speedrad, k_radius, k_speedAng ,k_speedrad):
        self.vars = np.zeros(5)
        self.vars[0] = radius
        self.vars[3] = speedAng
        self.vars[2] = speedrad
        self.rk = k_radius
        self.vars[4] = 0
        self.vphik = k_speedAng
        self.vrk = k_speedrad

        self.acc = acc

    def rungekutta4(self):

        args = np.array([elem for elem in self.vars])
        print(self.vars)
        x = list()
        y = list()
        angle = 0
        k = np.zeros((5, 4))
        h = 2 * np.pi/180
        while args[0] < self.rk:

            #h = 0.01/self.args[0]

            y.append(args[0])
            x.append(angle)

            k[:, 0] = self.diffs(args)
            k[:, 1] = self.diffs(args + k[:, 0] / 2) * 2
            k[:, 2] = self.diffs(args + k[:, 1] / 2) * 2
            k[:, 3] = self.diffs(args + k[:, 2])

            k *= h / 6

            dvars = [sum(elem) for elem in k]

            args += dvars

            angle += h
        print(angle/(2*np.pi))
        r0 =6571000
        mu = 398600.4415*(10**9)
        time = args[1]*r0*np.sqrt(r0/mu)
        print(args[1],' ',time/86400)
        print(args[4])
        return x, y

    def diffs(self, args):
        alpha = np.pi/2
        acc = self.acc
        r_ = args[0]
        time_ = args[1]
        Vr_ = args[2]
        Vphi_ = args[3]
        mass_ = args[4]
        dr_ = Vr_ * r_ / Vphi_
        dtime_ = r_ / Vphi_
        dVr_ = Vphi_ - 1 / (r_ * Vphi_)
        dVphi_ = -Vr_ + (r_ / Vphi_)*acc/(1-mass_)
        dmass_ = (acc/6.4)*(r_/Vphi_)
        res = np.array([dr_, dtime_, dVr_, dVphi_, dmass_])

        return res


















