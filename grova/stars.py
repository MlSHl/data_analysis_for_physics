import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('grova1.csv', header=None)

x = df[0]
y = df[1]
v_x = df[2]
v_y = df[3]
v_z = df[4]

plt.quiver(x, y, v_x, v_y, v_z, cmap='Blues')


stars = np.column_stack([x, y, v_x, v_y, v_z])

center_x = 30
center_y = 40
radius = 20

dx = stars[:, 0] - center_x
dy = stars[:, 1] - center_y

distance = dx**2 + dy**2

f_stars = stars[distance <= radius**2]

mean_v = np.mean(f_stars[:, 2:5], axis=0)

means = []
for i in f_stars:
    dot = np.dot(i[2:5], mean_v)
    means.append([i[0], i[1], dot])
    print(dot)

means = np.array(means)

#x_vals = means[:, 0]
#y_vals = means[:, 1]
#z_vals = means[:, 2]

#fig = plt.figure()

#plt.quiver(x_vals, y_vals, v_x, v_y, v_z, cmap='Blues')

plt.show()


#q = plt.quiver(
#    f_stars[:, 0],
#   f_stars[:, 1],
#  f_stars[:, 2],
# f_stars[:, 3],
#  f_stars[:, 4],
#  cmap='Purples'
#)#
#plt.show()

