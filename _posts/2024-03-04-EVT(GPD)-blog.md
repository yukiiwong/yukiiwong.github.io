---
title: "Extreme Value Theory (EVT) and Generalized Pareto Distribution (GPD)"
date: 2024-03-04
categories: research
tags: Extreme Value Theory (EVT), Generalized Pareto Distribution (GPD)
layout: post
---

# Extreme Value Theory (EVT) and Generalized Pareto Distribution (GPD)
## Introduction to Extreme Value Theory (EVT)
Extreme Value Theory (EVT) is a statistical approach used to analyze **extreme events** in datasets. Unlike traditional statistics that focus on the entire distribution, EVT specifically models **the tail behavior** of a distribution, which is essential in fields like finance, meteorology, and autonomous driving safety. EVT is a mathematical theory specifically designed for modeling and analyzing extreme values in data, deriving their statistical distribution, and making reasonable predictions about future extreme events.

---

## Generalized Pareto Distribution (GPD)
The **Generalized Pareto Distribution (GPD)** is a core component of EVT. It models the distribution of exceedances \( Y \) beyond a given threshold \( u \):

\[
Y = X - u \quad \text{for} \quad X > u
\]

### GPD Probability Distribution Function
The cumulative distribution function (CDF) of GPD is given by:

\[
F(y) = 1 - \left(1 + \xi \frac{y}{\sigma} \right)^{-\frac{1}{\xi}}, \quad y > 0
\]

where:
- \( \xi \) (Shape parameter): Determines the **tail heaviness**.
  - \( \xi > 0 \) → **Heavy-tailed** (e.g., Pareto distribution).
  - \( \xi = 0 \) → **Exponential distribution** (light tail).
  - \( \xi < 0 \) → **Short-tailed** (bounded distribution, e.g., Weibull).
- \( \sigma \) (Scale parameter): Defines the **spread** of exceedances.
- \( y \) is the exceedance (\( X - u \)), meaning values above the threshold.

The shape parameter \( \xi \) is crucial as it defines the **tail behavior** of the extreme values:

1. **Heavy-tailed (\( \xi > 0 \))**:
   - The tail is **long and heavy**.
   - Represents **catastrophic or extreme events** with **large exceedances**.
   - Common in **financial risks, insurance claims, and traffic accidents**.

2. **Exponential decay (\( \xi = 0 \))**:
   - The distribution resembles an **exponential distribution**.
   - Frequently appears in **queueing theory and reliability analysis**.

3. **Short-tailed (\( \xi < 0 \))**:
   - The distribution has a **finite maximum value**.
   - Often seen in **natural processes with strict physical limits** (e.g., rainfall amounts).
### Why GPD for POT?
According to **Pickands-Balkema-de Haan Theorem**:

\[
\lim_{u \to u_{max}} P(Y \leq y | X > u) = G(y; \xi, \sigma)
\]

This means that for a **sufficiently high threshold \( u \)**, the exceedances approximately follow a GPD. 

**Choosing the correct threshold \( u \) is crucial**:
- Too **low**: Includes non-extreme values, making the GPD model inaccurate.
- Too **high**: Reduces the sample size, leading to unstable parameter estimation.


####  What Does This Theorem Mean?
Suppose we have a dataset of some variable \( X \) (e.g., daily rainfall, stock price drops, Time-To-Collision in autonomous driving).
- We select a high threshold \( u \), and look at all values that exceed \( u \), which we define as:

  \[
  Y = X - u \quad \text{for} \quad X > u
  \]

- This means \( Y \) represents **how much larger** an extreme event is beyond \( u \).

- The theorem states that **for a sufficiently high threshold \( u \), the exceedances \( Y \) follow a GPD, regardless of the original distribution of \( X \).**  
  - This is a **remarkable result** because it means that **GPD is a universal model** for extreme events across many fields (finance, meteorology, traffic safety, etc.).



---

## Relationship Between GPD and POT Threshold \( u \)
### Steps in the POT Method
1. Choose an appropriate threshold \( u \).
2. Extract all values \( X > u \).
3. Compute the exceedances \( Y = X - u \).
4. Fit the **Generalized Pareto Distribution (GPD)** to \( Y \).
5. Estimate the **shape parameter \( \xi \) and scale parameter \( \sigma \)**.

### Threshold Selection Methods
Some common methods for selecting \( u \):
- **Mean Residual Life (MRL) Plot**: Identifies the point where exceedance mean remains linear.
- **Parameter Stability Analysis**: Checks the consistency of GPD parameter estimates over different thresholds.

---

## AIC and BIC in GPD Model Selection
When fitting the GPD model using **Maximum Likelihood Estimation (MLE)**, we evaluate model quality using **AIC and BIC**.

### Akaike Information Criterion (AIC)
\[
AIC = 2k - 2\ln L
\]
where:
- \( k \) is the number of parameters (2 for GPD: \( \xi, \sigma \)).
- \( L \) is the **log-likelihood function**.

### Bayesian Information Criterion (BIC)
\[
BIC = k \ln n - 2\ln L
\]
where:
- \( n \) is the sample size.

Both AIC and BIC are used to compare models:
- **Lower values indicate better models**.
- AIC prefers a good fit, while BIC penalizes excessive parameters more strictly.

In the code:
```python
log_likelihood = -neg_log_likelihood(result.x)
num_params = 2  # shape and scale parameters
n = len(exceedances)
aic = 2 * num_params - 2 * log_likelihood
bic = np.log(n) * num_params - 2 * log_likelihood