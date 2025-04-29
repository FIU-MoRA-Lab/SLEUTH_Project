"""
(1)   F_Float:
      Represents the force in the vertical direction of the float, including buoyancy and gravity.

         F(Float) = -mg + (p * A * (y+y1) * g),

  Where:

    m = the mass of the float body,

    g = the force of gravity,

    p (Rho) = the density of the seawater,

    A = the cross sectional area of the float, computed from frontal view as W x H, of float + glider,

    y = the draft of the float at some initial time,

    y1 = the change in draft of the float.



 This graph is plotted as a function of Force (N) per variation in draft (y1)

 Values:

    m = 155 kg,

      for WaveGlider SV3 including the float, umbilical and submerged glider. No payloads. From Google.

    g = 9.8 m/s^2,

    p = 1026 kg/m^3,

      From Google.

    A = 0.19 m^2,

      A(total) = A(float) + A(Glider) = 0.09 +0.1 = 0.19 m^2

    y = 0,

      Arbitrary
"""

import numpy as np
import matplotlib.pyplot as plt

# Range for y1 (variation in draft)
y1_values = np.linspace(0, 15, 400)

# Constants
M = 155  # mass of the float (kg)
G = 9.8  # acceleration due to gravity (m/s^2)
RHO = 1026  # density of seawater (kg/m^3)
A = 0.19  # cross-sectional area of the float (m^2)
y = 0  # initial draft of the float (m)

# Compute F_float for different values of y1
F_float = -M * G + RHO * A * (y + y1_values) * G

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(y1_values, F_float, label=r'$F_{\text{float}} = -mg + \rho A(y + y_1)g$', color='b')
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Equilibrium line
plt.axvline(0, color='gray', linestyle='--', linewidth=1)  # Reference line for y1 = 0

# Labels and title
plt.xlabel(r'Variation in Draft, $y_1$ (m)')
plt.ylabel(r'Float Force, $F_{\text{float}}$ (N)')
plt.title('(1) F(Float)')
plt.legend()
plt.grid(True)

# Plot
plt.show()