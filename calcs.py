import numpy as np

class calcs_class():
    def __init__(self, radius, speedAng, speedrad, k_radius, k_speedAng ,k_speedrad):
        self.vars = np.zeros(5)
        self.vars[0] = radius
        self.vars[3] = speedAng
        self.vars[2] = speedrad
        self.rk = k_radius
        self.vars[4] = 0
        self.vphik = k_speedAng
        self.vrk = k_speedrad
        self.x = list()
        self.y = list()
    def rungekutta4(self):
        angle = 0
        k = np.zeros((5, 4))
        h = np.pi/180
        while self.vars[0] < self.rk:
            self.x.append(self.vars[0] * np.cos(angle))
            self.y.append(self.vars[0] * np.sin(angle))



            k[:, 0] = self.diffs(self.vars)
            k[:, 1] = self.diffs(self.vars + k[:, 0] / 2) * 2
            k[:, 2] = self.diffs(self.vars + k[:, 1] / 2) * 2
            k[:, 3] = self.diffs(self.vars + k[:, 2])

            k *= h / 6

            dvars = [sum(elem) for elem in k]

            self.vars += dvars

            angle += h

        return self.x, self.y

    def diffs(self, args):
        alpha = np.pi/2
        acc = 0.01
        r_ = args[0]
        time_ = args[1]
        Vr_ = args[2]
        Vphi_ = args[3]
        mass_ = args[4]
        dr_ = Vr_ * r_ / Vphi_
        dtime_ = r_ / Vphi_
        dVr_ = Vphi_ - 1 / (r_ * Vphi_) + np.cos(alpha) * acc * r_ / Vphi_
        dVphi_ = -Vr_ + np.sin(alpha) * acc * r_ / Vphi_
        res = np.array([dr_, dtime_, dVr_, dVphi_, mass_])

        return res


















