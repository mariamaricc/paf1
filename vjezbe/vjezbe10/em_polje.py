import matplotlib.pyplot as plt
import numpy as np

def gibanje(q, m, B_z, vx, vy, vz, Ex, Ey, Ez):
    E = np.array((Ex, Ey, Ez))
    B = np.array((0,0,B_z))
    v = np.array((vx,vy,vz))
    F = q * E + q * (np.cross(v,B))
    
