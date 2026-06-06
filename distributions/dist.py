from numpy import random as rand
import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 2

x = np.linspace(1,10, 10)
n = rand.normal(size=10, scale = 1)
y = a*x + b
yn = y + n

plt.plot(x, y)
plt.scatter(x, yn)
plt.show()
