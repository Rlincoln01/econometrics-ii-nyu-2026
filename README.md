# Econometrics II @ NYU — Spring 2026

This is the repository for **Econometrics II** (PhD), covering **Time Series** (first half) and **Panel Data** (second half).

| Half   | Topic       | Instructor                                              |
|--------|-------------|---------------------------------------------------------|
| First  | Time Series | Tim Cogley (`tim.cogley@nyu.edu`)                       |
| Second | Panel Data  | Martín Almuzara (`martin.almuzara@ny.frb.org`)          |

- **TA**: Rafael Lincoln (`rafael.lincoln@nyu.edu`)

## Why Should You Take This Class?

First of all, it's a mandatory class. But let's set that aside...

Most applied economics research relies on data observed either over time (time series) or across individuals/firms tracked repeatedly (panel data). Both data structures are ubiquitous in fields like **Macroeconomics**, **Finance**, **Labor Economics**, **Industrial Organization**, **Development Economics**, and **Health Economics**. Mastering time series and panel data methods is essential for anyone doing empirical work in economics.

By the end of the course, you will be able to:

- Understand the Wold representation, ARMA processes, and state-space models;
- Implement Maximum Likelihood and GMM estimation for time series models;
- Work with VARs: forecasting, Granger causality, impulse responses, and identification;
- Understand unit roots, cointegration, and their implications for macroeconomic data;
- Handle panel data with fixed effects and random effects, including dynamic panels;
- Estimate nonlinear panel models (logits, quantiles, grouped heterogeneity);
- Work with matched employer-employee data and methods combining macro and micro data.

## Topics

A tentative schedule is below. Note: The Time Series syllabus is from **Spring 2025** (reference until 2026 is available); the Panel Data syllabus is **Spring 2026**.

### Part I: Time Series (Tim Cogley)

| Week | Topics |
|------|--------|
| Week 1 | Time Domain Representations: Stationarity, Wold representation, ARMA processes |
| Week 2 | Maximum Likelihood Estimation: Prediction-error decomposition, Kalman filter |
| Week 3 | Reduced-form VARs: Forecasting, Granger causality, variance decompositions |
| Week 4 | Identified VARs + DSGE Models: Structural identification, Bayesian estimation |
| Week 5 | Unit Roots and Cointegration: Beveridge-Nelson, Granger representation theorem |
| Week 6 | GMM: Conditional moment restrictions, Hansen-Singleton, HAC estimation |

### Part II: Panel Data (Martín Almuzara)

| Week | Topics |
|------|--------|
| Week 7 | Introduction: Why panel data? GMM refresher, simulated methods |
| Week 8 | Linear Panel Models: Fixed effects vs random effects, random coefficients |
| Week 9 | Dynamic Panels: Fixed-T biases, Arellano-Bond |
| Week 10 | Nonlinear Panel Models: Logits, mixtures, quantiles |
| Week 11 | Large-T Asymptotics: Incidental parameters, bias reduction |
| Week 12 | Beyond Panel Data: Bipartite networks, matched datasets, macro+micro |

## Books and Readings

Lecture slides will be posted to this repository. All books and papers can be accessed through the **NYU Library online**.

### Time Series — Textbooks

| Book | Reference |
|------|-----------|
| **Main** | Hamilton, J. (1994): *Time Series Analysis*. Princeton University Press. |
| **Supplementary** | Harvey, A. (1993): *Time Series Models* (2nd ed.). MIT Press. *(Out of print; used copies available.)* |

### Time Series — Readings by Topic

Required readings are marked with **(\*)**.

| Topic | Textbook Chapters | Papers |
|-------|-------------------|--------|
| **Time Domain Representations** | **(\*)** Hamilton, chs. 2–3, 10.1–10.3 | Harvey, ch. 2 |
| **Maximum Likelihood Estimation** | **(\*)** Hamilton, chs. 5, 7, 13 | Harvey, chs. 4–5 |
| **Reduced-form VARs** | **(\*)** Hamilton, ch. 11 | Campbell & Shiller (1987), *Cointegration and Tests of Present-Value Models*; Cochrane (1991), *Explaining the variance of price-dividend ratios*; Cochrane (1994), *Permanent and transitory components of GNP and Stock Prices*; Rotemberg & Woodford (1996), *Real-Business-Cycle Models and Forecastable Movements*; Cochrane (2022), *The Fiscal Roots of Inflation* |
| **DSGE Models** | **(\*)** Hamilton, ch. 12 | — |
| **Identified VARs** | — | Blanchard & Quah (1989), *Dynamic Effects of Aggregate Supply and Demand Shocks*; Cogley & Nason (1995), *Output Dynamics in Real-Business-Cycle Models*; Kehoe (2006), *How to Advance Theory with Structural VARs* |
| **Unit Roots & Cointegration** | **(\*)** Hamilton, chs. 15, 17, 19, 20 | Nelson & Plosser (1982), *Trends and Random Walks in Macroeconomic Time Series*; Stock (1991), *Confidence Intervals for the Largest Autoregressive Root*; King, Plosser, Stock & Watson (1991), *Stochastic trends and economic fluctuations* |
| **GMM** | **(\*)** Hamilton, ch. 14 | **(\*)** Hansen & Singleton (1982), *Generalized instrumental variables estimation of nonlinear rational expectations models*; **(\*)** Hansen (1982), *Large Sample Properties of GMM Estimators*; Hansen & Jagannathan (1997), *Assessing specification errors in stochastic discount factor models* |
| **Frequency Domain** *(time permitting)* | **(\*)** Hamilton, chs. 6, 10.4–10.5 | Harvey, ch. 3; Baxter & King (1999), *Measuring Business Cycles: Approximate Bandpass Filters*; Cogley (2006), *Data Filters*; Hamilton (2018), *Why You Should Never Use the Hodrick-Prescott Filter* |

---

### Panel Data — Textbooks

| Book | Reference |
|------|-----------|
| **Recommended** | Arellano, M. (2003): *Panel Data Econometrics*. Oxford University Press. |
| **Recommended** | Wooldridge, J. (2010): *Econometric Analysis of Cross Section and Panel Data*. MIT Press. |

### Panel Data — Readings by Topic

All readings are optional but useful for deeper understanding.

#### 1. Introduction

| Subtopic | Papers |
|----------|--------|
| **Foundations** | Chamberlain (1984), *Panel Data* (Handbook of Econometrics) |
| **GMM & Simulated Methods** | Gourieroux, Phillips & Yu (2010), *Indirect inference for dynamic panel models* |

#### 2. Linear Panel Data Models

| Subtopic | Papers |
|----------|--------|
| **Static: FE vs RE** | Chamberlain (1984), *Panel Data* |
| **Random Coefficients** | Browning, Ejrnaes & Alvarez (2010), *Modelling income processes with lots of heterogeneity* |
| **Dynamic Models / Fixed-T Bias** | Arellano & Bond (1991), *Some Tests of Specification for Panel Data*; Hahn & Kuersteiner (2002), *Asymptotically unbiased inference for a dynamic panel model* |
| **Large-T** | Hansen (2007), *Asymptotic properties of a robust variance matrix estimator for panel data when T is large*; Moon & Weidner (2015), *Linear regression for panel with unknown number of factors as interactive fixed effects* |

#### 3. Nonlinear Panel Data Models

| Subtopic | Papers |
|----------|--------|
| **Fixed-T: Logits** | Honoré & Kyriazidou (2000), *Panel data discrete choice models with lagged dependent variables*; Honoré & Lewbel (2002), *Semiparametric binary choice panel data models*; Chamberlain (2010), *Binary response models for panel data* |
| **Fixed-T: Mixtures & Quantiles** | Arellano, Blundell & Bonhomme (2017), *Earnings and consumption dynamics: a nonlinear panel data framework*; Belloni et al. (2019), *Conditional quantile processes*; Gu & Volgushev (2019), *Panel data quantile regression with grouped fixed effects* |
| **Large-T: Incidental Parameters & Bias Reduction** | Hahn & Newey (2004), *Jackknife and analytical bias reduction for nonlinear panel models*; Arellano & Bonhomme (2009), *Robust priors in nonlinear panel data models*; Arellano & Bonhomme (2011), *Nonlinear panel data analysis*; Fernández-Val & Lee (2013), *Panel data models with nonadditive unobserved heterogeneity*; Fernández-Val & Weidner (2016, 2018), *Individual and time effects in nonlinear panel models* |
| **Grouped/Discretized Heterogeneity** | Bonhomme & Manresa (2015), *Grouped patterns of heterogeneity in panel data*; Bonhomme, Lamadon & Manresa (2022), *Discretizing unobserved heterogeneity*; Ando & Bai (2016), *Panel data models with grouped factor structure*; Su, Shi & Phillips, *Identifying Latent Structures in Panel Data*; Hahn & Moon (2010), *Panel data models with finite number of multiple equilibria* |

#### 4. Beyond Panel Data

| Subtopic | Papers |
|----------|--------|
| **Bipartite Networks & Matched Data** | Abowd, Kramarz & Margolis (1999), *High wage workers and high wage firms*; Abowd, McKinney & Schmutte (2019), *Modeling endogenous mobility*; Andrews et al. (2008), *High wage workers and low wage firms*; Bonhomme, Lamadon & Manresa (2019), *A distributional framework for matched employer-employee data*; Jochmans & Weidner (2019), *Fixed-Effect Regressions on Network Data*; Kline, Saggio & Sølvsten (2020), *Leave-out estimation of variance components*; Woodcock (2008), *Wage differentials in the presence of unobserved worker, firm, and match heterogeneity*; Lachowska et al. (2022), *Do firm effects drift?* |
| **Network Theory** | Bonhomme (2020), *Econometric analysis of bipartite networks*; Kranton & Minehart (2001), *A theory of buyer-seller networks*; Gao, Lu & Zhou (2015), *Rate-optimal graphon estimation*; Lei & Rinaldo (2015), *Consistency of spectral clustering in stochastic block models* |
| **Combining Macro & Micro** | Finkelstein, Gentzkow & Williams (2016), *Sources of geographic variation in health care*; Freyaldenhoven, Hansen & Shapiro (2019), *Pre-event trends in the panel event-study design*; Rambachan & Roth (2019), *An honest approach to parallel trends* |

#### Additional References

| Topic | Papers |
|-------|--------|
| **High-Dimensional Panels** | Belloni et al. (2016), *Inference in high-dimensional panel models* |
| **Dynamic Models with Unobservables** | Hu & Shum (2012), *Nonparametric identification of dynamic models with unobserved state variables* |
| **Production Functions** | Levinsohn & Petrin (2003), *Estimating production functions using inputs to control for unobservables*; Doraszelski & Jaumandreu (2013), *R&D and productivity: Estimating endogenous productivity* |
| **Clustering Methods** | Vogt & Linton (2020), *Multiscale clustering of nonparametric regression curves*; Pollard (1982), *A central limit theorem for k-means clustering* |

## Administrative Stuff

### TA Sessions

Rafael will host **weekly TA sessions**. These sessions are your opportunity to:
- Go through common mistakes on problem sets;
- Discuss specific issues from your own study time;
- Work through extra problems and practice questions.

It is good etiquette to email Rafael beforehand about specific doubts you'd like covered during the session.

### Office Hours

- **Instructors**: By appointment (email to schedule).
- **TA**: Office hours TBD. Email Rafael if you have questions or want to schedule a meeting.

### Attendance

There is no mandatory attendance policy. However, coming to class and TA sessions will significantly help your understanding of the material.

## Evaluation

### Time Series (First Half)

- Your grade will be based on a **midterm exam** (date TBD).
- The exam is **closed book** — no notes or electronic devices allowed.
- Practice problems will be posted but are **optional and not graded**.

### Panel Data (Second Half)

- **Problem sets** (50% of grade): Assigned throughout the half. Collaboration is encouraged, but answers and code must be typed up independently. Problem sets are graded coarsely (full score for demonstrated effort and thoughtfulness).
- **Project presentation** (50% of grade): Instead of an exam, students present a project in the final week. May be original work or an in-depth critical assessment of an existing paper. Groups of two allowed. Topic requires prior approval from the instructor.

## Problem Set Logistics

### Weekly Handouts (TA Sessions)

In each weekly TA session, Rafael will distribute **practice problem handouts** and solve them during the session. These are **not mandatory** and are meant to reinforce lecture material.

### Part I: Time Series

Problem sets during the Time Series half are **optional and not graded**. They are old exam questions and practice problems to help you prepare for the midterm. Solutions will be discussed during recitation.

### Part II: Panel Data

Problem sets are **mandatory** and count toward your grade (50%). Key rules:
- Students may collaborate, but answers and code must be typed up independently.
- Grading is coarse: full score for demonstrated dedication and thoughtfulness.
- Sloppy exposition or unreadable code may result in point deductions.
- If you find a grading error, resubmit with a one-paragraph explanation. We reserve the right to re-grade the entire problem set.

## Repository Structure

```
.
├── README.md
├── LICENSE
├── Panel Data/
│   └── PanelData_syllabus.pdf      # Spring 2026 syllabus
└── Time Series/
    ├── TimeSeries_syllabus_2025.pdf # Spring 2025 syllabus (reference)
    ├── Slides/                      # Lecture slides (not tracked publicly)
    ├── Problem Sets/                # Practice problems (not tracked publicly)
    └── Books/                       # Reference materials (not tracked publicly)
```

**Note**: To avoid redistributing copyrighted material, most PDFs (slides, books, problem sets) are excluded from the public repository. Enrolled students can access these through NYU brightspace.

## Feedback

If you have suggestions for improving the TA sessions, want additional practice problems on specific topics, or notice any issues with the materials, please email Rafael. Feedback is always welcome!
