import pandas as pd

from graph import generate_graph
from phases.pre_covid import pre_covid_analysis
from phases.on_covid import on_covid_analysis
from phases.post_covid import post_covid_analysis

df = pd.read_csv("data/nifty_bank.csv",skiprows=3)

df.columns = ["Date","Close","High","Low","Open","Volume"]

phases = ["pre_covid","covid","post_covid"]

df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

df = df.dropna()
df= df.sort_values("Date")

def classify_phase(date):
    if date < pd.to_datetime("2020-03-01"):
        return phases[0]
    elif date <= pd.to_datetime("2021-12-31"):
        return phases[1]
    else:
        return phases[2]
    
df["Phase"] = df["Date"].apply(classify_phase)

pre_covid = df[df['Phase']=="pre_covid"]
covid = df[df['Phase']=="covid"]
post_covid = df[df['Phase']=="post_covid"]


phase_data = {
    "pre_covid": pre_covid,
    "covid": covid,
    "post_covid": post_covid
}

def phase_analysis(name, data, df):
    data = data.copy()

    high_row = data.loc[data["Close"].idxmax()]
    low_row = data.loc[data["Close"].idxmin()]

    drawdown = ((high_row["Close"] - low_row["Close"]) / high_row["Close"]) * 100

    result = {
        "phase": name,
        "high_value": high_row["Close"],
        "high_date": high_row["Date"],
        "low_value": low_row["Close"],
        "low_date": low_row["Date"],
        "drawdown": drawdown,
        "duration": None
    }

    if name == "covid":
        pre_covid_end = df[df["Date"] < "2020-03-01"].iloc[-1]
        covid_bottom = low_row

        crash_drawdown = ((pre_covid_end["Close"] - covid_bottom["Close"]) / pre_covid_end["Close"]) * 100
        crash_duration = (covid_bottom["Date"] - pre_covid_end["Date"]).days

        result["drawdown"] = crash_drawdown
        result["duration"] = crash_duration

    return result

#GENERAL VIEW

print("\nQUICK TAKE\n\n")

for phase_name, data in phase_data.items():
    result = phase_analysis(phase_name, data, df)

    print(f"\nPhase: {result['phase']}")
    print("High:", result["high_value"], "on", result["high_date"])
    print("Low:", result["low_value"], "on", result["low_date"])
    print("Drawdown (%):", round(result["drawdown"], 2))

    if result["duration"] is not None:
        print("Time to fall:", result["duration"], "days")


#GRAPH - 3 PHASES

generate_graph(pre_covid, covid, post_covid)


# PRE - COVID

pre_covid_result = pre_covid_analysis(pre_covid)

# COVID

covid_result = on_covid_analysis(covid, df)

# POST - COVID

post_covid_result = post_covid_analysis(post_covid, df)

# Insights

print("\n\nFINAL INSIGHTS\n")

# --- Pre-COVID ---

print("[Pre-COVID]")

print("Growth (%):", round(pre_covid_result["baseline_growth"], 2))
print("Volatility:", round(pre_covid_result["baseline_volatility"], 5))
print("Drawdown (%):", round(pre_covid_result["normal_drawdown"], 2))
print("Time Near Highs (%):", round(pre_covid_result["stability_ratio"], 2))
print("Up Days (%):", round(pre_covid_result["trend_consistency"], 2))


if pre_covid_result["baseline_volatility"] < covid_result["covid_volatility"]:
    print("Market was relatively stable before COVID.")

if pre_covid_result["normal_drawdown"] > -20:
    print("Corrections were moderate and within normal range.")

if pre_covid_result["trend_consistency"] > 50:
    print("Overall movement showed a slight upward bias.")


# --- COVID ---

print("\n[COVID Phase]")

print("Crash Drawdown (%):", round(covid_result["crash_drawdown"], 2))
print("Crash Duration (days):", covid_result["crash_duration"])
print("Recovery (%):", round(covid_result["recovery"], 2))
print("Volatility:", round(covid_result["covid_volatility"], 5))
print("Down Days (%):", round(covid_result["downtrend_ratio"], 2))
print("Up Days (%):", round(covid_result["uptrend_ratio"], 2))

if covid_result["crash_drawdown"] > abs(pre_covid_result["normal_drawdown"]):
    print("The COVID crash was significantly deeper than normal market corrections.")

if covid_result["crash_duration"] < 60:
    print("The decline happened rapidly within a short time frame.")

if covid_result["downtrend_ratio"] > covid_result["uptrend_ratio"]:
    print("Downward pressure dominated during the crisis.")

if covid_result["recovery"] > 50:
    print("The sector showed a strong recovery within the same phase.")


# --- Post-COVID ---

print("\n[Post-COVID]")

print("Recovery vs Pre-COVID Peak (%):", round(post_covid_result["recovery_strength"], 2))
print("Growth (%):", round(post_covid_result["post_growth"], 2))
print("Volatility:", round(post_covid_result["post_volatility"], 5))
print("Drawdown (%):", round(post_covid_result["post_drawdown"], 2))
print("Up Days (%):", round(post_covid_result["uptrend_ratio"], 2))

if post_covid_result["recovery_strength"] > 0:
    print("The sector recovered beyond its pre-COVID levels.")

if post_covid_result["post_growth"] > 0:
    print("An overall upward trend continued after the recovery.")

if post_covid_result["post_drawdown"] < pre_covid_result["normal_drawdown"]:
    print("Post-COVID corrections remained significant.")

if post_covid_result["uptrend_ratio"] > 50:
    print("Upward movement dominated in the post-COVID phase.")