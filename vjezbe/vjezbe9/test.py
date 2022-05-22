import bungee_jump
import numpy as np
import matplotlib.pyplot as plt

jump1 = bungee_jump.BungeeJump(70, 100, 0.5 , 1, 1.5, 30, 100)
jump1.plot_trajectory()
jump2 = bungee_jump.BungeeJump(70, 100, 0. , 1, 1.5, 30, 100)
jump2.plot_trajectory()