"""(4) F(body): the force of the towed body

    F(body) = (-m2 * g) + Fb2 + Fd2,

Where:

    m2 = mass of the towed body,

    Fb2 = the buyoancy of the towed body,

    Fd2 = the hydrodynamic force of the towed body

Computed as:

    Fd2 = 1/2 * Cd * p * S * ux * |ux|,
    Fb2 = p * volume * g

"""
import numpy as np
import math
import matplotlib.pyplot as plt

# Constants
RHO = 1026                # gravitational acceleration in m/s²
G = 9.81                  # density of seawater in kg/m³

# other variables:

ux_values = np.linspace(0, 5, 100) # velocity range from 0 to 5 m/s

# YSI Eco_mapper -----------------------------------------------------
m_1 = 31.75         # mass of towed body in kg -- 70 lbs
diameter_1 = 0.147   # diameter in meters -- 14.7cm
radius_1 = diameter_1 / 2
length_1 = 1.778         # length in meters -- (70 in, average range 60-85 in)
cd_1 = 0.133             # drag coefficient for torpedo shape (spec sheet)
S_1 = diameter_1 * length_1

# Calculate buoyancy force using Archimedes’ principle
volume_1 = np.pi * radius_1**2 * length_1  # submerged volume in m³
Fb_1 = RHO * volume_1 * G               # buoyant force in N
print(f"Buoyant Force (Fb_1): {Fb_1:.2f} N")

# Calculate hydrodynamic drag force over a range of velocities
Fd_1 = 0.5 * cd_1 * RHO * S_1 * ux_values**2    # Morison equation

# Calculate total towed body force
F_towed_1 = (-m_1 * G) + Fb_1 + Fd_1

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(ux_values, F_towed_1, label='Drag Force $F(D)$', color='teal')
plt.title('(4) F(body) - Eco-mapper vehicle')
plt.xlabel('Variation in velocity, $u_x$ (m/s)')
plt.ylabel('Drag Force (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Liquid Robotics Mini VR2C -----------------------------------------------------
m_2 = 0.7                # mass of towed body in kg
diameter_2 = 0.054
radius_2 =  diameter_2 / 2
length_2 = 0.317
cd_2 = 0.3                  # drag coefficient for torpedo shape (Change)
S_2 = diameter_2 * length_2

# Calculate buoyancy force using Archimedes’ principle
volume_2 = np.pi * radius_2**2 * length_2  # submerged volume in m³
Fb_2 = RHO * volume_2 * G               # buoyant force in N
print(f"Buoyant Force (Fb_2): {Fb_2:.2f} N")

# Calculate hydrodynamic drag force over a range of velocities
Fd_2 = 0.5 * cd_2 * RHO * S_2 * ux_values**2                # Morison equation

# Calculate total towed body force
F_towed_2 = (-m_2 * G) + Fb_2 + Fd_2

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(ux_values, F_towed_2, label='Drag Force $F(D)$', color='teal')
plt.title('(4) F(body) - VR2C vehicle')
plt.xlabel('Variation in velocity, $u_x$ (m/s)')
plt.ylabel('Drag Force (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()