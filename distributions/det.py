import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2],
              [3, 4]])
b = np.array([5, 6])

def det(matrix):
    return np.linalg.det(matrix)

d = det(a)
print(f"determinant = {d}")

cramer_thing_1 = np.array([b, a[1]])
cramer_thing_2 = np.array([a[0], b])

delta_1 = det(cramer_thing_1)
delta_2 = det(cramer_thing_2)

print(delta_1/d)
print(delta_2/d)
