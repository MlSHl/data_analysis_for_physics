import numpy as np
import matplotlib.pyplot as plt


def calc_coefficients(u, r):
	u = np.asarray(u, dtype=float)

	n = len(u)
	angle = 2 * np.pi / n

	a = 0.0
	b = 0.0

	for k in range(n):
		a += u[k] * np.cos(angle * k * r)
		b += u[k] * np.sin(angle * k * r)

	a *= 2 / n
	b *= 2 / n

	return a, b


def analyze_and_plot(x, u, title="", max_period=None):
	x = np.asarray(x, dtype=float)
	u = np.asarray(u, dtype=float)

	N = len(u)

	coefficients = {
		"a": [],
		"b": []
	}

	for r in range(1, N // 2 + 1):
		a, b = calc_coefficients(u, r)
		coefficients["a"].append(a)
		coefficients["b"].append(b)

	a_vals = np.array(coefficients["a"])
	b_vals = np.array(coefficients["b"])

	amplitudes = np.sqrt(a_vals**2 + b_vals**2)

	# Reconstruct original function
	a0 = np.mean(u)
	u_approx = np.full(N, a0)

	for r in range(1, N // 2 + 1):
		a = coefficients["a"][r - 1]
		b = coefficients["b"][r - 1]

		for k in range(N):
			angle = 2 * np.pi * k * r / N
			u_approx[k] += a * np.cos(angle) + b * np.sin(angle)

	bins = np.arange(1, N // 2 + 1)

	# Plot original and Fourier approximation
	plt.plot(x, u, label="Original")
	plt.plot(x, u_approx, "--", label="Fourier approximation")
	plt.xlabel("Time [s]")
	plt.ylabel("Signal")
	plt.title(title)
	plt.legend()
	plt.grid()
	plt.show()

	# Correct period formula for real x-axis spacing
	dx = x[1] - x[0]
	periods = N * dx / bins

	plt.plot(periods, amplitudes, marker="o")
	plt.xlabel("Period [s]")
	plt.ylabel("Amplitude")
	plt.title(f"Fourier spectrum: {title}")
	plt.grid()

	if max_period is not None:
		plt.xlim(0, max_period)

	plt.show()

	dominant_index = np.argmax(amplitudes)
	dominant_period = periods[dominant_index]

	print(f"Dominant period: {dominant_period:.3f} s")
	print(f"Dominant period: {dominant_period / 60:.3f} min")

	return periods, amplitudes
