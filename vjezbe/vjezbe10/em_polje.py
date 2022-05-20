import matplotlib.pyplot as plt
import numpy as np

class ChargedParticle():
    def __init__(self, q, m, B_z, vx, vy, vz, Ex, Ey, Ez, dt) -> None:
        self.E = np.array((Ex, Ey, Ez))
        self.B = np.array((0,0,B_z))
        self.v = np.array((vx,vy,vz))
        self.a = np.array((0,0,0))
        self.x = [0.]
        self.y = [0.]
        self.z = [0.]
        self.t = [0.]
        self.m = m
        self.q = q
        self.dt = dt

    def __move(self):
        self.a =  (self.q * self.E + self.q * (np.cross(self.v,self.B)))/self.m
        self.v += self.a * self.dt
        self.x.append(self.x[-1] + self.v[0]*self.dt)
        self.y.append(self.y[-1] + self.v[1]*self.dt)
        self.z.append(self.z[-1] + self.v[2]*self.dt)
        self.t.append(self.t[-1] + self.dt)

    def evolve(self, t):
        while self.t[-1] <= t:
            self.__move()