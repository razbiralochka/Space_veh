import numpy as np
from scipy.optimize import minimize
class calcs_class():
    def __init__(self, acc):
        self.r_k = 42164 / (6371 + 200)
        self.acc = acc


        self.mu = 398600.4415 * (10 ** 9)

        self.vars = np.zeros(9)
        self.vars[0] = 1 #r
        self.vars[3] = 1 #Vphi





        self.vars[8] = -1 # Pm




        self.err = 0
    def fit(self):
        a = 2.623581714078705
        b = 12.108649205761758
        c = 16.843360413636947
        h = 1
        g = 200
        print('fit')
        min_err = 30
        for i in range(100):

            res = self.rungekutta4(a, b, c)

            da = (self.rungekutta4(a + h, b, c) - res) / (h)
            print('da: ',da)
            db = (self.rungekutta4(a, b + h, c) - res) / (h)
            print('db: ', db)
            dc = (self.rungekutta4(a, b, c + h) - res) / (h)
            print('dc: ', dc)





            a = a - g * da
            b = b - g * db
            c = c - g * dc

            err = self.rungekutta4(a, b, c)


            print('iter: #', i + 1, 'err', err)
            print('Pr: ', a, '   Pvr: ', b, '   Pv_phi: ', c)



    def rungekutta4(self, a, b, c):

        args = np.array([elem for elem in self.vars])
        args[5] = a
        args[6] = b
        args[7] = c


        time = 0
        k = np.zeros((9, 4))



        #7099.125838682138
        while time < 10000:



            h = 2*np.pi/100


            k[:, 0] = self.diffs(args)
            k[:, 1] = self.diffs(args + k[:, 0] * h / 2) * 2
            k[:, 2] = self.diffs(args + k[:, 1] * h / 2) * 2
            k[:, 3] = self.diffs(args + k[:, 2] * h)



            k *= h / 6

            dvars = np.array([sum(elem) for elem in k])

            args += dvars

            time += h



        err = args[4]+(self.r_k-args[0])**2
        self.err = err


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


        flag = pm_/6.8 + pvp_/(1-m_)

        acc = self.acc*(flag > 0)

        dr = vr_
        dp = vp_/r_
        dVr = vp_**2 / r_ - 1 / r_**2
        dVp = -(vr_*vp_)/r_+acc/(1-m_)
        dm = acc/6.8

        dPm = -acc*pvp_/(1-m_)**2
        dPvp = -(2*pvr_*vp_)/r_ + (pvp_*vr_)/r_
        dPvr = pvp_*vp_/r_-pr_
        dPr = -(pvp_*vr_*vp_)/pow(r_,2)-pvr_*(2/pow(r_,3)-pow(vp_,2)/pow(r_,2))









        res = np.array([dr, dp, dVr, dVp, dm, dPr, dPvr,dPvp,dPm])

        return res