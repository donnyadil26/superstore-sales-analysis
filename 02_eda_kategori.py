import pandas as pd
import matplotlib.pyplot as plt

# Baca data bersih (parse_dates supaya kolom tanggal tetap bertipe tanggal)
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

# Per kategori
kategori = df.groupby("category").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    jumlah_transaksi=("order_id", "count"),
).round(2)
kategori["margin_%"] = (kategori["total_profit"] / kategori["total_sales"] * 100).round(1)
print("=== PER KATEGORI ===")
print(kategori.sort_values("total_profit", ascending=False))

# Per sub-kategori
sub = df.groupby("sub_category").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    avg_discount=("discount", "mean"),
).round(2)
sub["margin_%"] = (sub["total_profit"] / sub["total_sales"] * 100).round(1)
print("\n=== PER SUB-KATEGORI ===")
print(sub.sort_values("total_profit", ascending=False))

# Visualisasi
data = sub.sort_values("total_profit")
warna = ["red" if x < 0 else "steelblue" for x in data["total_profit"]]

plt.figure(figsize=(9, 6))
plt.barh(data.index, data["total_profit"], color=warna)
plt.title("Total Profit per Sub-Kategori")
plt.xlabel("Profit")
plt.tight_layout()
plt.show()