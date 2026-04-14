# NIFTY Bank & COVID-19

A data-driven look at how the Indian banking sector held up — and eventually thrived — through one of the most disruptive global events in recent memory.

This project tracks the NIFTY Bank index from 2019 to 2024, splitting the timeline into three distinct market phases to understand how external shocks translate into price behavior. The goal wasn't just to confirm that COVID caused a crash — everyone knows that. It was to quantify exactly how fast it fell, how long the chaos lasted, and what the recovery actually looked like in numbers.

---

## Snapshot

Before getting into the phases, here's the headline:

| | |
|---|---|
| COVID crash | **−41.96%** |
| Crash duration | **24 days** |
| Recovery (within COVID phase) | **+109.73%** |
| Post-COVID growth | **+39.9%** |
| Recovery vs pre-COVID peak | **+67.6%** |

A 42% wipeout in under a month, followed by a recovery that more than doubled the index from its low. The speed of both the fall and the rebound is what makes this dataset interesting.

---

## Dataset

| Field | Details |
|---|---|
| Source | Yahoo Finance |
| Index | NIFTY Bank |
| Period | 2019 – 2024 |
| Fields used | Date, Close |

The NIFTY Bank index tracks the performance of the 12 most liquid and large-cap banking stocks listed on the NSE. It's a good proxy for the broader financial sector's health in India.

### Phase definitions

The timeline is split into three phases based on when COVID materially impacted Indian markets:

| Phase | Period | Rationale |
|---|---|---|
| Pre-COVID | Before March 2020 | Baseline — normal market conditions |
| COVID phase | Mar 2020 – Dec 2021 | Covers crash, lockdowns, and the initial recovery |
| Post-COVID | 2022 onwards | Post-recovery, normalization period |

March 2020 was chosen as the COVID start because that's when the WHO declared a pandemic and Indian markets began pricing in the full impact. December 2021 as the end point captures the recovery cycle completing and volatility settling back toward normal.

---

## Phase Breakdown

### 🟢 Pre-COVID — Slow and steady

| Metric | Value |
|---|---|
| Growth | 7.26% |
| Volatility | 0.0126 |
| Max drawdown | −15.47% |
| Time near highs | 70.67% |
| Up days | 49.82% |

The pre-COVID period was textbook bull market behavior. The index spent roughly 70% of its time within striking distance of its peak, meaning dips were bought quickly and recoveries were swift. Volatility at 0.0126 was low — day-to-day swings were small and predictable.

The modest 7.26% growth reflects a market that wasn't running hot, just grinding steadily upward. The max drawdown of ~15% is a useful baseline — it tells us what a "normal" bad period looked like before COVID hit, which makes the 42% crash even more stark by comparison.

Up days at 49.82% means the index was essentially a coin-flip on any given day — typical for a rangebound, low-volatility market.

---

### 🔴 COVID — Crash, then climb

| Metric | Value |
|---|---|
| Crash drawdown | −41.96% |
| Crash duration | 24 days |
| Recovery from low | +109.73% |
| Volatility | 0.0225 |
| Down days | 46.05% |
| Up days | 53.73% |

This is where things get interesting. The index lost nearly 42% of its value in 24 calendar days — a pace of decline that's genuinely rare for a major sectoral index. For context, the 2008 financial crisis took several months to produce similar losses in most markets. COVID compressed that into less than four weeks.

Volatility jumped to 0.0225, nearly double the pre-COVID level. That's the market pricing in uncertainty — nobody knew how long lockdowns would last, what the credit impact would be on banks, or whether RBI interventions would be enough.

What's equally notable is the recovery. From the March 2020 trough, the index eventually gained over 109% within the same phase — meaning it more than doubled. That's partly a reflection of how oversold the crash left things, and partly a result of aggressive monetary easing globally and domestically. The up/down day split also normalized to roughly 54/46, showing that once the panic selling stopped, buyers consistently had the upper hand.

---

### 🔵 Post-COVID — New highs, calmer waters

| Metric | Value |
|---|---|
| Growth vs pre-COVID peak | +67.6% |
| Phase growth | +39.9% |
| Volatility | 0.0110 |
| Max drawdown | −17.07% |
| Up days | 53.66% |

By 2022, the index wasn't just recovered — it was in genuinely new territory, trading 67.6% above its pre-COVID peak. That's not just "getting back to normal," that's a structural re-rating of the sector.

Volatility at 0.0110 actually came in below the pre-COVID baseline of 0.0126, which suggests the post-COVID market was more confident and less reactive than the one before the pandemic. The max drawdown of ~17% is nearly identical to the pre-COVID figure, meaning corrections returned to their normal magnitude — sharp enough to notice, but not the cascading sell-offs seen during the crisis.

Up days held steady at 53.66%, almost exactly matching the COVID recovery phase, indicating the bullish bias that emerged post-crash continued well into the normalization period.

---

## Conclusion

The NIFTY Bank index went through three very different regimes in five years. A slow grind upward, a historic collapse, and then a recovery that left the index significantly above where it started.

The COVID crash was extreme in speed — 42% in 24 days — but the market's ability to recover just as quickly is the real story here. The same forces that caused the panic (liquidity concerns, credit risk fears, macro uncertainty) reversed hard once central banks stepped in and it became clear the banking sector wasn't facing a solvency crisis.

Post-2022, things normalized better than the pre-COVID baseline in some ways: lower volatility, similar drawdown depth, and a consistent upward trend. If anything, the COVID shock seems to have shaken out weaker hands and reset valuations in a way that gave the index a cleaner runway going forward.

The broader takeaway: external shocks can be violent and fast, but sectoral fundamentals tend to reassert themselves. The NIFTY Bank index didn't just survive COVID — it used the recovery as a launchpad.

---

## Running the Analysis

Clone the repo and make sure your data file is inside `data/` before running.

```bash
python analysis.py
```

Phase charts and output images will be saved to `outputs/` automatically. The phase logic is handled in `analysis.py`; visualization code lives in `graph.py`.

### Requirements

- Python 3.x
- CSV file with `Date` and `Close` columns inside `data/`
- Output directory `outputs/` (created automatically if it doesn't exist)

---

## Project Structure

```
bank-nifty-covid/
├── data/              # Raw CSV data from Yahoo Finance
├── phases/            # Phase-split datasets
├── outputs/           # Generated charts and visuals
├── analysis.py        # Core analysis logic
└── graph.py           # Plotting and visualization
```