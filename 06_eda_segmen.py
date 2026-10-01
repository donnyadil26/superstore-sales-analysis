import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

# Baca data bersih
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

# ---------- 1. Performa per SEGMEN ----------
seg = df.groupby("segment").agg(
    jumlah_pelanggan=("customer_id", "nunique"),
    jumlah_order=("order_id", "nunique"),
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    avg_discount=("discount", "mean"),
    pct_rugi=("is_loss", "mean"),
).round(2)
seg["margin_%"] = (seg["total_profit"] / seg["total_sales"] * 100).round(1)
seg["sales_per_pelanggan"] = (seg["total_sales"] / seg["jumlah_pelanggan"]).round(0)
seg["profit_per_pelanggan"] = (seg["total_profit"] / seg["jumlah_pelanggan"]).round(0)
seg["order_per_pelanggan"] = (seg["jumlah_order"] / seg["jumlah_pelanggan"]).round(1)
seg["avg_discount"] = (seg["avg_discount"] * 100).round(1)
seg["pct_rugi"] = (seg["pct_rugi"] * 100).round(1)
print("=== PER SEGMEN ===")
print(seg.sort_values("total_profit", ascending=False))

# ---------- 2. Pelanggan teratas dan terbawah ----------
pelanggan = df.groupby(["customer_id", "customer_name"]).agg(
    jumlah_order=("order_id", "nunique"),
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
).round(2).sort_values("total_profit", ascending=False)

print("\n=== 10 PELANGGAN DENGAN PROFIT TERTINGGI ===")
print(pelanggan.head(10))

print("\n=== 10 PELANGGAN DENGAN PROFIT TERENDAH ===")
print(pelanggan.tail(10))

# ---------- 3. Seberapa terkonsentrasi profitnya? ----------
total = pelanggan["total_profit"].sum()
top10_share = pelanggan.head(10)["total_profit"].sum() / total * 100
print("\nJumlah pelanggan:", len(pelanggan))
print("Pelanggan yang rugi:", (pelanggan["total_profit"] < 0).sum())
print("Kontribusi 10 pelanggan teratas terhadap total profit:", round(top10_share, 1), "%")

# ---------- 4. Visualisasi ----------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(seg.index, seg["total_profit"], color="steelblue")
axes[0].set_title("Total Profit per Segmen")

axes[1].bar(seg.index, seg["profit_per_pelanggan"], color="green")
axes[1].set_title("Profit per Pelanggan per Segmen")

plt.tight_layout()
plt.show()