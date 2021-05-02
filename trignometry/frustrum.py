from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math
import numpy as np

fog = plt.figure()
ax = plt.axes(projection = '3d')
x = []
y = []
z = []

r1 = int(input())
r2 = int(input())

for r in range(r1, r2):
    for a in range(0, 360, 3):
        aR = math.radians(a)
        x.append(r*math.sin(aR))
        y.append(r*math.cos(aR))
        z.append(r)

ax.scatter3D(x, y, z)
plt.show()