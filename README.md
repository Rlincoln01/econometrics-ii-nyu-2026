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

## Books and Slides

Lecture slides will be posted to this repository. All books and papers can be accessed through the **NYU Library online**.

### Time Series

**Main Textbook:**
- Hamilton, J. (1994): *Time Series Analysis*. Princeton University Press.

**Supplementary:**
- Harvey, A. (1993): *Time Series Models* (2nd ed.). MIT Press. *(Out of print; used copies available online.)*

**Selected Papers:**
- Campbell & Shiller (1987): Cointegration and Tests of Present-Value Models
- Cochrane (1994): Permanent and transitory components of GNP and Stock Prices
- Blanchard & Quah (1989): Dynamic Effects of Aggregate Supply and Demand Shocks
- Hansen & Singleton (1982): Generalized instrumental variables estimation of nonlinear rational expectations models
- Hansen (1982): Large Sample Properties of GMM Estimators

### Panel Data

**Recommended Textbooks:**
- Arellano, M. (2003): *Panel Data Econometrics*. Oxford University Press.
- Wooldridge, J. (2010): *Econometric Analysis of Cross Section and Panel Data*. MIT Press.

**Selected Papers:**
- Arellano & Bond (1991): Some Tests of Specification for Panel Data
- Bonhomme, Lamadon & Manresa (2019): A distributional framework for matched employer-employee data
- Bonhomme & Manresa (2015): Grouped patterns of heterogeneity in panel data
- Chamberlain (1984): Panel Data (Handbook of Econometrics)
- Abowd, Kramarz & Margolis (1999): High wage workers and high wage firms

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

**Note**: To avoid redistributing copyrighted material, most PDFs (slides, books, problem sets) are excluded from the public repository. Enrolled students can access these through NYU course channels.

## Feedback

If you have suggestions for improving the TA sessions, want additional practice problems on specific topics, or notice any issues with the materials, please email Rafael. Feedback is always welcome!
