from scipy.stats import rayleigh
import numpy as np

x = np.arange(0, 1, 0.001)
plt.title("Rayleigh(57) PPF")
plt.plot(x, rayleigh.ppf(x, scale=57))
