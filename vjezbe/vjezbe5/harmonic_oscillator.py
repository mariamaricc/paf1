import matplotlib.pyplot as plt
class HarmonicOscillator():
    def __init__(self,x0,dt,m,k,total_time) -> None:
        self.x = [x0]
        self.v = [0]
        self.a = [-k/m * x0]
        self.t = [0]
        self.m = m
        self.k = k
        self.total_time = total_time
        self.dt = dt

    def __move(self):
        self.a.append((-self.k/self.m)*self.x[-1])
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.x.append(self.x[-1] + self.v[-1]*self.dt)
        self.t.append(self.t[-1] + self.dt)

    def oscillate(self):
        while self.t[-1] <= self.total_time:
            self.__move()

    def plot(self):
        plt.subplot(1,3,1)
        plt.title("x-t graf")
        plt.plot(self.t,self.x)

        plt.subplot(1,3,2)
        plt.title("v-t graf")
        plt.plot(self.v,self.t)

        plt.subplot(1,3,3)
        plt.title("a-t graf")
        plt.plot(self.t,self.a)

        plt.show()