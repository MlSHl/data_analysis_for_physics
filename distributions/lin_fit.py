from numpy import random as rand
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp

# make the line
a = 1
b = 2
N = 1000 
x = np.linspace(1,N, N)
y = a*x + b

# blur the line
n = rand.normal(size=N, scale = 1)
yn = y + n


# define helper functions
def sum(arr):
    s = 0
    for i in arr:
        s+=i
    return s


def det(matrix):
    return np.linalg.det(matrix)

# cramer stuff
a = np.array([[N, sum(x)],
              [sum(x), sum(np.square(x))]])
b = np.array([sum(yn), sum(x*y)])

d = det(a)
#print(f"determinant = {d}")

cramer_thing_1 = np.array([b, a[1]])
cramer_thing_2 = np.array([a[0], b])

delta_1 = det(cramer_thing_1)
delta_2 = det(cramer_thing_2)
SSE = sum((yn - y)**2)
SST = sum((yn - np.mean(y))**2)
r_square = 1 - SSE/SST

print(delta_1/d)
print(delta_2/d)
print(f"r^2: {r_square}")

# testing against libraries
def f(x, a, b):
    return a*x + b

m, b = np.polyfit(x, yn, 1)
alpha, pcov = sp.curve_fit(f, x, yn)

plt.scatter(x, yn)
#plt.plot(x, m*x + b)
plt.plot(x, alpha[0]*x + alpha[1])
plt.plot(x, y)
plt.show()

