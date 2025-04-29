"""(8, 9) Daisy-chained Damp System for Towed-Body cable

(8) F(d4): hydrodynamic force for segment of Towed-body cable

    F(d4) = 1/2 * Cd * p * S * ux * |ux|,

Where:

    Cd = drag coefficient for cable segment
    p = density of seawater
    S = projected area for cable segment
    ux = velocity

(9) F(c): force in the vertical direction for each segment of Towed-body cable

    F(c) = -m4 * g + Fb4,

Where:
   
    m4 = mass of cable segment,
    F(b4) = buoyancy of cable segment, computed as:
        F(b4) = p * volume * g


Assuming a cable length of 6 m discretised as 60 segments of length of 100 mm (0.1 m) each as as per Zhang et al.
"""

import numpy as np
import math
import matplotlib.pyplot as plt

# Constants
RHO = 1026                # gravitational acceleration in m/s²
G = 9.81                  # density of seawater in kg/m³

# other variables:

ux_values = np.linspace(0, 5, 100) # velocity range from 0 to 5 m/s
m = 0.05                # !mass of cable segment in kg, assuming cable mass = 3kg
radius = 0.01           # radius in m
diameter =  2 * radius  # diameter in m
length =  0.1           # length in meters
cd =  1                 # !drag coefficient for cable segment (assuming cylinder)
S = diameter * length

# Calculate buoyancy force using Archimedes’ principle
volume = np.pi * radius **2 * length  # submerged volume in m³
Fb = RHO * volume * G               # buoyant force in N

# Calculate vertical force Fc
Fc = (-m * G) + Fb

# Calculate hydrodynamic drag force over a range of velocities Fd
Fd = 0.5 * cd * RHO * S * ux_values**2    # Morison equation

# Plotting -- Fd
plt.figure(figsize=(8, 5))
plt.plot(ux_values, Fd, label='Drag Force on Cable segment $F(D)$', color='teal')
plt.title('Hydrodynamic Force on cable segment')
plt.xlabel('Current Velocity (m/s)')
plt.ylabel('Drag Force (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()