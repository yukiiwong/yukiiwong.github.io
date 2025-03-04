---
title: "Review of Solid Mechanics I"
date: 2024-03-04
categories: course
tags: 
layout: post
---

## **1. Concept of Stress and Strain**
- **Rigid body** is an idealized model, but in reality, objects **deform under forces**.
- **Stress ( \( \sigma \) )**: Measures the **force per unit area** causing deformation.
- **Strain ( \( \varepsilon \) )**: Measures the **relative deformation** in response to stress.
- **Elastic modulus (Young’s modulus, \( E \) )**: Defines the relationship between stress and strain.

### **Stress in a Prismatic Bar (Under Tension)**
For a prismatic bar with axial force \( P \) and cross-sectional area \( A \):

\[
\sigma = \frac{P}{A}
\]

### **Strain in a Prismatic Bar**
For a bar of original length \( L \) that undergoes elongation \( \delta \):

\[
\varepsilon = \frac{\delta}{L}
\]

**Assumptions:**
1. Uniform deformation.
2. Loads act through the centroid.
3. The material is homogeneous.

---

## **2. Stress-Strain Diagram**
- **Elastic region**: The material returns to its original shape when stress is removed.
- **Plastic region**: Permanent deformation occurs after yielding.
---
- **Proportional limit (A)**: The region where stress and strain are proportional.

In solid mechanics, the **proportional limit** is the region where **stress and strain have a linear relationship**. This follows **Hooke’s Law**, which states:

\[
\sigma = E \varepsilon
\]

where:
- \( \sigma \) = **stress** (force per unit area, measured in Pascals, Pa)
- \( \varepsilon \) = **strain** (dimensionless, ratio of deformation to original length)
- \( E \) = **Young’s modulus** (elastic modulus, measures material stiffness, in Pascals)

- **Young’s modulus** (\( E \)) is a **material property** that defines how much a material deforms under stress.
- A **higher \( E \)** means the material is **stiffer** (harder to deform).
- A **lower \( E \)** means the material is **more flexible**.


For example:
- **Steel has a high \( E \)** → it resists deformation.
- **Rubber has a low \( E \)** → it stretches easily.

- **The proportional limit (Point A) is the point on the stress-strain curve where stress and strain are still proportional.**
- Before reaching this point, the material **fully obeys Hooke’s Law**.
- Beyond this point, the stress-strain relationship **becomes nonlinear**, and permanent deformation may begin.

---


- **Engineering stress**: Uses the original cross-sectional area.
- **True stress**: Uses the updated cross-section.

---

## **3. Linear Elasticity and Hooke’s Law**
### **Hooke’s Law (Axial Loading)**
For an axially loaded member:

\[
\sigma = E \varepsilon
\]

Using force equilibrium and displacement relations:

\[
\delta = \frac{PL}{EA}
\]

where:
- \( E \) = Young’s modulus
- \( A \) = Cross-sectional area
- \( L \) = Length
- \( P \) = Applied load

\[
P = \frac{EA}{L} \delta
\]

which resembles **Hooke’s law for a spring**: \( F = kx \).

# **Derivation and Explanation of Axial Deformation Formula**
When an axial force \( P \) is applied to a prismatic bar (a bar with uniform cross-section), the bar **stretches or compresses**. The amount of elongation or shortening is given by:

\[
\delta = \frac{PL}{EA}
\]

where:
- \( \delta \) = **Axial deformation (elongation or compression)**
- \( P \) = **Axial force applied**
- \( L \) = **Original length of the bar**
- \( E \) = **Young’s modulus (material stiffness)**
- \( A \) = **Cross-sectional area of the bar**

---

## **1. Force Equilibrium and Stress-Strain Relations**
### **(1) Stress Definition**
Stress \( \sigma \) in the bar is given by:

\[
\sigma = \frac{P}{A}
\]

Since **Hooke’s Law** states that stress and strain are proportional in the elastic region:

\[
\sigma = E \varepsilon
\]

where:
- \( \varepsilon \) = strain = relative deformation.

### **(2) Strain Definition**
Strain is defined as:

\[
\varepsilon = \frac{\delta}{L}
\]

Substituting \( \sigma = \frac{P}{A} \) into Hooke’s Law:

\[
\frac{P}{A} = E \varepsilon
\]

Since \( \varepsilon = \frac{\delta}{L} \), we substitute:

\[
\frac{P}{A} = E \frac{\delta}{L}
\]

Rearranging for \( \delta \):

\[
\delta = \frac{PL}{EA}
\]

which is the **axial deformation formula**.

---

## **2. Rearranging the Formula**
The equation can also be rewritten in terms of **force**:

\[
P = \frac{EA}{L} \delta
\]

This equation shows that:
- The **restoring force \( P \)** in an axially loaded bar **acts like a spring**, where the term \( \frac{EA}{L} \) represents the **stiffness** of the bar.
- The form of the equation is similar to **Hooke’s Law** for a spring:

  \[
  F = kx
  \]

  where:
  - \( k = \frac{EA}{L} \) (stiffness of the bar),
  - \( x = \delta \) (displacement),
  - \( F = P \) (applied force).

Thus, an **elastic bar under axial load behaves like a linear elastic spring**.

---

## **3. Interpretation**
### ✅ **What This Equation Tells Us**
- **Larger \( P \) → Larger \( \delta \)**: More force leads to more elongation.
- **Larger \( L \) → Larger \( \delta \)**: Longer bars deform more for the same force.
- **Larger \( E \) or \( A \) → Smaller \( \delta \)**: A **stiffer** material (high \( E \)) or a **thicker bar** (large \( A \)) deforms **less**.

### ❌ **When This Formula Does NOT Work**
- **Material is beyond the elastic limit** (plastic deformation occurs).
- **Cross-section is not uniform** (requires integration).
- **Non-axial loading** (torsion or bending is involved).

---

# **Poisson’s Ratio: Definition, Concept, and Applications**

## **1. What is Poisson’s Ratio?**
When a material is stretched in one direction, it **contracts in the perpendicular directions**. Similarly, when compressed, it **expands laterally**. 

This behavior is quantified by **Poisson’s ratio \( \nu \)**, which is defined as:

\[
\nu = -\frac{\text{Lateral strain}}{\text{Axial strain}}
\]

where:
- **Lateral strain** \( \varepsilon_{\text{lat}} = \frac{\Delta d}{d} \) (change in width/diameter per unit width)
- **Axial strain** \( \varepsilon_{\text{ax}} = \frac{\Delta L}{L} \) (change in length per unit length)

The **negative sign** ensures \( \nu \) is **positive**, since stretching (positive axial strain) causes contraction (negative lateral strain), and vice versa.

---

## **2. Interpretation of Poisson’s Ratio**
- **Higher Poisson’s ratio** (\( \nu \approx 0.5 \)): Material is highly **compressible laterally** (e.g., rubber).
- **Lower Poisson’s ratio** (\( \nu \approx 0 \)): Material shows **almost no lateral change** (e.g., cork).
- **Negative Poisson’s ratio** (\( \nu < 0 \)): The material **expands laterally when stretched**, called an **auxetic material**.

### **Common Values of Poisson’s Ratio**
| **Material** | **Poisson’s Ratio (\( \nu \))** |
|-------------|------------------|
| Rubber | 0.49 - 0.50 |
| Steel | 0.27 - 0.30 |
| Aluminum | 0.33 |
| Concrete | 0.15 - 0.20 |
| Cork | 0.0 (no lateral contraction) |
| Auxetic Materials | Negative \( \nu \) |

---

## **3. Relationship with Elastic Moduli**
Poisson’s ratio connects different **elastic properties** of a material.

### **(1) Shear Modulus and Young’s Modulus**
The **shear modulus** \( G \) (modulus of rigidity) is related to **Young’s modulus** \( E \) by:

\[
G = \frac{E}{2(1+\nu)}
\]

- If \( \nu \) is high, \( G \) is lower → material resists shear deformation **less**.
- If \( \nu \) is low, \( G \) is higher → material resists shear **more**.

### **(2) Bulk Modulus and Young’s Modulus**
The **bulk modulus** \( K \) (resistance to uniform compression) is:

\[
K = \frac{E}{3(1 - 2\nu)}
\]

- If \( \nu \approx 0.5 \), **bulk modulus is very high**, meaning material is **nearly incompressible** (like rubber).
- If \( \nu \approx 0 \), **bulk modulus is smaller**, meaning material **compresses more easily** (like foam or cork).

---

## **4. Physical Meaning of Poisson’s Ratio**
### **(1) Stretching a Rubber Band**
- When you **pull** a rubber band, it **becomes thinner**.
- Rubber has a high Poisson’s ratio (~0.5), meaning it **contracts significantly in width** when stretched.

### **(2) Compressing a Sponge**
- A sponge **compresses easily in all directions**.
- Its Poisson’s ratio is **low**, meaning lateral contraction is minimal.

### **(3) Cork vs. Rubber**
- **Cork** has \( \nu \approx 0 \), meaning it **does not contract laterally**.
- That’s why **wine corks are easy to insert into a bottle**—they don’t expand sideways when pushed in.

---

## **5. Special Case: Auxetic Materials (\( \nu < 0 \))**
- **Auxetic materials expand laterally when stretched** (opposite of normal materials).
- They have applications in **biomechanics, flexible armor, and shock absorption**.
- Example: **Some foams and engineered structures** exhibit negative Poisson’s ratio.

---
# **Shear and Torsion in Solid Mechanics**

## **1. Shear Stress and Shear Strain**
Shear stress occurs when a force is applied **parallel** to a surface rather than **perpendicular** (as in normal stress). This type of stress **deforms** the material by causing adjacent layers to slide over each other.

### **(1) Shear Stress \( \tau \)**
Shear stress is defined as:

\[
\tau = \frac{F}{A}
\]

where:
- \( \tau \) = **Shear stress** (Pa)
- \( F \) = **Applied force parallel to the surface** (N)
- \( A \) = **Area on which the force acts** (m²)

### **(2) Shear Strain \( \gamma \)**
Shear strain is the **deformation due to shear stress**, defined as:

\[
\gamma = \frac{\Delta x}{h} = \tan \theta \approx \theta
\]

where:
- \( \gamma \) = **Shear strain** (dimensionless)
- \( \Delta x \) = **Lateral displacement** (m)
- \( h \) = **Height of the material** (m)
- \( \theta \) = **Angle of deformation in radians**

---

## **2. Hooke’s Law for Shear**
Similar to Hooke’s Law for normal stress, the shear stress-strain relationship is:

\[
\tau = G \gamma
\]

where:
- \( G \) = **Shear modulus (modulus of rigidity)** (Pa)
- \( \gamma \) = **Shear strain**

### **Relationship Between Young’s Modulus \( E \) and Shear Modulus \( G \)**
The **shear modulus \( G \)** is related to **Young’s modulus \( E \)** and **Poisson’s ratio \( \nu \)** by:

\[
G = \frac{E}{2(1 + \nu)}
\]

- If \( G \) is **high**, the material resists shearing (e.g., steel).
- If \( G \) is **low**, the material deforms easily in shear (e.g., rubber).

---



## **3. Torsion in Circular Shafts**
Torsion occurs when a **circular shaft is twisted** due to a torque \( T \). This generates **shear stress** inside the shaft.

### **(1) Shear Strain in Torsion**
The shear strain \( \gamma \) at a distance \( r \) from the center of the shaft is:

\[
\gamma = \frac{\phi r}{L}
\]

where:
- \( \phi \) = **Angle of twist** (radians)
- \( r \) = **Radial distance from the center** (m)
- \( L \) = **Length of the shaft** (m)

### **(2) Shear Stress in Torsion**
Using Hooke’s Law:

\[
\tau = G \gamma
\]

Substituting \( \gamma \):

\[
\tau = G \frac{\phi r}{L}
\]

### **(3) Torque and Polar Moment of Inertia**
The total **torque \( T \)** in the shaft is given by:

\[
T = G I_p \frac{\phi}{L}
\]

where:
- \( I_p \) = **Polar moment of inertia**, which depends on the cross-sectional area:

  \[
  I_p = \int_A r^2 dA
  \]

For a **solid circular shaft** of radius \( R \):

\[
I_p = \frac{\pi R^4}{2}
\]

For a **hollow circular shaft** (outer radius \( R_o \), inner radius \( R_i \)):

\[
I_p = \frac{\pi}{2} (R_o^4 - R_i^4)
\]

---

## **4. Key Insights**
### ✅ **Shear and Torsion in Materials**
- **Shear stress** is caused by **forces parallel** to a surface.
- **Torsion** is caused by **rotational forces** in circular shafts.
- Both follow **Hooke’s Law**, with shear stress proportional to strain.

### ✅ **Material Properties Affect Shear and Torsion**
- **High \( G \) (e.g., steel)** → **Resists shear and torsion**.
- **Low \( G \) (e.g., rubber)** → **Easily deforms under shear forces**.

### ✅ **Torsion Design Considerations**
- **Larger radius \( R \) → Higher resistance to torsion** (\( I_p \propto R^4 \)).
- **Hollow shafts** are more efficient than solid shafts (high strength with less weight).

Understanding **shear stress and torsion** is **essential for designing mechanical components like shafts, gears, and structural beams**! 🚀


## **4. Strain Energy**
### **Stored Energy in an Elastic Bar**
For a bar subjected to axial force \( P \):

\[
U = \int_0^{\delta} P \, d\delta = \frac{1}{2} P \delta
\]

Using \( \delta = \frac{PL}{EA} \):

\[
U = \frac{P^2 L}{2EA}
\]

### **Strain Energy Density**
\[
u = \frac{U}{V} = \frac{1}{2} \sigma \varepsilon
\]

For a bar with volume \( V = AL \):

\[
U = \frac{1}{2} \frac{P^2 L}{EA} = \frac{1}{2} \frac{\sigma^2}{E} A L
\]

---

## **5. Stress Concentration**
- **Stress concentration** occurs due to geometric discontinuities (holes, sharp corners, etc.).
- **Saint-Venant’s principle**: Stresses become uniform at a distance from the load application point.
- **Maximum stress \( \sigma_{\text{max}} \)** is higher than average stress.

\[
\sigma_{\text{max}} = K_t \sigma_{\text{avg}}
\]

where \( K_t \) is the **stress concentration factor**.

---

## **6. Allowable Stress and Factor of Safety**
To prevent failure, we define the **factor of safety (SF)**:

\[
SF = \frac{\text{actual strength}}{\text{required strength}}
\]

For yielding:

\[
SF = \frac{\sigma_y}{\sigma_{\text{actual}}}
\]

where \( \sigma_y \) is the **yield stress**.

### **Design Considerations:**
- **\( SF > 1 \)** ensures safety.
- Higher **\( SF \)** is used for critical structures (e.g., bridges, aircraft).

---

## **7. Summary**
### ✅ **Key Concepts**
1. **Stress and Strain**: Fundamental properties of material deformation.
2. **Hooke’s Law**: Describes linear elasticity.
3. **Poisson’s Ratio**: Relationship between axial and lateral strain.
4. **Strain Energy**: Energy stored in elastic deformation.
5. **Stress Concentration**: Localized stress increase due to discontinuities.
6. **Allowable Stress & Safety Factor**: Ensures safe structural design.
