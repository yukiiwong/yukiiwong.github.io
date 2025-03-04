---
title: "Review of Solid Mechanics II"
date: 2024-03-04
categories: course
tags: 
layout: post
---

## **1. Linear Algebra Review**
### **(1) Systems of Linear Equations**
A linear equation in general form:

\[
a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b
\]

For a system of linear equations:

\[
A X = B
\]

where:
- \( A \) is the **coefficient matrix**,
- \( X \) is the **vector of unknowns**,
- \( B \) is the **vector of constants**.

### **(2) Matrices and Operations**
- **Matrix Addition & Subtraction**: \( A \pm B = [a_{ij} \pm b_{ij}] \)
- **Scalar Multiplication**: \( k A = [k a_{ij}] \)
- **Matrix Multiplication**: \( (AB)_{ij} = \sum_{k=1}^{p} a_{ik} b_{kj} \)

### **(3) Properties of Matrices**
- **Associative Law**: \( A(BC) = (AB)C \)
- **Distributive Law**: \( A(B+C) = AB + AC \)
- **Transpose Properties**:
  - \( (A^T)^T = A \)
  - \( (A+B)^T = A^T + B^T \)
  - \( (AB)^T = B^T A^T \)

### **(4) Determinants and Inverses**
- **Determinant**:

\[
\det(A) = \sum_{i=1}^{n} a_{i1} C_{i1}
\]

where \( C_{ij} \) is the **cofactor**:

\[
C_{ij} = (-1)^{i+j} M_{ij}
\]

- **Inverse of a Matrix**:
  If \( A \) is invertible:

  \[
  A^{-1} = \frac{\text{adj}(A)}{\det(A)}
  \]

  where adj(A) is the **adjugate matrix**.

### **(5) Eigenvalues and Eigenvectors**
For a square matrix \( A \), an **eigenvalue equation** is:

\[
A K = \lambda K
\]

Rearranging:

\[
(A - \lambda I) K = 0
\]

For nontrivial solutions:

\[
\det(A - \lambda I) = 0
\]

which gives the eigenvalues \( \lambda \), and solving for \( K \) gives the **eigenvectors**.

---

## **2. Basics of Stress and Strain**
### **(1) Definition of Stress**
Stress at a point is defined as:

\[
\sigma = \lim_{\Delta A \to 0} \frac{\Delta F}{\Delta A}
\]

### **(2) Stress Components**
For an infinitesimal volume:

\[
\mathbf{\sigma} =
\begin{bmatrix}
\sigma_{xx} & \sigma_{xy} & \sigma_{xz} \\
\sigma_{yx} & \sigma_{yy} & \sigma_{yz} \\
\sigma_{zx} & \sigma_{zy} & \sigma_{zz}
\end{bmatrix}
\]

where:
- \( \sigma_{xx}, \sigma_{yy}, \sigma_{zz} \) are **normal stresses**.
- \( \sigma_{xy}, \sigma_{xz}, \sigma_{yz} \) are **shear stresses**.

From moment equilibrium:

\[
\sigma_{xy} = \sigma_{yx}, \quad \sigma_{xz} = \sigma_{zx}, \quad \sigma_{yz} = \sigma_{zy}
\]

### **(3) Stress Transformation**
For a rotated coordinate system:

\[
\sigma_P = \sigma N
\]

where \( N \) is the unit normal vector.

---

## **3. Principal Stresses and Invariants**
### **(1) Principal Stresses**
Principal stresses occur on **planes with no shear stress**.

Solving:

\[
\det(\sigma - \lambda I) = 0
\]

yields **principal stresses** \( \sigma_1, \sigma_2, \sigma_3 \).

### **(2) Stress Invariants**
Stress tensor properties **do not change** with coordinate system rotations:

\[
I_1 = \sigma_{xx} + \sigma_{yy} + \sigma_{zz}
\]

\[
I_2 = \sigma_{xx} \sigma_{yy} + \sigma_{yy} \sigma_{zz} + \sigma_{zz} \sigma_{xx} - \sigma_{xy}^2 - \sigma_{yz}^2 - \sigma_{zx}^2
\]

\[
I_3 = \det(\sigma)
\]

---

## **4. First Law of Thermodynamics in Solid Mechanics**
### **(1) Energy Balance**
\[
\delta W + \delta H = \delta U + \delta K
\]

where:
- \( W \) = work done by external forces.
- \( H \) = heat transfer.
- \( U \) = internal energy.
- \( K \) = kinetic energy.

For **static equilibrium** and **adiabatic conditions**:

\[
\delta W = \delta U
\]

### **(2) Work Done by Stresses**
Using the **divergence theorem**:

\[
\delta W = \int_V \sigma_{ij} \delta \varepsilon_{ij} \, dV
\]

Internal energy per unit volume:

\[
\delta U_0 = \frac{1}{2} (\sigma_{xx} \delta \varepsilon_{xx} + \sigma_{yy} \delta \varepsilon_{yy} + \sigma_{zz} \delta \varepsilon_{zz} + 2\sigma_{xy} \delta \varepsilon_{xy} + 2\sigma_{yz} \delta \varepsilon_{yz} + 2\sigma_{zx} \delta \varepsilon_{zx})
\]

---

## **5. Hooke’s Law for Isotropic Elasticity**
For an **isotropic** material (same properties in all directions), Hooke’s law is:

\[
\varepsilon_{xx} = \frac{1}{E} (\sigma_{xx} - \nu (\sigma_{yy} + \sigma_{zz}))
\]

\[
\varepsilon_{yy} = \frac{1}{E} (\sigma_{yy} - \nu (\sigma_{xx} + \sigma_{zz}))
\]

\[
\varepsilon_{zz} = \frac{1}{E} (\sigma_{zz} - \nu (\sigma_{xx} + \sigma_{yy}))
\]

where:
- \( E \) = Young’s modulus.
- \( \nu \) = Poisson’s ratio.

For **shear stress**:

\[
\gamma_{xy} = \frac{\tau_{xy}}{G}, \quad \gamma_{xz} = \frac{\tau_{xz}}{G}, \quad \gamma_{yz} = \frac{\tau_{yz}}{G}
\]

where \( G \) is the **shear modulus**:

\[
G = \frac{E}{2(1+\nu)}
\]

---

## **6. Von Mises Stress**
To determine **failure under multiaxial loading**, we use the **von Mises stress**:

\[
\sigma_e = \sqrt{\frac{1}{2} \left( (\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2 \right)}
\]

For stress components:

\[
\sigma_e = \sqrt{\frac{1}{2} \left( (\sigma_{xx} - \sigma_{yy})^2 + (\sigma_{yy} - \sigma_{zz})^2 + (\sigma_{zz} - \sigma_{xx})^2 + 6(\sigma_{xy}^2 + \sigma_{yz}^2 + \sigma_{zx}^2) \right)}
\]

---

## **7. Summary**
### ✅ **Key Topics**
- **Linear Algebra Review**: Matrices, determinants, eigenvalues.
- **Stress and Strain Basics**: Stress tensors, transformation.
- **Principal Stresses and Invariants**: Coordinate-independent properties.
- **First Law of Thermodynamics**: Work-energy relation in solids.
- **Hooke’s Law for Isotropic Materials**: Linear elasticity.
- **Von Mises Stress**: Failure criterion for materials.