---
title: "Beam Element in FEM"
date: 2025-03-17
categories: course
tags:
layout: post
---

## **1. Review of Truss vs. Beam (1-D Elements)**

| **Truss**                         | **Beam**                          |
|-----------------------------------|-----------------------------------|
| Supports **axial loads** only     | Supports **axial** and **bending loads** |
| Lecture #05                      | Lecture #06                      |

---

## **2. General Formula (From Previous Lecture)**

- General Displacement Approximation:  
  \[
  \{ u(x, y, z) \} = [N] \{ u_n \}
  \]

- Strain-Displacement Relation:  
  \[
  \varepsilon = [B] \{ u_n \}
  \]  
  where \( [B] = \partial N \).

- Stress:  
  \[
  \sigma = E \varepsilon = E [B] \{ u_n \}
  \]

- Element Stiffness Matrix:  
  \[
  [k^e] = \int_V B^T E B \, dV
  \]

- Truss Example Stiffness Matrix (1-D):  
  \[
  [k] = \frac{AE}{L} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}
  \]

---

## **3. Types of Beams (Boundary Cases)**

- **Case 1**: Simple supports (pinned).  
- **Case 2**: Fixed support (clamped).  
- **Case 3**: Cantilevered beams.  
- Each **nodal DOF** includes **translational** and **rotational** components (v, θ).

---

## **4. Beam Deflection and Slope**

- **Deflection**:  
  \[
  v(x)
  \]

- **Slope (Angle of rotation)**:  
  \[
  \theta(x) = \frac{dv}{dx}
  \]

- **Curvature**:  
  \[
  \kappa(x) = \frac{d^2 v}{dx^2}
  \]

- **Curvature Change Rate**:  
  \[
  \frac{d^3 v}{dx^3}
  \]

---

## **5. Bending Moment, Shear Force, and Stress-Strain Relation**

- Moment-Curvature Relation:  
  \[
  M(x) = -EI \frac{d^2 v}{dx^2}
  \]

- Shear Force Relation:  
  \[
  V(x) = -EI \frac{d^3 v}{dx^3}
  \]

- Axial Strain at \( y \) from neutral axis:  
  \[
  \varepsilon_x = -y \frac{d^2 v}{dx^2}
  \]

- Axial Stress:  
  \[
  \sigma_x = -E y \frac{d^2 v}{dx^2}
  \]

---

## **6. Degrees of Freedom (DOF) for Simple Beam**

For nodes \( 1 \) and \( 2 \):  
\[
\{ n \} = \begin{Bmatrix} v_1 \\ \theta_1 \\ v_2 \\ \theta_2 \end{Bmatrix}
\]

---

## **7. Shape Functions for Beam Elements**

- Interpolated displacement field:  
  \[
  v(x) = N_1(x) v_1 + N_2(x) \theta_1 + N_3(x) v_2 + N_4(x) \theta_2
  \]

- Interpolated slope field:  
  \[
  \theta(x) = \frac{dv}{dx} = \text{function of } \{ v_1, \theta_1, v_2, \theta_2 \}
  \]

- Shape function \( N_i(x) \):  
  Typically cubic polynomials for beams to represent constant shear and moment variations.

---

## **8. Example of Shape Functions**

- \( N_1(x) = 1 - 3(x/L)^2 + 2(x/L)^3 \)  
- \( N_2(x) = x(1 - x/L)^2 \)  
- \( N_3(x) = 3(x/L)^2 - 2(x/L)^3 \)  
- \( N_4(x) = x(x/L)^2 - x^2/L \)

---

## **9. Strain-Displacement Matrix [B]**

- For beam bending strain (axial):  
  \[
  \varepsilon_x = -y \frac{d^2 v}{dx^2}
  \]

- [B] matrix involves second derivatives of \( N_i(x) \):  
  \[
  [B] = y \cdot \begin{bmatrix} \frac{d^2 N_1}{dx^2} & \frac{d^2 N_2}{dx^2} & \frac{d^2 N_3}{dx^2} & \frac{d^2 N_4}{dx^2} \end{bmatrix}
  \]

---

## **10. Element Stiffness Matrix for Beam**

- General formula:  
  \[
  [k^e] = \int_0^L B^T E B \, dV = \int_0^L \frac{d^2 N}{dx^2} EI \frac{d^2 N}{dx^2} dx
  \]

- Simplified matrix for uniform properties:  
  \[
  [k^e] = \frac{EI}{L^3}
  \begin{bmatrix}
  12 & 6L & -12 & 6L \\
  6L & 4L^2 & -6L & 2L^2 \\
  -12 & -6L & 12 & -6L \\
  6L & 2L^2 & -6L & 4L^2
  \end{bmatrix}
  \]

---

## **11. Bending Moment, Strain, and Stress**

- Bending Moment:  
  \[
  M = EI \frac{d^2 v}{dx^2} = EI [B] \{ u \}
  \]

- Strain:  
  \[
  \varepsilon = -y \frac{d^2 v}{dx^2} = -y [B] \{ u \}
  \]

- Stress:  
  \[
  \sigma = E \varepsilon = -E y [B] \{ u \}
  \]

---

## **12. Summary (Beam Element Formulation)**

- Displacement:  
  \[
  v(x) = [N] \{ u \}
  \]

- Strain:  
  \[
  \varepsilon = [B] \{ u \}
  \]

- Stress:  
  \[
  \sigma = E [B] \{ u \}
  \]

- Stiffness Matrix:  
  \[
  [k^e] = \int_V B^T E B \, dV
  \]

- For beam elements:  
  \[
  [k^e] = \frac{EI}{L^3}
  \begin{bmatrix}
  12 & 6L & -12 & 6L \\
  6L & 4L^2 & -6L & 2L^2 \\
  -12 & -6L & 12 & -6L \\
  6L & 2L^2 & -6L & 4L^2
  \end{bmatrix}
  \]


