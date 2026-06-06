import numpy as np
import matplotlib.pyplot as plt

N = 100

A_true = 10
B_true = 3

x = np.linspace(0.5, 20, N)
y = A_true * x / (B_true + x)

noise = np.random.normal(0, 0.3, N)
yn = y + noise

# to avoid division by zero or negative y
mask = yn > 0
x_fit = x[mask]
yn_fit = yn[mask]

z = x_fit / yn_fit

def det(M):
    return np.linalg.det(M)

M = np.array([
    [np.sum(x_fit**2), np.sum(x_fit)],
    [np.sum(x_fit), len(x_fit)]
])

C1 = np.array([
    [np.sum(x_fit*z), np.sum(z)],
    M[1]
])

C2 = np.array([
    M[0],
    [np.sum(x_fit*z), np.sum(z)]
])

D = det(M)
D1 = det(C1)
D2 = det(C2)

m = D1 / D
n = D2 / D

A = 1 / m
B = n / m

print(f"A: {A}")
print(f"B: {B}")

y_hat = A * x_fit / (B + x_fit)

SSE = np.sum((yn_fit - y_hat)**2)
SST = np.sum((yn_fit - np.mean(yn_fit))**2)

r_square = 1 - SSE/SST

print(f"r^2: {r_square}")

x_line = np.linspace(min(x_fit), max(x_fit), 300)
y_line = A * x_line / (B + x_line)


plt.scatter(x_fit, yn_fit, label="data")
plt.plot(x_line, y_line, label="fit")

plt.title("Saturation Model")

formula = f"y = {A_true}x / ({B_true} + x)\n$r^2$ = {r_square:.4f}"

plt.text(
    0.05, 0.95,
    formula,
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment="top"
)

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
