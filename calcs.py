import numpy as np
from scipy.optimize import minimize
class calcs_class():
    def __init__(self, acc):
        self.r_k = 6
        self.acc = acc

        print(self.r_k)
        self.mu = 398600.4415 * (10 ** 9)

        self.vars = np.zeros(9)
        self.vars[0] = 1
        self.vars[3] = 1.32

        self.foo=1
        self.fee = 0


        self.vars[8] = 1 # Pm




        self.err = 0
    def fit(self):

        a = 86.97565418402574
        b = -0.43295030927096434
        c = 79.50704645060031

        h = 1e-0
        g = 1e-0

        print('fit')
        err = 30
        for i in range(10000):

            da = (self.rungekutta4(a+h, b, c) - self.rungekutta4(a-h, b, c)) / (2*h)
            print('da: ', da)
            db = (self.rungekutta4(a, b + h , c) - self.rungekutta4(a, b- h , c)) / (2*h)
            print('db: ', db)
            dc = (self.rungekutta4(a, b, c + h) - self.rungekutta4(a, b,c - h)) / (2*h)
            print('dc: ', dc)



            a = 1.0 * a - g * da
            b = 1.0 * b - g * db
            c = 1.0 * c - g * dc


            err = self.rungekutta4(a, b, c)

            print('iter: #', i + 1, 'err', err, 'mass: ',self.mass)
            print('Pr: ', a, '   Pvr: ', b, '   Pv_phi: ', c)



    def rungekutta4(self, a, b, c):

        args = np.array([elem for elem in self.vars])
        args[8] = a
        args[6] = b
        args[7] = c

        k = np.zeros((9, 4))
        err = 100
        r = list()
        p = list()
        tl = list()
        ul = list()
        u2 = list()
        time = 0
        T = 350
        h = 0.01



        while args[8] > 0:


            r.append(args[0])
            p.append(args[1])
            tl.append(time)
            ul.append(self.foo)
            u2.append(self.fee)



            k[:, 0] = self.diffs(args)
            k[:, 1] = self.diffs(args + k[:, 0] * h / 2) * 2
            k[:, 2] = self.diffs(args + k[:, 1] * h / 2) * 2
            k[:, 3] = self.diffs(args + k[:, 2] * h)

            k *= h / 6

            dvars = np.array([sum(elem) for elem in k])

            args += dvars
            err = (self.r_k- args[0])**2  + (args[3] - 1/np.sqrt(self.r_k))**2 + args[2]**2+args[4]
            self.mass = args[4]
            time += h
            print('Pm ', args[8])






        return p,r,tl,ul,u2
        return err

    def diffs(self, args):
        r_ = args[0]
        vr_ = args[2]
        vp_ = args[3]
        m_ = args[4]
        pr_ = args[5]
        pvr_ = args[6]
        pvp_ = args[7]
        pm_ = args[8]


        sin = pvp_/np.sqrt(pvp_**2+pvr_**2)
        cos = pvr_ / np.sqrt(pvp_ ** 2 + pvr_ ** 2)

        flag = pm_ / 1.5 + (pvr_*cos)/ (1 - m_)+ (pvp_*sin)/ (1 - m_)

        acc = self.acc #* (flag > 0)


        self.foo = acc*1000

        self.fee = 180*np.arctan2(pvp_, pvr_)/np.pi-90


        dr = vr_
        dp = vp_/r_
        dVr = vp_**2 / r_ - 1 / r_**2 + cos*acc/(1-m_)
        dVp = -(vr_*vp_)/r_+sin*acc/(1-m_)
        dm = abs(acc)/1.5

        dPm = -acc*sin*pvp_/(1-m_)**2-acc*cos*pvr_/(1-m_)**2
        dPvp = -(2*pvr_*vp_)/r_ + (pvp_*vr_)/r_
        dPvr = pvp_*vp_/r_-pr_
        dPr = -(pvp_*vr_*vp_)/pow(r_,2)-pvr_*(2/pow(r_,3)-pow(vp_,2)/pow(r_,2))

        res = np.array([dr, dp, dVr, dVp, dm, dPr,dPvr,dPvp,dPm])

        return res