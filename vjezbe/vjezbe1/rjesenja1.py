import matplotlib.pyplot as plt
import numpy as np

def pravac():
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    k = (y2 - y1) / (x2 - x1)
    l = y1 - k*x1
    print("y = {}x + {}".format(k,l))

    t = np.arange(0.0, 10.0, 0.1)
    s = k*(x2-x1)*t + l

    fig, ax = plt.subplots()
    ax.plot(t, s)
    
    ax.set(xlabel='x', ylabel='y',
       title='Pravac')
    ax.grid()

    prikaz = input("1.prikazi na ekranu ili 2. spremi kao pdf: ")
    if prikaz == "1":
        plt.show()
    elif prikaz == "2":
        spremanje = input("pod kojim imenom zelite spremiti file? ")
        fig.savefig("{}.pdf".format(spremanje))
pravac()