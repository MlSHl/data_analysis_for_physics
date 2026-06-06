import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

from discrete_fourier_analysis import analyze_and_plot

H_alpha_air = 6562.8
D1 = 5896
C = 300000

# data harness
folder = "images"
images = [] 
for filename in range(1, 1000):
    img = plt.imread(f"{folder}/{filename}.tif")
    images.append(img)

def double_gaussian(x, A1, mu1, sigma1, A2, mu2, sigma2, C):
    return (
        A1 * np.exp(-(x - mu1)**2 / (2 * sigma1**2))
        + A2 * np.exp(-(x - mu2)**2 / (2 * sigma2**2))
        + C
    )

# fitting functions
def gaussian(x, A, mu, sigma, C):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2)) + C

def laplace_peak(x, A, mu, b, C):
    return A * np.exp(-np.abs(x - mu) / b) + C

def fit(y_data, x_data, model):
    p0 = [
        y_data.max() - y_data.min(),   # A
        x_data[np.argmax(y_data)],     # mu
        10,                            # sigma
        y_data.min()                   # C
    ]

    params, covariance = curve_fit(model, x_data, y_data, p0=p0)

    return params

def fit_double_gaussian(y_data, x_data):
    p0 = [
        y_data.max() - y_data.min(), 250, 5,  
        6000, 280, 5,                         
        y_data.min()                          
    ]

    params, covariance = curve_fit(
        double_gaussian,
        x_data,
        y_data,
        p0=p0
    )

    return params

half_widths = []

# analysis
def analysis(i):
    section1 = i[120:350]
    section2 = i[580:650]

    x_section1 = np.arange(120, 350)
    x_section2 = np.arange(580, 650)

    # section 1 Gaussian fit
    fit_sec_1 = fit_double_gaussian(section1, x_section1)
    fit_1 = double_gaussian(x_section1, *fit_sec_1)

    # section 2 Laplace fit
    fit_sec_2 = fit(section2, x_section2, laplace_peak)
    fit_2 = laplace_peak(x_section2, *fit_sec_2)

    # unpack centers
    A1, mu1, sigma1, A2, mu2, sigma2, C1 = fit_sec_1
    A_lap, mu_lap, b_lap, C_lap = fit_sec_2

    # Calculate velocity
    lmbd = mu2/10 + (H_alpha_air - D1)
    print(f"mu_lap: {mu_lap}");
    delta_lmbd = np.abs(mu_lap - lmbd)/10000 # scale the pixel 1 to 10000
    velocity = delta_lmbd / lmbd * C
    print(f"delta_lambda/lambda: {delta_lmbd / lmbd}");
    print(f"Velocity: {velocity} km/s");

    # Calculate mid width
    laplace_fwhm = 2 * abs(b_lap) * np.log(2)
    half_widths.append(laplace_fwhm)
    print(f"Mid point width: {laplace_fwhm}");


    # Plotting
    # plt.plot(i, label="full row")
    # plt.plot(x_section1, section1, label="section 1 data")
    # plt.plot(x_section1, fit_1, label="section 1 Gaussian fit")

    # plt.scatter(lmbd, 0, label="expected shifted H-alpha")
    # plt.scatter(mu_lap, 0, label="measured Laplace center")
    # plt.scatter(mu2, 0, label="D1/second Gaussian center")

    # plt.plot(x_section2, section2, label="section 2 data")
    # plt.plot(x_section2, fit_2, label="section 2 Laplace fit")
    # # plt.scatter(mu2, 0);
    # # plt.scatter(mu_lap, 0);

    # plt.legend()
    # plt.show()


for i in images:
    analysis(i[10])


time = np.arange(len(half_widths)) * 10  # seconds

plt.scatter(time, half_widths)
plt.xlabel("Time [s]")
plt.ylabel("Hα half-width [Å]")
plt.title("Hα half-width over time")
plt.show()

analyze_and_plot(time, half_widths)



