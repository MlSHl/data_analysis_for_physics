import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

df = pd.read_csv('grova2.csv', header=None)

x = df[0]
y = df[1]
v_x = df[2]
v_y = df[3]
v_z = df[4]

v = np.sqrt(v_x**2 + v_y**2 + v_z**2)

f = df[(x > 15) & (x < 45) & (y > 25) & (y < 55) & (v_x>2.5) & (v_y>2) & (v_z>2)]


fig, ax = plt.subplots()
xm =np.mean(f[0])
ym =np.mean(f[1])

vxm =np.mean(f[2])
vym =np.mean(f[3])

density = []
radii = []

r_init = 4
k = 2
r0 = 0
r1 = 0
while r1 < 15.2:
    r0 = r_init*((k-1)**(1/2))
    r1 = r_init*((k)**(1/2))
    print(np.pi*(r1**2-r0**2))
    circle = Circle((float(xm), float(ym)), r1, color='blue', fill=False, linewidth=2)
    n=len(f[(((f[0]-xm)**2 + (f[1]-ym)**2) <= r1**2) & (((f[0]-xm)**2 + (f[1]-ym)**2) >= r0**2)])
    density.append(n/(np.pi*r_init**2))
    radii.append(r0)
    k+=1
    ax.add_patch(circle)


dx = f[0] - xm
dy = f[1] - ym

dvx = f[2] - vxm
dvy = f[3] - vym

r = np.sqrt(dx**2 + dy**2)

v_tan = (dx * dvy - dy * dvx) / r

print("Mean tangential velocity:", v_tan.mean())

#plt.hist(v_y, bins=int(np.sqrt(len(v_x))))
plt.quiver(f[ 0],f[ 1],f[ 2],f[ 3],f[ 4],cmap='Purples')
plt.scatter(xm, ym)
plt.show()

plt.scatter(radii, density)
plt.show()


speed = np.sqrt(f[2]**2 + f[3]**2 + f[4]**2)

plt.hist(speed, bins=30)
plt.xlabel("Speed")
plt.ylabel("Count")
plt.show()
