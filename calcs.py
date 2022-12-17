import numpy as np

class calcs_class():
    def __init__(self, acc):
        self.vars = np.zeros(10)
        self.vars[0] = 1 #r
        self.vars[1] = 0 #phi
        self.vars[2] = np.sqrt(1/self.vars[0])+1 #Vphi
        self.vars[3] = 0 #Vr
        self.vars[4] = 0 #m

        self.vars[5] = -0.01  # Pr
        self.vars[7] = -0.01  # pVr
        self.vars[8] = -0.01  # pVphi

        self.vars[6] = 0  # Pphi
        self.vars[9] = -1  # Pm



        self.r_k = 42164/(6371+200)
        self.acc = acc

        self.err = 0
    def fit(self):
        a = 0.1
        b = 0.4
        h = 0.00001
        print('fit')
        for i in range(100):
            print(self.rungekutta4(a, b))
            da = (self.rungekutta4(a+h, b)-self.rungekutta4(a-h, b))/2*h
            db = (self.rungekutta4(a, b+h)-self.rungekutta4(a, b-h))/2*h

            a = a - 10*da
            b = b - 10*db


            print('iter: #',i+1, 'err', self.err)









    def rungekutta4(self, foo, fee):

        args = np.array([elem for elem in self.vars])

        r = list()
        angle = list()
        t_list = list()
        vr_list = list()
        #print(pr, pf)
        time = 0
        k = np.zeros((10, 4))


        #7099.125838682138
        while args[0] < self.r_k:


            if time > 8000:
                break
            h = 0.1/args[2]
            t_list.append(time)
            vr_list.append(args[3])
            r.append(args[0])
            angle.append(args[1])

            k[:, 0] = self.diffs(args)
            k[:, 1] = self.diffs(args + k[:, 0] / 2) * 2
            k[:, 2] = self.diffs(args + k[:, 1] / 2) * 2
            k[:, 3] = self.diffs(args + k[:, 2])


            k *= h/6

            dvars = np.array([sum(elem) for elem in k])

            args += dvars

            time += h




        print(time)
        err = np.sin(args[1])**2+args[2]
        self.err = err
        return angle, r, t_list, vr_list

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

        #print(flag)

        acc = 0*self.acc#*(flag > -1)




        dr = vr
        dp = vp/r
        dVp = -(vr*vp)/r+0
        dVr = (vp*vp)/r - 1/(r*r)
        dm = acc/6.8

        dPm = -acc*pvp/(1-m)**2
        dPvp = (pvp*vr-2*pvr*vp-pp)/r
        dPvr = pvp*vp/r-pr
        dPr = pp*vp/(r*r)-pvp*vr*vp/(r*r)-pvp*(2/(r*r*r)-vp*vp/(r*r))





        res = np.array([dr,dp,dVp,dVr,dm,dPr,0,dPvr,dPvp,dPm])

        return res


















