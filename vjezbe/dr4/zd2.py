from turtle import color
import projectile
import numpy as np
import matplotlib.pyplot as plt

obj1 = projectile.Projectile()
obj1.angle_to_hit_target(3, 3, 0.5, 10, 0, 0, 1.226, 0.5, 5, 0.25)

obj2 = projectile.Projectile()
obj2.angle_to_hit_target(3, 8, 0.5, 14, 0, 0, 1.226, 0.5, 5, 0.25)
plt.show()

target1 = plt.Circle((obj1.p, obj1.q), obj1.r, color = 'black')
target2 = plt.Circle((obj2.p, obj2.q), obj2.r, color = 'blue')
fig, axs = plt.subplots()
axs.set_aspect("equal")
axs.add_patch(target1)
axs.add_patch(target2)
axs.plot(obj1.x, obj1.y)
axs.plot(obj2.x, obj2.y)
plt.show()