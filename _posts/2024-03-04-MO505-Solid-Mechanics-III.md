---
title: "Review of Solid Mechanics III"
date: 2025-03-17
categories: course
tags:
layout: post
---

## **1. Introduction to Bending**

- **Beam**  
  - A structural member subjected to **loads acting laterally** to its **longitudinal axis**.  
  - Compare with **truss** structures that primarily carry axial loads.

- **Pure Bending**  
  - Bending moment \( M \) is **constant**.  
  - Shear force \( Q \) is **zero**.

---

## **2. Strains in Beams**

### **Curvature and Geometry**
- **Curvature** \( \kappa \):  
  \[
  \kappa = \frac{1}{\rho}
  \]  
  where \( \rho \) is the **radius of curvature**.

- For small deflections:  
  \[
  \frac{d\theta}{dx} = \kappa
  \]  
  \( \theta \): slope or angle of rotation of the beam.

---

### **Axial (Normal) Strains**
- **Assumption** (Euler-Bernoulli beam theory):  
  Cross-sections remain **plane** and **perpendicular** to longitudinal axis after deformation.

- **Tension**: Upper part of the beam.  
- **Compression**: Lower part of the beam.  
- **Neutral Surface**: No change in length.

- **Axial strain \( \varepsilon_x \)**:  
  \[
  \varepsilon_x = -y \kappa
  \]  
  where \( y \): distance from the neutral axis.

---

## **3. Stresses in Beams**

### **Axial (Normal) Stress**
- Hooke’s Law for beams:  
  \[
  \sigma_x = E \varepsilon_x = -E y \kappa
  \]

- **Tensile stress** (positive) and **compressive stress** (negative) depend on \( y \).

---

### **Transverse Strains**
- Poisson effect introduces transverse strains:  
  \[
  \varepsilon_z = -\nu \varepsilon_x = \nu y \kappa
  \]

---

## **4. Force and Moment Equilibrium in Pure Bending**

- **Resultant axial force** is zero:  
  \[
  \int_A \sigma_x \, dA = 0
  \]

- **Resultant moment** about neutral axis:  
  \[
  M = \int_A \sigma_x y \, dA = -E \kappa \int_A y^2 dA = -E \kappa I
  \]

- **Stress distribution**:  
  \[
  \sigma_x = -\frac{M}{I} y
  \]

- Maximum stress occurs at the largest \( |y| \):  
  \[
  \sigma_{max} = \frac{M y_{max}}{I}
  \]

---

## **5. Beams with Axial Loads**

- **Combined axial force \( N \)** and bending moment \( M \)**:  
  \[
  \sigma = \frac{N}{A} + \frac{M y}{I}
  \]

---

### **Eccentric Axial Loads**
- Axial force \( P \) applied at a distance \( e \):  
  \[
  \sigma = \frac{P}{A} + \frac{P e y}{I}
  \]

- Statically equivalent to a **centrally applied force** plus a **moment** \( Pe \).

---

## **6. Deflections of Beams**

### **Basic Geometry**
- \( \kappa = \frac{d\theta}{dx} = \frac{d^2 v}{dx^2} \)  
- Slope \( \theta \approx \tan \theta = \frac{dv}{dx} \)

---

### **Differential Equations of the Deflection Curve**
- Curvature relates to moment:  
  \[
  \kappa = \frac{M}{EI}
  \]  
  Therefore:  
  \[
  \frac{d^2 v}{dx^2} = \frac{M}{EI}
  \]  
  And further:  
  \[
  \frac{d^3 v}{dx^3} = \frac{V}{EI}
  \]  
  \[
  \frac{d^4 v}{dx^4} = \frac{q}{EI}
  \]

---

### **Example Exercise**
- Simply supported beam under **uniform load** \( q \):  
  - Moment equation:  
    \[
    M(x) = -\frac{q}{2}(Lx - x^2)
    \]  
  - Deflection equation:  
    \[
    v(x) = \frac{q}{24 EI} (x^4 - 2L x^3 + L^2 x^2)
    \]  
  - Maximum deflection at \( x = \frac{L}{2} \).

---

## **7. Plane Stress vs. Plane Strain**

|                 | Plane Stress                              | Plane Strain                              |
|-----------------|-------------------------------------------|-------------------------------------------|
| Stress          | \( \sigma_{zz} = 0 \)                    | \( \varepsilon_{zz} = 0 \)               |
| Applicable to   | Thin plates                              | Long structures constrained in \( z \)-dir |
| Constitutive Eq | \( \varepsilon_{zz} = -\frac{\nu}{E}(\sigma_{xx} + \sigma_{yy}) \) | \( \sigma_{zz} = \nu(\sigma_{xx} + \sigma_{yy}) \) |

---

## **8. Summary**

### ✅ **Key Points**
1. Strains and stresses in beams under bending.  
2. Equilibrium conditions for pure bending.  
3. Deflection curves and equations.  
4. Difference between plane stress and plane strain conditions.

---

## **9. Preview of Next Topics**

- **FEM (Finite Element Method)** for structural analysis.  
- Real-world applications:  
  - Complex geometries and loading conditions.  
  - Use of computational tools (PCs, supercomputers).

---