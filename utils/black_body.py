""" 

"""

import numpy as np

# Constants
h = 6.62607015e-34  # Planck's constant (J·s)
c = 3.0e8           # Speed of light (m/s)
k = 1.380649e-23    # Boltzmann constant (J/K)
b = 2.897e-3        # Wien's displacement constant (m·K)
sigma = 5.67e-8     # Stefan-Boltzmann constant (W/m^2·K^4)

# Planck's Law function
def planck(lam, T):
    return (2*h*c**2) / (lam**5) * (1 / (np.exp(h*c / (lam*k*T)) - 1))

# Wien's Law function
def wien_peak_temp(T):
    return b / T  # Peak wavelength (m)

# Stefan-Boltzmann Law for power
def stefan_boltzmann(T):
    return sigma * T**4
