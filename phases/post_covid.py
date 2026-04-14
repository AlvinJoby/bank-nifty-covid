import pandas as pd

def post_covid_analysis(data, df):

    data = data.copy()

    cutoff = pd.to_datetime("2020-03-01")

    #Recovery vs Pre-COVID peak

    pre_peak = df[df["Date"] < cutoff]["Close"].max()
    post_peak = data["Close"].max()

    recovery_strength = ((post_peak - pre_peak) / pre_peak) * 100

    #Post-COVID growth

    start = data.iloc[0]["Close"]
    end = data.iloc[-1]["Close"]

    post_growth = ((end - start) / start) * 100

    #Volatility

    data["returns"] = data["Close"].pct_change().dropna()
    post_volatility = data["returns"].std()

    #Drawdown

    data["rolling_max"] = data["Close"].cummax()
    data["drawdown"] = (data["Close"] - data["rolling_max"]) / data["rolling_max"]

    post_drawdown = data["drawdown"].min() * 100

    #Trend strength

    positive_days = (data["returns"] > 0).sum()
    total_days = len(data["returns"])

    uptrend_ratio = (positive_days / total_days) * 100

    return {
        "recovery_strength": recovery_strength,
        "post_growth": post_growth,
        "post_volatility": post_volatility,
        "post_drawdown": post_drawdown,
        "uptrend_ratio": uptrend_ratio
    }