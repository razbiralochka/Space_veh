import numpy as np

class calcs_class():
    def __init__(self, acc):
        self.r_k = 42164 / (6371 + 200)
        self.acc = acc


        self.mu = 398600.4415 * (10 ** 9)

        self.vars = np.zeros(10)
        self.vars[0] = 1 #r
        self.vars[1] = 0 #phi
        self.vars[2] = np.sqrt(1/self.vars[0])#Vphi
        self.vars[3] = 0 #Vr
        self.vars[4] = 0 #m



        self.vars[6] = 0  # Pphi
        self.vars[9] = -1 # Pm




        self.err = 0
    def fit(self):
        a = -1
        b = 0
        c = -1
        h = 0.01
        print('fit')
        for i in range(10):

            da = (self.rungekutta4(a + h, b, c) - self.rungekutta4(a - h, b, c)) / (2 * h)
            db = (self.rungekutta4(a, b + h, c) - self.rungekutta4(a, b - h, c)) / (2 * h)
            dc = (self.rungekutta4(a, b, c + h) - self.rungekutta4(a, b, c - h)) / (2 * h)




            a = a - 0.01 * da
            b = b - 0.01 * db
            c = c - 0.01 * dc

            print('iter: #',i+1, 'err', self.err)
            print('Pr: ',a,'   Pvr: ',b,'   Pv_phi: ',c)








    def rungekutta4(self, a, b,c):

        args = np.array([elem for elem in self.vars])
        args[5] = a
        args[7] = b
        args[8] = c
        r = list()
        angle = list()
        t_list = list()
        vr_list = list()

        time = 0
        k = np.zeros((10,4))



        #7099.125838682138
        while time < 10000:


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
        r = args[0]
        p = args[1]
        vp = args[2]
        vr = args[3]
        m = args[4]
        pr = args[5]
        pp = args[6]*0
        pvr = args[7]
        pvp = args[8]
        pm = args[9]


        flag = pm/6.8 + pvp/(1-m)




        acc = self.acc*(flag > 0)





        dr = vr
        dp = vp/r
        dVr = vp**2 / r - 1 / r**2
        dVp = -(vr*vp)/r+acc
        dm = acc/6.8

        dPm = -acc*pvp/(1-m)**2
        dPvp = (pvp*vr-2*pvr*vp-pp)/r
        dPvr = pvp*vp/r-pr
        dPr = pp*vp/(r*r)-pvp*vr*vp/(r*r)-pvp*(2/(r*r*r)-vp*vp/(r*r))
        dpp = 0




        res = np.array([dr, dp, dVp, dVr, dm, dPr, dpp, dPvr, dPvp, dPm])

        return res