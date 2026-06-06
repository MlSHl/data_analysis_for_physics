import matplotlib.pyplot as plt
import numpy as np

a = 1
b = -6
c = 11
d = -6 

delta_0 = b**2 - 3*a*c
delta_1 = 2*b**3 - 9*a*b*c + 27* a**2 * d

sqrt_term = np.sqrt(delta_1**2 - 4*delta_0**3 + 0j)

C_plus = ((delta_1 + sqrt_term)/2)**(1/3)
C_minus = ((delta_1 - sqrt_term)/2)**(1/3)

C = C_plus
if (C==0):
    C = C_minus

qsi = (-1 + np.sqrt(3)*1j)/2

k = [0, 1, 2]

def x(k):
    if (abs(C) < 1e-12):
        return -(b/(3*a))
    else:
        return -(1/(3*a))*(b+(qsi**k)*C + delta_0/((qsi**k)*C))

for i in k:
    sol = x(i)
    print(f"k={i} -> x={sol}")


# Plotting for comparison
def polynomial(x):
    return a*x**3 + b*x**2 + c*x + d

x = np.linspace(0, 5)
y = polynomial(x)

plt.plot(x, y);
plt.axhline(0)
plt.grid(True)
plt.savefig("image_cubic.png", dpi=150, bbox_inches="tight")
