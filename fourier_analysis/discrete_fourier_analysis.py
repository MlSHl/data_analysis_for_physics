import numpy as np
import matplotlib.pyplot as plt

# u is the function we are doing analysis for
def calc_coefficients(u, r):
    n = len(u)
    angle = 2*np.pi/n
    a = 0
    b = 0
    for k in range(n):
        a += u[k] * np.cos(angle * k * r) 
        b += u[k] * np.sin(angle * k * r) 

    a *= 2/n
    b *= 2/n

    return a, b

def analyze_and_plot(x, u, title="", max_period=10):
    # calc cofficients
    N = len(u)

    coefficients = {
        "a": [],
        "b": []
    }

    for i in range(1, N // 2 + 1):
        a, b = calc_coefficients(u, i)
        coefficients["a"].append(a)
        coefficients["b"].append(b)

    a_vals = np.array(coefficients["a"])
    b_vals = np.array(coefficients["b"])

    # calc amplitudes
    amplitudes = np.sqrt(a_vals**2 + b_vals**2)

    # reconstruct original function
    a0 = np.mean(u)
    u_approx = np.full(N, a0)

    for r in range(1, N // 2 + 1):
        a = coefficients["a"][r - 1]
        b = coefficients["b"][r - 1]

        for k in range(N):
            angle = 2 * np.pi * k * r / N
            u_approx[k] += a * np.cos(angle) + b * np.sin(angle)

    bins = np.arange(1, N // 2 + 1)

    # Plot original and approximation
    plt.plot(x, u, label="Original")
    plt.plot(x, u_approx, "--", label="Fourier approximation")
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

    dx = x[1] - x[0]
    periods = 2*np.pi/bins

    plt.plot(periods, amplitudes, marker="o")
    plt.xlabel("Period")
    plt.ylabel("Amplitude")
    plt.title(f"Fourier spectrum: {title}")
    plt.grid()
    plt.xlim(0, max_period) 
    plt.show()

    return periods, amplitudes

# 9
data = np.loadtxt("sunspot.dat")

years = data[:, 0]
sunspots = data[:, 1]

analyze_and_plot(years, sunspots, title="Sunspot yearly data", max_period=120)

# 1
N = 1000

single_periods = [1, 2, 2*np.pi/3, 3]

for T in single_periods:
    L = 20 * T
    x = np.linspace(0, L, N, endpoint=False)

    u = np.cos(2 * np.pi * x / T)

    analyze_and_plot(x, u, title=f"Single period T = {T:.3f}")

# 2
N = 1000
x = np.linspace(0, 60, N, endpoint=False)

u = (
    np.cos(2 * np.pi * x / 3)
    + np.cos(2 * np.pi * x / 5)
)

analyze_and_plot(x, u, title="Two dominant periods: 3 and 5")

# 3
N = 1000
x = np.linspace(0, 60, N, endpoint=False)

u = (
    np.cos(2 * np.pi * x / 2.5)
    + np.cos(2 * np.pi * x / 3)
    + np.cos(2 * np.pi * x / 5)
)

analyze_and_plot(x, u, title="Three dominant periods: 2.5, 3, and 5")

# 4
N = 1000
x = np.linspace(0, 60, N, endpoint=False)

u = (
    1 * np.cos(2 * np.pi * x / 3)
    + 3 * np.cos(2 * np.pi * x / 5)
)

analyze_and_plot(x, u, title="Peak heights: amplitude 1 vs amplitude 3")

# 5
N = 1000
x = np.linspace(0, 60, N, endpoint=False)

u = (
    0.5 * np.cos(2 * np.pi * x / 2.5)
    + 2.0 * np.cos(2 * np.pi * x / 3)
    + 4.0 * np.cos(2 * np.pi * x / 5)
)

analyze_and_plot(x, u, title="Adjusted peak heights: 0.5, 2, 4")

# 6
N = 1000
x = np.linspace(0, 60, N, endpoint=False)

u_clean = (
    np.cos(2 * np.pi * x / 2.5)
    + np.cos(2 * np.pi * x / 3)
    + np.cos(2 * np.pi * x / 5)
)

gaussian_noise = np.random.normal(0, 0.5, N)
u_gaussian = u_clean + gaussian_noise

analyze_and_plot(x, u_gaussian, title="Three periods + Gaussian noise")

uniform_noise = np.random.uniform(-0.5, 0.5, N)
u_uniform = u_clean + uniform_noise

analyze_and_plot(x, u_uniform, title="Three periods + Uniform noise")

laplace_noise = np.random.laplace(0, 0.5, N)
u_laplace = u_clean + laplace_noise

analyze_and_plot(x, u_laplace, title="Three periods + Laplace noise")

# 7
N = 1000
x = np.linspace(0, 60, N, endpoint=False)

u_clean = (
    np.cos(2 * np.pi * x / 2.5)
    + np.cos(2 * np.pi * x / 3)
    + np.cos(2 * np.pi * x / 5)
)

u_zeroed = u_clean.copy()

number_of_zeros = 150
indices = np.random.choice(N, number_of_zeros, replace=False)

u_zeroed[indices] = 0

analyze_and_plot(x, u_zeroed, title="150 random values replaced by zero")

# 8 
N = 1000
x = np.linspace(0, 60, N, endpoint=False)

u_clean = (
    np.cos(2 * np.pi * x / 2.5)
    + np.cos(2 * np.pi * x / 3)
    + np.cos(2 * np.pi * x / 5)
)

number_to_remove = 150
indices = np.random.choice(N, number_to_remove, replace=False)

x_removed = np.delete(x, indices)
u_removed = np.delete(u_clean, indices)

analyze_and_plot(x_removed, u_removed, title="150 data points removed")

