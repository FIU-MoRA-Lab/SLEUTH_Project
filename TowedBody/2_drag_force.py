"""(2) F(Drag): Represents the hydrodynamic force of the float, given on the basis of the Morison equation.

     F(Drag) = 1/2 * Cd * p * S * ux * |ux|,

Where:

    Cd = the drag coefficient of the float, computed as:

    S = the projected area of the immersed portion perpendicular to the flow direction,

    p (Rho) = the density of the seawater,

    ux = the horizontal velocity of the float,

This graph is plotted as a function of force (N) per variation in horizontal velocity (m/s)

Values:

    Cd = 0.0030,

       an average, between the range of the Cd of a Kayak and a Keelboat.
    

         [Another option]: Cd = (2 * M * G)/(p A ux^2) [Youtube]
      

    S = Computed as
            A(rectangle) + A(triangle)
            = (w * h(rectangle)) + (1/2 * w * h(triangle))
            = (0.81 * 0.1) + (1/2 * 0.81 * 0.13)
            = 0.081 + 0.05265
            = 0.13365 m^2 = 0.134 m^2
          
        Values are estimates taken from WG spec sheet:

        WG float dimensions = (l * w * h) = 305 cm * 81 cm * 23 cm

          height was split between triangle
      

    p (Rho) = 1026 kg/m^3


(2.1) F(Drag_1): For computation of umbilical chord.

    F(Drag_1) = 1/2 * Cd * p * S * ux * |ux|,

Where:

    Cd = the drag coefficient of the umbilical chord

    S = the projected area of the immersed portion perpendicular to the flow direction,

    p (Rho) = the density of the seawater,

    ux = the horizontal velocity of the float,

(2.2) F(Drag_2): For computation of towed body.

    F(Drag_2) = 1/2 * Cd * p * S * ux * |ux|,

Where:

    Cd = the drag coefficient of the towed body

    S = the projected area of the immersed portion perpendicular to the flow direction,

    p (Rho) = the density of the seawater,

    ux = the horizontal velocity of the towed body,
    
"""

import numpy as np
import matplotlib.pyplot as plt

# Range for ux (variation in horizontal velocity)
ux_values = np.linspace(0, 10, 50)

# Constants
M = 155  # mass of the float (kg)
G = 9.8  # acceleration due to gravity (m/s^2)
RHO = 1026  # density of seawater (kg/m^3)
A = 0.19  # cross-sectional area of the float (m^2)
S = 1 # projected area of immersed portion (m^2) | SAMPLE
Cd = 0.0030
# Cd = (2 * M * G)/(1026 * 0.19 * pow(ux_values, 2)) # drag coefficient (dimensionless)


# Compute F_drag for different values of y1
F_drag = 1/2 * Cd * RHO * S * ux_values * abs(ux_values)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(ux_values, F_drag, label=r'$F_{\text{drag}} = 1/2 * Cd * RHO * S * ux * |ux|$', color='b')
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Equilibrium line
plt.axvline(0, color='gray', linestyle='--', linewidth=1)  # Reference line for y1 = 0

# Labels and title
plt.xlabel(r'Variation in velocity, $u_x$ (m/s)')
plt.ylabel(r'Float Force, $F_{\text{float}}$ (N)')
plt.title('(2) F(Drag)')
plt.legend()
plt.grid(True)

# Plot
plt.show()