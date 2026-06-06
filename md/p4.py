import numpy as np
import matplotlib.pyplot as plt

N = 100

A_true = 2
B_true = 3
C_true = 0.5
D_true = -2

x = np.random.uniform(0, 10, N)
y = np.random.uniform(5, 15, N)

z = A_true + B_true*x + C_true*x**2 + D_true*y

noise = np.random.normal(0, 1, N)
zn = z + noise

def det(M):
    return np.linalg.det(M)

S1 = N
Sx = np.sum(x)
Sx2 = np.sum(x**2)
Sx3 = np.sum(x**3)
Sx4 = np.sum(x**4)

Sy = np.sum(y)
Sy2 = np.sum(y**2)

Sxy = np.sum(x*y)
Sx2y = np.sum((x**2)*y)

Sz = np.sum(zn)
Sxz = np.sum(x*zn)
Sx2z = np.sum((x**2)*zn)
Syz = np.sum(y*zn)

M = np.array([
    [S1,   Sx,   Sx2,   Sy],
    [Sx,   Sx2,  Sx3,   Sxy],
    [Sx2,  Sx3,  Sx4,   Sx2y],
    [Sy,   Sxy,  Sx2y,  Sy2]
])

R = np.array([
    Sz,
    Sxz,
    Sx2z,
    Syz
])

D_main = det(M)

# Cramer part
MA = M.copy()
MA[:, 0] = R

MB = M.copy()
MB[:, 1] = R

MC = M.copy()
MC[:, 2] = R

MD = M.copy()
MD[:, 3] = R

A = det(MA) / D_main
B = det(MB) / D_main
C = det(MC) / D_main
D = det(MD) / D_main

print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

z_hat = A + B*x + C*x**2 + D*y

SSE = np.sum((zn - z_hat)**2)
SST = np.sum((zn - np.mean(zn))**2)

r_square = 1 - SSE / SST

print(f"r^2: {r_square}")

x_grid = np.linspace(np.min(x), np.max(x), 50)
y_grid = np.linspace(np.min(y), np.max(y), 50)

Xg, Yg = np.meshgrid(x_grid, y_grid)

Zg = A + B*Xg + C*Xg**2 + D*Yg

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x, y, zn, label="data")
ax.plot_surface(Xg, Yg, Zg, alpha=0.5)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Quadratic Multiple Regression Model")

formula = f"z = {A_true} + {B_true}x + {C_true}x² + {D_true}y\n$r^2$ = {r_square:.4f}"

ax.text2D(
    0.05, 0.95,
    formula,
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top"
)

ax.legend()
plt.show()
