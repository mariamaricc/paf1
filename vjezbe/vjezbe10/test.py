import em_polje
import matplotlib.pyplot as plt
import numpy as np

elektron = em_polje.ChargedParticle(-1,1,1,0.1, 0.1, 0.1, 0,0,0,0.01)
elektron.evolve(30)

pozitron = em_polje.ChargedParticle(1,1,1,0.1,0.1,0.1,0,0,0,0.01)
pozitron.evolve(30)

def plot(self1,self2):
    ax = plt.axes(projection='3d')
    ax.plot3D(self1.x, self1.y, self1.z, 'black',self2.x, self2.y, self2.z, 'grey')
    plt.show()
plot(elektron, pozitron)