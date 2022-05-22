import projectile
import numpy as np
import matplotlib.pyplot as plt

obj1 = projectile.Projectile()
obj1.set_initial_conditions(30, 0.5, 0, 0, 1.0, 0.5, 5)
obj1.shape("kocka", 0.25, 0.25)
obj1.plot()

obj2 = projectile.Projectile()
obj2.set_initial_conditions(30, 0.5, 0, 0, 1.0, 0.5, 5)
obj2.shape("kugla", 0.2, 0.2)
obj2.plot()

plt.plot(obj1.x, obj1.y)
plt.plot(obj2.x, obj2.y)
plt.show()