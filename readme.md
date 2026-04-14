# COVID Impact on Banking Sector (NIFTY Bank)

## Overview

This project analyzes how the NIFTY Bank index behaved before, during, and after the COVID-19 period.

The data is divided into three phases to understand how market behavior changed over time:

* Pre-COVID
* COVID Phase
* Post-COVID

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

## Visuals

### Pre-COVID

![Pre-COVID](outputs/pre_covid.png)

---

### COVID Phase

![COVID](outputs/covid.png)

---

### Post-COVID

![Post-COVID](outputs/post_covid.png)

---

## Metrics

### Pre-COVID

| Metric              | Value   |
| ------------------- | ------- |
| Growth (%)          | 7.26    |
| Volatility          | 0.01259 |
| Drawdown (%)        | -15.47  |
| Time Near Highs (%) | 70.67   |
| Up Days (%)         | 49.82   |

---

### COVID Phase

| Metric                | Value   |
| --------------------- | ------- |
| Crash Drawdown (%)    | 41.96   |
| Crash Duration (days) | 24      |
| Recovery (%)          | 109.73  |
| Volatility            | 0.02253 |
| Down Days (%)         | 46.05   |
| Up Days (%)           | 53.73   |

---

### Post-COVID

| Metric                         | Value   |
| ------------------------------ | ------- |
| Recovery vs Pre-COVID Peak (%) | 67.6    |
| Growth (%)                     | 39.9    |
| Volatility                     | 0.01097 |
| Drawdown (%)                   | -17.07  |
| Up Days (%)                    | 53.66   |

---

## Observations

Before COVID, the index moved in a relatively stable manner. Growth was moderate, volatility was low, and prices stayed near peak levels for a significant portion of the time.

During the COVID phase, the index experienced a sharp decline of around 42% in just 24 days. Volatility increased noticeably during this period. Despite the fall, the index recovered more than 100% from its lowest point within the same phase.

After COVID, the index moved above its earlier levels, with an overall growth of about 40%. Volatility reduced compared to the COVID phase, although corrections of around 17% were still observed. The overall movement remained upward.

---

## How to Run

```bash
python analysis.py
```

Make sure:

* The CSV file is inside the `data/` folder
* Output images are generated inside `outputs/`

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
