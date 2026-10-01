import pandas as pd

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", 45)

df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])
d = df[(df["sub_category"].isin(["Machines", "Tables"])) & (df["order_year"] == 2017)]

# 8 transaksi paling rugi
print(d.sort_values("profit").head(8)[
    ["sub_category", "product_name", "sales", "discount", "profit"]])

# Apakah satu transaksi mengubah hasil Machines 2017?
m = d[d["sub_category"] == "Machines"]
print("\nProfit Machines 2017:", round(m["profit"].sum()))
print("Tanpa 1 transaksi terburuk:", round(m["profit"].sum() - m["profit"].min()))

# Tables: berapa persen kerugian dari 5 transaksi terburuk?
t = d[d["sub_category"] == "Tables"]
print("\nProfit Tables 2017:", round(t["profit"].sum()))
print("Jumlah 5 transaksi terburuk:", round(t.nsmallest(5, "profit")["profit"].sum()))