import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self):
        self.x = []
        self.y = []
        self.t = [0.]
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.g = -9.81

    def set_initial_conditions(self, v0, theta, x0, y0, rho, mi, m, A = 0.25, dt = 0.01):
        self.v0 = v0
        self.theta = theta
        self.x0 = x0
        self.y0 = y0
        self.rho = rho
        self.mi = mi
        self.A = A
        self.dt = dt
        self.m = m
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0 * np.cos(theta))
        self.vy.append(v0 * np.sin(theta))


    def shape(self, shape, r, a):
        if shape == "kocka":
            self.A = a**2
        else:
            self.A = r**2 * np.pi

    def reset(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0.]

    def __move(self):
        self.ay.append(self.g - np.sign(self.vy[-1])*(self.rho * self.mi * self.A) / (2*self.m) * self.vy[-1]**2)
        self.ax.append(- np.sign(self.vx[-1])*(self.rho * self.mi * self.A) / (2*self.m) * self.vx[-1]**2)
        self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1] * self.dt)
        self.x.append(self.x[-1] + self.vx[0]*self.dt)
        self.t.append(self.t[-1] + self.dt)
    
    def ay_Runge_Kutta(self, v = 0, x = 0, t = 0):
        return self.g - np.sign(v)*(self.rho * self.mi * self.A) / (2*self.m) * v**2

    def ax_Runge_kUtta(self, v= 0, x = 0, t = 0):
        return - np.sign(v)*(self.rho * self.mi * self.A) / (2*self.m) * v**2

    def __move_rk4(self):
        k1vx = self.ax_Runge_kUtta(self.vx[-1]) * self.dt
        k1x = self.vx[-1] * self.dt

        k2vx = self.ax_Runge_kUtta(self.vx[-1] + k1vx/2) * self.dt
        k2x = (self.vx[-1] + (k1vx/2)) * self.dt

        k3vx = self.ax_Runge_kUtta(self.vx[-1] + k2vx/2) * self.dt
        k3x = (self.vx[-1] + (k2vx/2)) * self.dt

        k4vx = self.ax_Runge_kUtta(self.vx[-1] + k3vx) * self.dt
        k4x = (self.vx[-1] + k3vx) * self.dt

        k1vy = self.ay_Runge_Kutta(self.vy[-1]) * self.dt
        k1y = self.vy[-1] * self.dt
        
        k2vy = self.ay_Runge_Kutta(self.vy[-1] + k1vy/2) * self.dt
        k2y = (self.vy[-1] + (k1vy/2)) * self.dt

        k3vy = self.ay_Runge_Kutta(self.vy[-1] + k2vy/2) * self.dt
        k3y = (self.vy[-1] + (k2vy/2)) * self.dt
        
        k4vy = self.ay_Runge_Kutta(self.vy[-1] + k3vy) * self.dt
        k4y = (self.vy[-1] + k3vy) * self.dt

        self.x.append(self.x[-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)
        self.y.append(self.y[-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)
        self.vx.append(self.vx[-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
        self.vy.append(self.vy[-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)

    def plot_runge_kutta(self):
        while self.y[-1] >= 0:
            self.__move()

    def plot(self):
        while self.y[-1] >= 0:
            self.__move()

    def domet(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.x[-1] - self.x[0]

    def angle_to_hit_target(self, p, q, r, v0, x0, y0, rho, mi, m, A):
        self.target = False
        self.theta = 0.01
        self.br = 0
        self.theta_0 = 0.01
        self.p = p
        self.q = q
        self.r = r
        while self.target == False:
            if self.theta_0 * self.br < np.pi / 2:
                self.reset()
                self.br += 1
                self.set_initial_conditions(v0, self.theta_0 * self.br, x0, y0, rho, mi, m, A) 

                while self.y[-1] >= 0:
                    self.__move()

                    for i in range(len(self.x)):
                        
                        if self.target == False:
                            if (self.x[i] - p) ** 2 + (self.y[i] - q) ** 2 < r**2:
                                self.target = True
                                print("potreban kut je", self.theta_0 * self.br)
                                break
            else:
                print("meta nije pogođena")
                self.target = True