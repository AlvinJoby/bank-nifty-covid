# COVID Impact on Banking Sector (NIFTY Bank)

## Overview

This project analyzes how the NIFTY Bank index behaved across three distinct periods surrounding COVID-19.

The dataset is segmented into phases to observe how market behavior changed under different conditions:

* Pre-COVID (baseline)
* COVID phase (shock period)
* Post-COVID (recovery)

---

## Dataset

* Source: Yahoo Finance
* Index: NIFTY Bank
* Period: 2019 – 2024
* Fields used:

  * Date
  * Close Price

---

## Phase Definition

| Phase      | Period              |
| ---------- | ------------------- |
| Pre-COVID  | Before March 2020   |
| COVID      | Mar 2020 – Dec 2021 |
| Post-COVID | 2022 onwards        |

---

# Analysis

## 1. Pre-COVID Phase

![Pre-COVID](outputs/pre_covid.png)

### Metrics

| Metric              | Value   |
| ------------------- | ------- |
| Growth (%)          | 7.26    |
| Volatility          | 0.01259 |
| Drawdown (%)        | -15.47  |
| Time Near Highs (%) | 70.67   |
| Up Days (%)         | 49.82   |

### Observation

The index moved in a relatively stable manner during this period.
Growth was moderate, and volatility remained low. Prices stayed near peak levels for a large portion of the time, indicating steady market conditions.

---

## 2. COVID Phase

![COVID](outputs/covid.png)

### Metrics

| Metric                | Value   |
| --------------------- | ------- |
| Crash Drawdown (%)    | 41.96   |
| Crash Duration (days) | 24      |
| Recovery (%)          | 109.73  |
| Volatility            | 0.02253 |
| Down Days (%)         | 46.05   |
| Up Days (%)           | 53.73   |

### Observation

The index experienced a sharp decline of around 42% within 24 days, marking a clear break from normal behavior.
Volatility increased significantly during this phase.

Despite the decline, the index recovered strongly within the same period, with a recovery of over 100% from the lowest point.

---

## 3. Post-COVID Phase

![Post-COVID](outputs/post_covid.png)

### Metrics

| Metric                         | Value   |
| ------------------------------ | ------- |
| Recovery vs Pre-COVID Peak (%) | 67.6    |
| Growth (%)                     | 39.9    |
| Volatility                     | 0.01097 |
| Drawdown (%)                   | -17.07  |
| Up Days (%)                    | 53.66   |

### Observation

The index moved above its pre-COVID levels and continued in an upward trend.
Volatility reduced compared to the COVID phase, although corrections remained present.

Overall movement during this phase indicates sustained recovery with continued growth.

---

## Summary

* Pre-COVID: Stable market conditions with moderate growth
* COVID: Sharp decline followed by high volatility and recovery
* Post-COVID: Strong recovery with continued upward movement

---

## How to Run

```bash
python analysis.py
```

Requirements:

* CSV file inside `data/`
* Output graphs inside `outputs/`

---

## Project Structure

```
covid-analytics/
│── data/
│── phases/
│── outputs/
│── analysis.py
│── graph.py
```

---
