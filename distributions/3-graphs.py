import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

gamma = 0.5

def eps(k, h, gamma):
    return np.sqrt((h + np.cos(k))**2 + (gamma**2) * (np.sin(k)**2))

def energy(h, gamma):
    integrand = lambda k: eps(k, h, gamma)
    val, _ = quad(integrand, 0, np.pi, limit=200)
    return -val / (2 * np.pi)

def magnetization(h, gamma):
    integrand = lambda k: (h + np.cos(k)) / eps(k, h, gamma)
    val, _ = quad(integrand, 0, np.pi, limit=200)
    return val / (2 * np.pi)

def susceptibility(h, gamma):
    integrand = lambda k: (gamma**2) * (np.sin(k)**2) / (eps(k, h, gamma)**3)
    val, _ = quad(integrand, 0, np.pi, limit=200)
    return val / (2 * np.pi)

# h starts from 0
h_vals = np.linspace(0, 5, 400)

E_vals = np.array([energy(h, gamma) for h in h_vals])
M_vals = np.array([magnetization(h, gamma) for h in h_vals])
X_vals = np.array([susceptibility(h, gamma) for h in h_vals])

plt.figure(figsize=(9, 5))
plt.plot(h_vals, E_vals, label=r"$E^\gamma(h)$")
plt.plot(h_vals, M_vals, label=r"$M_z^\gamma(h)$")
plt.plot(h_vals, X_vals, label=r"$\chi_{zz}^\gamma(h)$")

plt.xlabel(r"$h$")
plt.ylabel("Value")
plt.title(r"$E^\gamma(h)$, $M_z^\gamma(h)$, and $\chi_{zz}^\gamma(h)$")
plt.grid(True)
plt.legend()
plt.show()
