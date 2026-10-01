import pandas as pd
import matplotlib.pyplot as plt

# Baca data bersih
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

# ---------- 1. Tren per TAHUN ----------
tahunan = df.groupby("order_year").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
).round(2)
tahunan["margin_%"] = (tahunan["total_profit"] / tahunan["total_sales"] * 100).round(1)
tahunan["pertumbuhan_sales_%"] = (tahunan["total_sales"].pct_change() * 100).round(1)
print("=== TREN PER TAHUN ===")
print(tahunan)

# ---------- 2. Tren per BULAN (berurutan) ----------
bulanan = df.groupby("order_ym").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
).round(2)
print("\n=== 5 BULAN DENGAN SALES TERTINGGI ===")
print(bulanan.sort_values("total_sales", ascending=False).head(5))

# ---------- 3. Pola MUSIMAN (rata-rata per nama bulan) ----------
musiman = df.groupby("order_month")["sales"].sum()
print("\n=== TOTAL SALES PER BULAN (Jan-Des, semua tahun digabung) ===")
print(musiman.round(2))

# ---------- 4. Visualisasi ----------
fig, axes = plt.subplots(2, 1, figsize=(11, 8))

# Grafik 1: tren bulanan
axes[0].plot(bulanan.index, bulanan["total_sales"], label="Sales", color="steelblue")
axes[0].plot(bulanan.index, bulanan["total_profit"], label="Profit", color="green")
axes[0].set_title("Tren Sales dan Profit per Bulan")
axes[0].set_xticks(range(0, len(bulanan), 6))   # tampilkan label tiap 6 bulan
axes[0].tick_params(axis="x", rotation=45)
axes[0].legend()

# Grafik 2: pola musiman
axes[1].bar(musiman.index, musiman.values, color="steelblue")
axes[1].set_title("Total Sales per Bulan (Jan-Des, semua tahun)")
axes[1].set_xlabel("Bulan")
axes[1].set_xticks(range(1, 13))

plt.tight_layout()
plt.show()