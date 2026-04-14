import yfinance as yf

symbol = "^NSEBANK"

data = yf.download(symbol,start="2019-01-01", end="2024-12-31")



data.to_csv("nifty_bank.csv")