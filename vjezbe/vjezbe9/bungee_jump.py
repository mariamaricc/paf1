import numpy as np
import matplotlib.pyplot as plt

class BungeeJump:
    def __init__(self, m, k, Cd, A, rho, l0, h0):
        self.v = [0.]
        self.y = [h0]
        self.a = [-9.81]
        self.t = [0.]
        self.dt = 0.01
        self.g = -9.81
        self.m = m
        self.k = k
        self.Cd = Cd
        self.A = A
        self.rho = rho
        self.l0 = l0
        self.h0 = h0
        self.E_k = [0.]
        self.E_p = [h0 * m * 9.81]
        self.E_el = [0.]
        self.E_uk = []
        
    def __a_F_el(self, v, y):
        return self.g - np.sign(v)*(self.rho * self.Cd * self.A) / (2*self.m) * v**2 + self.k/self.m * (self.h0 - self.y[-1] - self.l0)

    def __a(self, v, y):
        return self.g - np.sign(v)*(self.rho * self.Cd * self.A) / (2*self.m) * v**2

    def __move(self, a):
        self.a.append(a(self.v[-1], self.y[-1]))
        self.v.append(self.v[-1] + self.a[-1] * self.dt)
        self.y.append(self.y[-1] + self.v[-1] * self.dt)
        self.t.append(self.t[-1] + self.dt)
        self.E_k.append(self.__kinetic(self.m, self.v[-1]))
        self.E_p.append(self.__potential(self.m, self.y[-1]))

    def __kinetic(self, m, v):
        return 0.5*m*v**2

    def __potential(self, m, h):
        return m*9.81*h

    def __elastic(self, k, x):
        return 0.5*k*x**22

    def plot_trajectory(self):
        while self.t[-1] < 50:
            if self.y[-1] > self.h0 - self.l0:
                self.__move(self.__a)
                self.E_el.append(0)
            else:
                self.__move(self.__a_F_el)
                self.E_el.append(self.__elastic(self.k, self.h0 - self.y[-1] - self.l0))
        plt.plot(self.t, self.y)
        plt.show()

        for i in range(len(self.E_el)):
            self.E_uk.append(self.E_k[i] + self.E_el[i] + self.E_p[i])

        plt.plot(self.t, self.E_k)
        plt.plot(self.t, self.E_p)
        plt.plot(self.t, self.E_el)
        plt.plot(self.t, self.E_uk)
        plt.show()