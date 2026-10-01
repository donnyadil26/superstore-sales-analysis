import pandas as pd

pd.set_option("display.width", 200)
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

# 1. Porsi transaksi dengan diskon > 20% per tahun
df["diskon_tinggi"] = df["discount"] > 0.2
print((df.groupby("order_year")["diskon_tinggi"].mean() * 100).round(1))

# 2. Komposisi sales per kategori per tahun (%)
komposisi = df.pivot_table(index="order_year", columns="category",
                           values="sales", aggfunc="sum")
print((komposisi.div(komposisi.sum(axis=1), axis=0) * 100).round(1))

# 3. Margin per kategori per tahun
m = df.groupby(["order_year", "category"])[["profit", "sales"]].sum()
m["margin_%"] = (m["profit"] / m["sales"] * 100).round(1)
print(m["margin_%"].unstack())