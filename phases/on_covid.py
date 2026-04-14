import pandas as pd

def on_covid_analysis(data, df):
    
    data = data.copy()

    cutoff = pd.to_datetime("2020-03-01")

    #Crash impact

    pre_end = df[df["Date"] < cutoff].iloc[-1]
    covid_bottom = data.loc[data["Close"].idxmin()]

    crash_drawdown = ((pre_end["Close"] - covid_bottom["Close"]) / pre_end["Close"]) * 100
    crash_duration = (covid_bottom["Date"] - pre_end["Date"]).days

    #Recovery strength

    covid_end = data.iloc[-1]["Close"]
    recovery = ((covid_end - covid_bottom["Close"]) / covid_bottom["Close"]) * 100

    #Volatility spike

    data["returns"] = data["Close"].pct_change().dropna()
    covid_volatility = data["returns"].std()

    total_days = len(data["returns"])

    #Instability(downward pressure)

    negative_days = (data["returns"] < 0).sum()
    downtrend_ratio = (negative_days / total_days) * 100

    #Stability(upward movement)

    positive_days = (data["returns"] > 0).sum()
    uptrend_ratio = (positive_days / total_days) * 100

    return {
        "crash_drawdown": crash_drawdown,
        "crash_duration": crash_duration,
        "recovery": recovery,
        "covid_volatility": covid_volatility,
        "downtrend_ratio": downtrend_ratio,
        "uptrend_ratio": uptrend_ratio
    }