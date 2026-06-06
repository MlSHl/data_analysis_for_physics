import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("elipsi_gamocda.xlsx", header=None)

x = df.iloc[0, :].dropna().to_numpy(dtype=float)
y = df.iloc[1, :].dropna().to_numpy(dtype=float)

A = np.column_stack([2*x*y,y**2,2*x,2*y,np.ones_like(x)])
rhs = -x**2

a12, a22, a13, a23, a33 = np.linalg.lstsq(A, rhs, rcond=None)[0]
a11 = 1

D = np.linalg.det([
    [a11, a12],
    [a12, a22]
])

x0 = -(a13*a22 - a12*a23) / D
y0 = -(a11*a23 - a12*a13) / D

print("Center:")
print("x0 =", x0)
print("y0 =", y0)

xl = np.linspace(0, 20, 1000)
yl = np.linspace(0, 20, 1000)
f = xl**2 + 2*a12*xl*yl + a22*yl**2 + 2*a13*xl + 2*a23*yl + a33

print("Coefficients:")
print("a11 =", 1)
print("a12 =", a12)
print("a22 =", a22)
print("a13 =", a13)
print("a23 =", a23)
print("a33 =", a33)

print()
print("Residual max:", np.max(np.abs(f)))

x_min, x_max = x.min() - 1, x.max() + 1
y_min, y_max = y.min() - 1, y.max() + 1

# Finding a and b
a11 = 1.0

Q = np.array([
    [a11, a12],
    [a12, a22]
])

D = np.linalg.det(Q)

A_det = np.linalg.det([
    [a11, a12, a13],
    [a12, a22, a23],
    [a13, a23, a33]
])

# Center
x0 = -(a13*a22 - a12*a23) / D
y0 = -(a11*a23 - a12*a13) / D
center = np.array([x0, y0])

# Axes and rotation
eigvals, eigvecs = np.linalg.eigh(Q)

c = A_det / D
radii_squared = -c / eigvals
radii = np.sqrt(radii_squared)

a = np.max(radii)
b = np.min(radii)

print("Center:", x0, y0)
print("semi-major axis a =", a)
print("semi-minor axis b =", b)

# Parametrize ellipse
theta = np.linspace(0, 2*np.pi, 1000)

ellipse_local = np.vstack([
    radii[0] * np.cos(theta),
    radii[1] * np.sin(theta)
])

ellipse_global = eigvecs @ ellipse_local + center.reshape(2, 1)

ellipse_x = ellipse_global[0, :]
ellipse_y = ellipse_global[1, :]

plt.scatter(x, y, label="Data points")
plt.plot(ellipse_x, ellipse_y, label="Fitted ellipse")
plt.scatter([x0], [y0], label="Center")
plt.grid(True)
plt.legend()
plt.show()

def dist(x, y):
    px = 47
    py = 58
    return np.sqrt((x - px)**2 + (y - py)**2)

min_dist = 999999
closest_x = None
closest_y = None

for i, j in zip(ellipse_x, ellipse_y):
    d = dist(i, j)

    if min_dist > d:
        min_dist = d
        closest_x = i
        closest_y = j

print("Distance:", min_dist)
print("Closest point:", closest_x, closest_y)


#I = a11 + a22
#D = np.array([[a11, a12], 
#              [a12, a22]])
#A = np.array([[a11, a13, a13], 
#              [a12, a22, a23], 
#              [a13, a23, a33]])
#
#DD = np.linalg.det(D)
