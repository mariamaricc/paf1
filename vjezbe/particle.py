import matplotlib.pyplot as plt
from cmath import cos, sin
import math


class Particle:
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.dt = 0.01

    def set_initial_conditions(self,v0,theta,x0,y0):
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0 * sin(math.radians(theta)))
        self.vy.append(v0 * cos(math.radians(theta)))
        self.ay.append(-9.81)
    
    def reset(self):
        self.__init__()

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.vx[-1] * self.dt)
        self.y.append(self.y[-1] + self.vy[-1] * self.dt)
        self.vx.append(self.vx[-1] + self.ax * self.dt)
        self.vy.append(self.vy[-1] + self.ay * self.dt)

    def range(self):
        while (self.y[-1] >= 0):
            self.__move()
        return self.x[-1]

    def plot_trajectory(self):
        plt.show()
