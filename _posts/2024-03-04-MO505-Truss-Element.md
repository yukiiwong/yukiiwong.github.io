---
title: "Truss Element in FEM"
date: 2025-03-17
categories: course
tags:
layout: post
---

## **1. Truss vs. Beam (1-D Elements)**

| **Truss**                         | **Beam**                        |
|-----------------------------------|---------------------------------|
| Supports only **axial loads**     | Supports **axial and bending** loads |
| No bending moments                | Bending moments present         |
| Discussed in **Lecture 5**        | Discussed in **Lecture 6**      |

---

## **2. General Procedure of FEM (Finite Element Method)**

1. **Domain discretization**: Divide the domain into small, simple elements.
2. **Field interpolation**: Approximate field quantities (displacements, etc.) within each element using interpolation functions (polynomials).
3. **DOF (Degrees of Freedom)**: Nodes at element boundaries share DOFs to ensure continuity.
4. **Element equations**: Derive algebraic equations for each element:  
   \[
   [K^E] \{u^E\} = \{F^E\}
   \]
5. **Global assembly**: Assemble the **element equations** into the **global system**.

---

## **3. Shape Function for Truss Elements**

### **3-D Truss Elements**
- Displacement field components:  
  \[
  u(x, y, z), v(x, y, z), w(x, y, z)
  \]  
- They are functions of nodal displacements at nodes \(1\) and \(2\):  
  \[
  (u_1, v_1, w_1), (u_2, v_2, w_2)
  \]

### **1-D Truss Element Displacement Field**  
- **Linear interpolation**:  
  \[
  u(x) = N_1(x) u_1 + N_2(x) u_2
  \]  
- Shape functions:  
  \[
  N_1(x) = \frac{L - x}{L}, \quad N_2(x) = \frac{x}{L}
  \]  
- In matrix form:  
  \[
  u(x) = [N_1 \quad N_2] \begin{Bmatrix} u_1 \\ u_2 \end{Bmatrix}
  \]

---

## **4. Strain in 1-D Truss Element**

- Strain-displacement relationship:  
  \[
  \varepsilon_x = \frac{du}{dx}
  \]  
- Strain-displacement matrix \( [B] \):  
  \[
  \varepsilon = [B] \begin{Bmatrix} u_1 \\ u_2 \end{Bmatrix}
  \]  
  where  
  \[
  [B] = \begin{bmatrix} -\frac{1}{L} & \frac{1}{L} \end{bmatrix}
  \]

---

## **5. Stress in 1-D Truss Element**

- Hooke's Law:  
  \[
  \sigma_x = E \varepsilon_x
  \]  
- Stress in terms of nodal displacements:  
  \[
  \sigma_x = E [B] \begin{Bmatrix} u_1 \\ u_2 \end{Bmatrix}
  \]

---

## **6. Stiffness Matrix for 1-D Truss Element**

- Strain energy:  
  \[
  U = \frac{1}{2} \varepsilon^T E \varepsilon \cdot V
  \]  
- Stiffness matrix expression:  
  \[
  [k^E] = \int_V B^T E B \, dV
  \]  
- For 1-D truss (constant cross-section \(A\)):  
  \[
  [k^E] = \frac{AE}{L} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}
  \]

---

## **7. Global Stiffness Matrix Assembly**

### **Procedure**
1. **Expand** element matrices to match **global DOFs**.
2. **Assemble** by summing contributions of overlapping nodes.

### **Example: Two Bar Elements**
- Element 1 (Nodes 1-2):  
  \[
  \begin{bmatrix} a & b \\ c & d \end{bmatrix}
  \]  
- Element 2 (Nodes 2-3):  
  \[
  \begin{bmatrix} e & f \\ g & h \end{bmatrix}
  \]  
- Global assembly results in:  
  \[
  [K] = \begin{bmatrix} a & b & 0 \\ c & d + e & f \\ 0 & g & h \end{bmatrix}
  \]

---

## **8. FEA by Hand (1-D Truss Example)**

### **Steps**
1. Obtain stiffness matrices for **each element**.
2. Expand and assemble into the **global stiffness matrix** \([K]\).
3. Apply **boundary conditions** and known forces.
4. Solve \([K]\{u\} = \{F\}\) for nodal displacements \(\{u\}\).
5. Compute **strain** and **stress**:
   - Strain:  
     \[
     \varepsilon = [B] \{u\}
     \]
   - Stress:  
     \[
     \sigma = E \varepsilon
     \]

---

### **Example Results (Given Parameters)**  
- \(L = 2 m\), \(E = 210 GPa\), \(A = 1 cm^2\), \(P = 1000 N\)

#### **Displacements**
\[
u_1 = 0, \quad u_2 = 9.52 \times 10^{-5} m, \quad u_3 = 2.86 \times 10^{-5} m
\]

#### **Strains**
\[
\varepsilon_1 = 4.76 \times 10^{-5}, \quad \varepsilon_2 = 9.52 \times 10^{-5}
\]

#### **Stresses**
\[
\sigma_1 = 1.00 \times 10^7 N/m^2, \quad \sigma_2 = 2.00 \times 10^7 N/m^2
\]

---

## **9. Summary**

✅ **Key Concepts**
1. Truss elements only support **axial** loads.  
2. Displacement field is **linearly interpolated** using shape functions.  
3. **Strain and stress** derive from displacement gradients.  
4. **Stiffness matrix** derived from energy methods and assembled globally.  
5. Manual FEA steps emphasize the **importance of assembly and boundary conditions**.
