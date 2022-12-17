import numpy as np

class calcs_class():
    def __init__(self, acc, radius):
        self.vars = np.zeros(6)
        self.vars[0] = radius
        self.vars[1] = 0
        self.vars[2] = 0
        self.vars[3] = 0
        self.vars[4] = 0
        self.vars[5] = 0
        self.acc = acc

    def fit(self):
        pass


    def rungekutta4(self):

        args = np.array([elem for elem in self.vars])
        print(self.vars)
        x = list()
        y = list()
        time = 0
        k = np.zeros((6, 4))

        r_k = 42164 / (6371 + 200)
        while args[0] < r_k:

            h = 0.1 * args[0]

            y.append(args[0])
            x.append(args[1])

            k[:, 0] = self.diffs(args)
            k[:, 1] = self.diffs(args + k[:, 0] / 2) * 2
            k[:, 2] = self.diffs(args + k[:, 1] / 2) * 2
            k[:, 3] = self.diffs(args + k[:, 2])

            k *= h / 6

            dvars = [sum(elem) for elem in k]

            args += dvars

            time += h

        r0 =6571000
        mu = 398600.4415*(10**9)
        time = args[1]*r0*np.sqrt(r0/mu)
        print(time)
        return x, y

    def diffs(self, args):
        acc = self.acc

        r_ = args[0]
        phi_ = args[1]
        m_ = args[2]

        pf_ = args[3]
        pr_ = args[4]
        pm_ = args[5]

        dr_ = 2*pow(r_,1.5)*acc/(1-m_)
        dphi_ = 1/pow(r_,1.5)
        dmass_ = acc/6.4

        dpf_ = 0
        dpr_ = 1.5*pf_/pow(r_, 2.5)-3*acc*pr_*np.sqrt(r_)/(1-m_)
        dpm_ = -2*acc*pr_*pow(r_, 1.5)/(1-m_)**2

        res = np.array([dr_, dphi_, dmass_, dpf_, dpr_, dpm_])

        return res


















