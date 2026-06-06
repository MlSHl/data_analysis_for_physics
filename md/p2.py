import numpy as np
import matplotlib.pyplot as plt

N = 100

A_true = 2
B_true = 1.5

x = np.linspace(1, 10, N)
y = A_true * x**B_true

noise = np.random.normal(0, 2, N)
yn = y + noise

# Same reason as before, log can't be <= 0
mask = (x > 0) & (yn > 0)

x_fit = x[mask]
yn_fit = yn[mask]

t = np.log(x_fit)
z = np.log(yn_fit)

def det(M):
    return np.linalg.det(M)

M = np.array([
    [np.sum(t**2), np.sum(t)],
    [np.sum(t), len(t)]
])

C1 = np.array([
    [np.sum(t*z), np.sum(z)],
    M[1]
])

C2 = np.array([
    M[0],
    [np.sum(t*z), np.sum(z)]
])

D = det(M)
D1 = det(C1)
D2 = det(C2)

B = D1 / D
lnA = D2 / D

A = np.exp(lnA)

print(f"A: {A}")
print(f"B: {B}")

y_hat = A * x_fit**B

SSE = np.sum((yn_fit - y_hat)**2)
SST = np.sum((yn_fit - np.mean(yn_fit))**2)

r_square = 1 - SSE/SST

print(f"r^2: {r_square}")

x_line = np.linspace(min(x_fit), max(x_fit), 300)
y_line = A * x_line**B

plt.scatter(x_fit, yn_fit, label="data")
plt.plot(x_line, y_line, label="fit")

plt.title("Power Model")

formula = f"y = {A_true}x^{B_true}\n$r^2$ = {r_square:.4f}"

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
