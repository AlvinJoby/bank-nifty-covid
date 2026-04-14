import pandas as pd

def pre_covid_analysis(data):
    data = data.copy()

    #Baseline Trend

    start = data.iloc[0]["Close"]
    end = data.iloc[-1]["Close"]
    baseline_growth = ((end - start) / start) * 100

    #Baseline Volatility

    data["returns"] = data["Close"].pct_change()
    baseline_volatility = data["returns"].std()

    #Normal Drawdown

    data["rolling_max"] = data["Close"].cummax()
    data["drawdown"] = (data["Close"] - data["rolling_max"]) / data["rolling_max"]
    normal_drawdown = data["drawdown"].min() * 100

    #Market Strength

    near_high = data[data["drawdown"] > -0.05]  
    stability_ratio = len(near_high) / len(data) * 100

    #Trend Consistency

    positive_days = (data["returns"] > 0).sum()
    total_days = len(data)
    trend_consistency = (positive_days / total_days) * 100

    return {
        "baseline_growth": baseline_growth,
        "baseline_volatility": baseline_volatility,
        "normal_drawdown": normal_drawdown,
        "stability_ratio": stability_ratio,
        "trend_consistency": trend_consistency
    }