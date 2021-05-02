import math
import numpy as np  
import matplotlib.pyplot as plt 

from mpl_toolkits import mplot3d

fog = plt.figure()
ax = plt.axes(projection = '3d')
r = int(input())
h = int(input())

x = []
y = []
z = []

for i in range(h):
    for a in range(0, 360, 3):
        aR = math.radians(a)
        x.append(r*math.sin(aR))
        y.append(r*math.cos(aR))
        z.append(i)

ax.scatter3D(x, y, z)
plt.show()