import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator():
    def __init__(self,x0,dt,m,F,v0,t0,total_time) -> None:
        self.x = [x0]
        self.v = [v0]
        self.a = [F(x0,t0,v0)/m]
        self.F = F
        self.t = [t0]
        self.m = m
        self.total_time = total_time
        self.dt = dt

    def __move(self):
        self.x.append(self.x[-1] + self.v[-1]*self.dt)
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.a.append(self.F(self.v[-1],self.x[-1],self.t[-1])/self.m)
        self.t.append(self.t[-1] + self.dt)

    def oscillate(self):
        while self.t[-1] <= self.total_time:
            self.__move()

    def plot(self):
        plt.plot(self.t, self.x)
        plt.show()