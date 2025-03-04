---
title: "Basic Concepts: PDF and CDF"
date: 2020-02-28
categories: knowledge
tags: 
layout: post
---

## **1. Probability Density Function (PDF)**
### **Definition**
The **Probability Density Function (PDF)** describes how **likely** a continuous random variable \( X \) takes on a specific value.

For a random variable \( X \), the PDF is denoted as:

\[
f(x) = \frac{d}{dx} F(x)
\]

where \( F(x) \) is the **Cumulative Distribution Function (CDF)**.

### **Key Properties of PDF**
1. **Non-negativity**: \( f(x) \geq 0 \) for all \( x \).
2. **Total area under the curve is 1**:

   \[
   \int_{-\infty}^{\infty} f(x) dx = 1
   \]

3. **It does not directly give probability** of a single value, but rather how densely probability is distributed.

### **Example: Normal Distribution PDF**
For a **normal distribution** \( X \sim N(\mu, \sigma^2) \), the PDF is:

\[
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)
\]

- \( \mu \) = mean (center of the distribution).
- \( \sigma \) = standard deviation (spread of data).

#### **Visual Interpretation**
- The PDF graph shows **where values are most likely** to occur.
- In a normal distribution, the peak is at \( x = \mu \) (mean), and probability decreases as you move away.

---

## **2. Cumulative Distribution Function (CDF)**
### **Definition**
The **Cumulative Distribution Function (CDF)** gives the probability that a random variable \( X \) takes on a value **less than or equal to \( x \)**:

\[
F(x) = P(X \leq x) = \int_{-\infty}^{x} f(t) dt
\]

### **Key Properties of CDF**
1. **Monotonic increasing**: \( 0 \leq F(x) \leq 1 \).
2. **Limits**:
   - \( F(-\infty) = 0 \) (probability is 0 before any values occur).
   - \( F(\infty) = 1 \) (eventually, all probability accumulates to 1).
3. **Deriving PDF from CDF**: 
   - The PDF is the **derivative** of the CDF:  
     \[
     f(x) = \frac{d}{dx} F(x)
     \]

### **Example: Normal Distribution CDF**
For a normal distribution \( X \sim N(\mu, \sigma^2) \), the CDF is:

\[
F(x) = \frac{1}{2} \left[1 + \text{erf} \left(\frac{x - \mu}{\sqrt{2\sigma^2}} \right) \right]
\]

where **erf()** is the error function.

---

## Relationship Between PDF and CDF
| Concept | Probability Density Function (PDF) | Cumulative Distribution Function (CDF) |
|---------|--------------------------------|--------------------------------|
| **Definition** | Describes probability *density* at a point \( x \). | Gives probability that \( X \) is **less than or equal to** \( x \). |
| **Mathematical Relation** | \( f(x) = \frac{d}{dx} F(x) \) | \( F(x) = \int_{-\infty}^{x} f(t) dt \) |
| **Graph Shape** | Bell-shaped for normal distributions, can vary for others. | Always **monotonically increasing** from 0 to 1. |
| **Use Case** | Helps understand the most likely values. | Helps compute probabilities of intervals. |


---

## **5. Why Are PDF and CDF Important?**
- **PDF is useful for modeling distributions** and determining the likelihood of specific values.
- **CDF is essential for probability calculations**, such as:
  - **Finding the probability of intervals**: \( P(a \leq X \leq b) = F(b) - F(a) \).
  - **Setting percentiles**: The median is where \( F(x) = 0.5 \).

Understanding **PDF and CDF** is fundamental in **Extreme Value Theory (EVT)** since:
- **PDF helps model how extreme values are distributed** (e.g., tail behavior).
- **CDF helps compute exceedance probabilities**, which are critical in **risk assessment** (e.g., probability of a flood exceeding a certain height).

By mastering these concepts, you build a strong foundation for working with **probability distributions, EVT, and GPD modeling**!