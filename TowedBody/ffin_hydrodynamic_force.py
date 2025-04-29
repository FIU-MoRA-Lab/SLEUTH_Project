"""F(Fin): The Hydrodynamic force of each fin on the raft

    F(Fin) = 1/2 * Cd3 * rho * S3 * u3 * cos(alpha) * |u3 * cos(alpha)|
    + 1/2 * Cl3 * rho * S3 * sin(alpha) * |u3 * sin(alpha)|,

Where:

    rho = 1026 kg/m³, Density of seawater,

    Cd3 = the drag coefficient of the fin,

    Cl3 = the lift coefficient of the fin,

    S3 = the projected area of the fin perpendicular to the flow direction, assuming a rectangular shape (S = b * c),

    u3 = the horizontal velocity of the fin,

    alpha = the "attack angle" of the fin

As per Wang et al, 2018:

    Cl = (1.8 * pi * lambda) /
    cos(chi) * (sqrt( ((lambda^2)/(cos^4(chi)) + 4) + 1.8
    * alpha(k) + (Cdc / lambda) * alpha(k)^2

    Cd = CdO + (Cl)^2/0.9 * pi * lambda
"""

import numpy as np
import math
import matplotlib.pyplot as plt

# Constants
RHO = 1026
S = 0.06      #m^2, from zhang et al

# other variables
chi = 0.25
lamb = 2
alpha = 18
c_dc = 0.6
pi = 3.14
c_do = 0.008
cos_4_chi = math.cos(chi) ** 4

u3 = np.linspace(0, 5, 100)      # velocity range from 0 to 5 m/s

# Computing c_lift3 in steps
sqrt_denom = math.cos(chi) * math.sqrt( ((math.pow(lamb, 2))/cos_4_chi) + 4)

c_lift_1 = ((1.8 * pi * lamb) / ((math.cos(chi) * sqrt_denom) + 1.8))

c_lift_2 = (c_dc / lamb) * math.pow(alpha, 2)

print("square root denom: ", sqrt_denom)
print("front: ", c_lift_1)
print("back: ", c_lift_2)

c_lift = c_lift_1 * alpha * c_lift_2

print("c_lift: ", c_lift)

# Computing c_drag3
c_drag_back = math.pow(c_lift, 2) / 0.9 * pi * lamb
c_drag = c_do + c_drag_back

print("back_2: ", c_drag_back)
print("c_drag: ", c_drag)

# f_fin in parts
sin_alpha = math.sin(alpha)
cos_alpha = math.cos(alpha)

f_fin = (6) * (0.5 * c_drag * RHO * S * u3 * cos_alpha * abs(u3 * cos_alpha)) + 0.5 * c_lift * RHO * S * u3 * sin_alpha * abs(u3 * sin_alpha)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(u3, f_fin, label='Hydrodynamic force of fin $F(fin)$', color='teal')
plt.title('(5,6) F(Fin)')
plt.xlabel('Variation in velocity, $u_x$ (m/s)')
plt.ylabel('Drag Force (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()