"""(3) F(Umbilical): represents the force of the umbilical.

    F(umbilical) = -m1 * g + Fb1 + Fd1,

Where:

        g = 9.81 m/s², Gravity

        rho = 1026 kg/m³, Density of seawater

     Umbilical Parameters:

        m1 = 50 kg, Mass of umbilical

        length = 10 m, Length of umbilical submerged

        diameter = 0.05 m, Diameter of umbilical

        CD = 1.1, drag coefficient for a cylinder

         A = diameter * length m², Projected area perpendicular to flow

    Environmental Conditions:

     u = 0-3 m/s, Horizontal water speed range
     (from environmental modelling or sensor input)
"""

import numpy as np
import matplotlib.pyplot as plt

# Range for ux (variation in horizontal velocity)
ux_values = np.linspace(0, 10, 50)

# Constants
G = 9.81                  # gravitational acceleration in m/s²
RHO = 1025                # density of seawater in kg/m³ (typical value)
M1 = 50                   # mass of umbilical in kg (measured or estimated)
length = 10               # length of umbilical in meters (variable)
diameter = 0.05           # diameter in meters
radius = diameter / 2     # radius in meters

# Drag force parameters
CD = 1.1                  # drag coefficient for cylindrical shape
A = diameter * length     # projected area perpendicular to flow in m²

# Calculate buoyancy force Fb(1) using Archimedes’ principle
volume = np.pi * radius**2 * length  # submerged volume in m³
Fb1 = RHO * volume * G               # buoyant force in N

# Hydrodynamic drag force on the umbilical using Morison equation
Fd1 = 0.5 * CD * RHO * A * ux_values * abs(ux_values)

# Total umbilical force
F_umbilical = -M1 * G + Fb1 + Fd1

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(ux_values, F_umbilical, label='F(umbilical)', color='blue', linewidth=2)
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.xlabel('Variation in velocity, $u_x$ (m/s)')
plt.ylabel('Umbilical Force F_umbilical [N]')
plt.title('(3) F(Umbilical)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()