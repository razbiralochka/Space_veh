import numpy as np

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
        a = 1
        b = 1
        c = 1
        h = 0.0001
        g= 1
        print('fit')
        for i in range(1000):
            err = 100
            da = (self.rungekutta4(a + h, b, c) - self.rungekutta4(a - h, b, c)) / (2 * h)
            db = (self.rungekutta4(a, b + h, c) - self.rungekutta4(a, b - h, c)) / (2 * h)
            dc = (self.rungekutta4(a, b, c + h) - self.rungekutta4(a, b, c - h)) / (2 * h)




            a = a - g * da
            b = b - g * db
            c = c - g * dc

            if self.err < err:
                err = self.err

            if self.err > err:
                h*=0.99
                g*=0.5

            print('iter: #',i+1, 'err', self.err)
            print('Pr: ',a ,'   Pvr: ',b,'   Pv_phi: ',c)








    def rungekutta4(self, a, b,c):

        args = np.array([elem for elem in self.vars])
        args[5] = a
        args[6] = b
        args[7] = c
        r = list()
        angle = list()
        t_list = list()
        vr_list = list()

        time = 0
        k = np.zeros((9, 4))



        #7099.125838682138
        while time < 8000:



            h = 2*np.pi/100
            t_list.append(time)
            vr_list.append(args[3])
            r.append(args[0])
            angle.append(args[1])

            k[:, 0] = self.diffs(args)
            k[:, 1] = self.diffs(args + k[:, 0] * h / 2) * 2
            k[:, 2] = self.diffs(args + k[:, 1] * h / 2) * 2
            k[:, 3] = self.diffs(args + k[:, 2] * h)



            k *= h / 6

            dvars = np.array([sum(elem) for elem in k])

            args += dvars

            time += h



        err = args[4]+(self.r_k-args[0])**2+args[3]**3+(np.sqrt(1/args[0])-args[2])**2
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