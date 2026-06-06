import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipeinc

delta = 0.5

def M_delta(h, delta):
    if 0 <= h <= delta:
        return 0.0
    elif delta < h <= 1:
        return (1 / np.pi) * np.arcsin(np.sqrt((h**2 - delta**2) / (1 - delta**2)))
    else:  # h >= 1
        return 0.5

def E_delta(h, delta):
    M = M_delta(h, delta)
    phi = np.pi * (0.5 - M)
    m = 1 - delta**2
    return -(1 / np.pi) * ellipeinc(phi, m) - h * M

def chi_delta(h, delta):
    if delta < h < 1:
        return h / (np.pi * np.sqrt((1 - h**2) * (h**2 - delta**2)))
    else:
        return 0.0

h_vals = np.linspace(-np.pi, np.pi, 800)

E_vals = np.array([E_delta(h, delta) for h in h_vals])
M_vals = np.array([M_delta(h, delta) for h in h_vals])
chi_vals = np.array([chi_delta(h, delta) for h in h_vals])

plt.figure(figsize=(10, 6))
plt.plot(h_vals, E_vals, label=rf"$E^\delta(h)$")
plt.plot(h_vals, M_vals, label=rf"$M_z^\delta(h)$")
plt.plot(h_vals, chi_vals, label=rf"$\chi_{{zz}}^\delta(h)$")

plt.xlabel(r"$h$")
plt.ylabel("Value")
plt.title(rf"$E^\delta(h)$, $M_z^\delta(h)$, and $\chi_{{zz}}^\delta(h)$ for $\delta={delta}$")
plt.grid(True)
plt.legend()
plt.show()
