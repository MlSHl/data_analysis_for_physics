import numpy as np
import matplotlib.pyplot as plt

N = 100
a = 3
b = 4

x = np.linspace(0, 10, 100)
y = a*x + b

noise = np.random.normal(0, 0.3, N)

yn = y + noise

def det(A):
    return np.linalg.det(A)

A = np.array([[np.sum(x**2), np.sum(x)], [np.sum(x), N]])

C1 = np.array([[np.sum(x*yn), np.sum(yn)], A[1]])
C2 = np.array([A[0], [np.sum(x*yn), np.sum(yn)]])

D = det(A)
D1 = det(C1)
D2 = det(C2)

m = D1/D
n = D2/D

print(f"m: {m}")
print(f"n: {n}")

plt.plot(x, yn)
plt.plot(x, m*x+n)
plt.show()

