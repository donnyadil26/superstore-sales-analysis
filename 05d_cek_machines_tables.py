import pandas as pd
pd.set_option("display.max_columns", None)  # tampilkan semua kolom
pd.set_option("display.width", 200)         # lebarkan area tampilan

pd.set_option("display.width", 200)
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

d = df[df["sub_category"].isin(["Machines", "Tables"])]
r = d.groupby(["sub_category", "order_year"]).agg(
    jumlah_transaksi=("order_id", "count"),
    sales=("sales", "sum"),
    profit=("profit", "sum"),
    avg_discount=("discount", "mean"),
).round(2)
r["avg_discount"] = (r["avg_discount"] * 100).round(1)
r["margin_%"] = (r["profit"] / r["sales"] * 100).round(1)
print(r)