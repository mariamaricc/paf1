import math
from decimal import Decimal
from textwrap import fill
import matplotlib.pyplot as plt
import numpy as np
ax = plt.subplot()

def kruznica():
    p = float(input("unesite x koordinatu sredista: "))
    q = float(input("unesite y koordinatu sredista: "))
    r = float(input("radijus kruznice: "))
    x = float(input("x koordinata točke: "))
    y = float(input("y koordinata točke: "))

    r1 = round(math.sqrt((x-p)**2+(y-q)**2),2)
    print(r1)

    if r == r1:
        print("tocka lezi na kruznici")
    elif r < r1:
        d = r1 - r
        print("tocka lezi unutar kruznice i udaljena je od nje za {}".format(d))
    else:
        d = r - r1
        print("tocka lezi izvan kruznice i udaljena je od nje za {}".format)
        
    krug = plt.Circle((p,q),r, fill=False)
    ax.scatter(x, y, s=r)
    ax.add_patch(krug)
    plt.axis('square')
    pohrana = input("1. prikaz slike na ekranu ili 2. spremanje kao pdf? ")
    if pohrana == "1":
        plt.show()
    else:
        spremanje = input("pod kojim imenom zelite spremiti file? ")
        plt.savefig("{}.pdf".format(spremanje))
   
kruznica()
