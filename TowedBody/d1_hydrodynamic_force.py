"""F(D1): Hydrodynamic Force of the Umbilical"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.81                  # gravitational acceleration in m/s²
rho = 1025                # density of seawater in kg/m³

# Umbilical properties
m1 = 50                   # mass of umbilical in kg
length = 10               # length of umbilical in meters
diameter = 0.05           # diameter in meters
radius = diameter / 2     # radius in meters

# Drag force parameters
CD = 1.1                  # drag coefficient for cylindrical shape
A = diameter * length     # projected area perpendicular to flow in m²

# Calculate buoyancy force Fb1 using Archimedes’ principle
volume = np.pi * radius**2 * length  # submerged volume in m³
Fb1 = rho * volume * g               # buoyant force in N

print(f"Buoyant Force (Fb1): {Fb1:.2f} N")

# Calculate hydrodynamic drag force over a range of velocities
u = np.linspace(0, 10, 50)                     # velocity range from 0 to 10 m/s
Fd1 = 0.5 * CD * rho * A * u**2                # Morison equation

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(u, Fd1, label='Drag Force $F(D)$', color='teal')
plt.title('Hydrodynamic Drag Force on Umbilical')
plt.xlabel('Current Velocity (m/s)')
plt.ylabel('Drag Force (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()