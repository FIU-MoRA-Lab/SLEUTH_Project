# Towed Body Model Code Overview

This README provides an explanation of the Python code that models different forces acting on a Wave Glider with a towed body system. The model is based on Zhang et al. (2020) - "Analysis of the Dynamic System of Wave Glider with a Towed Body".

## Table of Contents

1. [Force on Float (F_Float)](#1-force-on-float-f_float)
2. [Hydrodynamic Drag Force (F_Drag)](#2-hydrodynamic-drag-force-f_drag)
3. [Umbilical Force (F_Umbilical)](#3-umbilical-force-f_umbilical)
4. [Hydrodynamic Force on Umbilical (F_D1)](#4-hydrodynamic-force-on-umbilical-f_d1)
5. [Fin Force (F_Fin)](#5-fin-force-f_fin)
6. [Towed Body Force (F_Body)](#6-towed-body-force-f_body)
7. [Towed Body Cable Forces (F_D4 and F_C)](#7-towed-body-cable-forces-f_d4-and-f_c)

## 1. Force on Float (F_Float)

**Description**: Calculates the vertical force on the float, combining buoyancy and gravity.

**Formula**: `F_Float = -mg + (ρ * A * (y+y1) * g)`

**Parameters**:

- `m`: Mass of the float (155 kg)
- `g`: Gravitational acceleration (9.8 m/s²)
- `ρ`: Density of seawater (1026 kg/m³)
- `A`: Cross-sectional area of the float (0.19 m²)
- `y`: Initial draft of the float (0 m)
- `y1`: Variation in draft (0-15 m)

**Function**: Plots the relationship between variation in draft and the resulting vertical force on the float.

## 2. Hydrodynamic Drag Force (F_Drag)

**Description**: Calculates the hydrodynamic force on the float based on the Morison equation.

**Formula**: `F_Drag = (1/2) * Cd * ρ * S * ux * |ux|`

**Parameters**:

- `Cd`: Drag coefficient (0.0030)
- `ρ`: Density of seawater (1026 kg/m³)
- `S`: Projected area of immersed portion (1 m²)
- `ux`: Horizontal velocity (0-10 m/s)

**Function**: Plots the relationship between horizontal velocity and the resulting drag force.

## 3. Umbilical Force (F_Umbilical)

**Description**: Calculates the total force on the umbilical connecting the float to the submerged glider.

**Formula**: `F_Umbilical = -m1 * g + Fb1 + Fd1`

**Parameters**:

- `m1`: Mass of umbilical (50 kg)
- `g`: Gravitational acceleration (9.81 m/s²)
- `Fb1`: Buoyancy force of umbilical
- `Fd1`: Drag force on umbilical
- `length`: Length of umbilical (10 m)
- `diameter`: Diameter of umbilical (0.05 m)
- `CD`: Drag coefficient for cylindrical shape (1.1)

**Function**: Plots the relationship between horizontal velocity and the total force on the umbilical.

## 4. Hydrodynamic Force on Umbilical (F_D1)

**Description**: Specifically calculates the drag force component for the umbilical.

**Formula**: `Fd1 = 0.5 * CD * ρ * A * u²`

**Parameters**: Same as section 3, but focusing only on the drag component.

**Function**: Plots the relationship between current velocity and the drag force on the umbilical.

## 5. Fin Force (F_Fin)

**Description**: Calculates the hydrodynamic force on each fin of the raft, combining drag and lift forces.

**Formula**:

```
F_Fin = (1/2) * Cd3 * ρ * S3 * u3 * cos(α) * |u3 * cos(α)|
      + (1/2) * Cl3 * ρ * S3 * sin(α) * |u3 * sin(α)|
```

**Parameters**:

- `ρ`: Density of seawater (1026 kg/m³)
- `S`: Projected area of fin (0.06 m²)
- `u3`: Horizontal velocity (0-5 m/s)
- `α`: Attack angle (18°)
- Complex coefficients for drag and lift calculated from mathematical formulas

**Function**: Plots the relationship between velocity and the hydrodynamic force on the fins.

## 6. Towed Body Force (F_Body)

**Description**: Calculates the total force on the towed body for two different vehicles: YSI Eco-mapper and Liquid Robotics Mini VR2C.

**Formula**: `F_Body = (-m2 * g) + Fb2 + Fd2`

**Parameters for Eco-mapper**:

- `m_1`: Mass (31.75 kg)
- `diameter_1`: Diameter (0.147 m)
- `length_1`: Length (1.778 m)
- `cd_1`: Drag coefficient (0.133)

**Parameters for VR2C**:

- `m_2`: Mass (0.7 kg)
- `diameter_2`: Diameter (0.054 m)
- `length_2`: Length (0.317 m)
- `cd_2`: Drag coefficient (0.3)

**Function**: Plots the relationship between velocity and the total force for each towed body model.

## 7. Towed Body Cable Forces (F_D4 and F_C)

**Description**: Models the forces on segments of the towed body cable using a daisy-chained damping system.

**Formula for F_D4 (hydrodynamic force)**: `F_D4 = (1/2) * Cd * ρ * S * ux * |ux|`

**Formula for F_C (vertical force)**: `F_C = -m4 * g + Fb4`

**Parameters**:

- `m`: Mass of cable segment (0.05 kg)
- `radius`: Cable radius (0.01 m)
- `length`: Segment length (0.1 m)
- `cd`: Drag coefficient (1.0)

**Function**: Plots the relationship between velocity and the drag force on a cable segment.

---

## Usage Notes

1. All plots use metric units (Newtons, meters, seconds, etc.)
2. The code segments simulate different components of the Wave Glider system independently
3. Parameters are based on literature values or reasonable estimates for actual equipment
4. The model assumes steady-state conditions for simplicity
5. Different velocity ranges are used for different components based on their operational characteristics
