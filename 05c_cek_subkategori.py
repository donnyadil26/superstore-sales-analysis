import pandas as pd

pd.set_option("display.width", 200)
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

d = df[df["order_year"].isin([2016, 2017])]
t = d.pivot_table(index="sub_category", columns="order_year",
                  values="profit", aggfunc="sum").round(0)
t["selisih"] = t[2017] - t[2016]
print(t.sort_values("selisih"))