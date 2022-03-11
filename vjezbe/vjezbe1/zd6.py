import math
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np


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
        print("tocka lezi unutar kruznice i udaljena je od nje za {}".format())
    else:
        print("tocka lezi izvan kruznice")
   
kruznica()