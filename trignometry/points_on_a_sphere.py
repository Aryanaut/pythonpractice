from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib
import math

fog = plt.figure()
ax = plt.axes(projection='3d')
r = 10
x = []
y = []
z = []

for i in range(0, 180, 5):
    iR = math.radians(i)
    for a in range(0, 360, 5):
        aR = math.radians(a)
        x.append(r*math.sin(iR)*math.cos(aR))
        y.append(r*math.sin(iR)*math.sin(aR))
        z.append(r*math.cos(iR))

ax.scatter3D(x, y, z)
plt.show()