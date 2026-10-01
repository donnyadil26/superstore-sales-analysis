import pandas as pd

pd.set_option("display.width", 200)
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

p = df.groupby("customer_id").agg(
    total_profit=("profit", "sum"),
    avg_discount=("discount", "mean"),
)
p["rugi"] = p["total_profit"] < 0

print((p.groupby("rugi")["avg_discount"].mean() * 100).round(1))