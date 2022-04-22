from re import X
import matplotlib.pyplot as plt

class ProjectileDrop:
    def __init__(self):
        self.h = []
        self.vx = []
        self.a = []
        self.t = []
        self.x = []
        self.y = []
        self.dt = 0.01
    def set_initial_conditions(self,h,vx):
        self.h.append(h)
        self.vx.append(vx)
        print("Uspješno stvoren objekt. h = {}, vx = {}".format(h,vx))
    def change_height(self,h):
        self.h = []
        self.h.append(h)
    def change_vx(self,vx,dvx):
        self.vx = vx + dvx
    def __move(self):
        self.h.append(self.h[-1] - self.vx[-1] * self.dt)
        self.a.append(9.81)
        self.vx.append(self.v[-1] + self.a[-1] * self.dt)
        self.x.append(self.x[-1] + self.vx[-1] * self.dt)
        self.t.append(self.t[-1] + self.dt)
    def drop(self):
        while self.h > 0:
            self.__move()
            if self.h == 0:
                return(self.x, self.h)
    def plot(self):
        plt.plot(self.x,self.h)
        plt.show()
    
