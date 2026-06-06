import numpy as np
import matplotlib.pyplot as plt

N = 100

A_true = 2
B_true = 0.4

x = np.linspace(0, 10, N)
y = A_true * np.exp(B_true * x)

noise = np.random.normal(0, 2, N)
yn = y + noise

# Because logarithm can not be <= 0
mask = yn > 0
x_fit = x[mask]
yn_fit = yn[mask]

z = np.log(yn_fit)

def det(M):
    return np.linalg.det(M)

print(len(x_fit))

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

B = D1 / D
lnA = D2 / D

A = np.exp(lnA)

print(f"A: {A}")
print(f"B: {B}")

y_hat = A * np.exp(B * x_fit)

SSE = np.sum((yn_fit - y_hat)**2)
SST = np.sum((yn_fit - np.mean(yn_fit))**2)

r_square = 1 - SSE/SST

print(f"r^2: {r_square}")

x_line = np.linspace(min(x_fit), max(x_fit), 300)
y_line = A * np.exp(B * x_line)

plt.scatter(x_fit, yn_fit, label="data")
plt.plot(x_line, y_line, label="fit")

plt.title("Exponential Model")

formula = f"y = {A_true}*exp({B_true}x)\n$r^2$ = {r_square:.4f}"

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
