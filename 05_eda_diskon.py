import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)  # tampilkan semua kolom
pd.set_option("display.width", 200)         # lebarkan area tampilan

# Baca data bersih
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

# ---------- 1. Kelompokkan transaksi ke level diskon ----------
batas = [-0.001, 0, 0.2, 0.4, 0.6, 0.8]
label = ["0%", "1-20%", "21-40%", "41-60%", "61-80%"]
df["level_diskon"] = pd.cut(df["discount"], bins=batas, labels=label)

diskon = df.groupby("level_diskon", observed=True).agg(
    jumlah_transaksi=("order_id", "count"),
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    avg_profit=("profit", "mean"),
    pct_rugi=("is_loss", "mean"),
).round(2)
diskon["margin_%"] = (diskon["total_profit"] / diskon["total_sales"] * 100).round(1)
diskon["pct_rugi"] = (diskon["pct_rugi"] * 100).round(1)
print("=== PERFORMA PER LEVEL DISKON ===")
print(diskon)

# ---------- 2. Korelasi diskon vs profit ----------
korelasi = df["discount"].corr(df["profit"])
print("\nKorelasi diskon vs profit:", round(korelasi, 3))

# ---------- 3. Diskon per TAHUN (menjelaskan margin 2017?) ----------
tahun = df.groupby("order_year").agg(
    avg_discount=("discount", "mean"),
    margin=("profit", "sum"),
    sales=("sales", "sum"),
)
tahun["margin_%"] = (tahun["margin"] / tahun["sales"] * 100).round(1)
tahun["avg_discount"] = (tahun["avg_discount"] * 100).round(1)
print("\n=== DISKON & MARGIN PER TAHUN ===")
print(tahun[["avg_discount", "margin_%"]])

# ---------- 4. Diskon per KATEGORI ----------
kat = df.groupby("category").agg(
    avg_discount=("discount", "mean"),
    pct_rugi=("is_loss", "mean"),
).round(3)
kat["avg_discount"] = (kat["avg_discount"] * 100).round(1)
kat["pct_rugi"] = (kat["pct_rugi"] * 100).round(1)
print("\n=== DISKON & TRANSAKSI RUGI PER KATEGORI ===")
print(kat)

# ---------- 5. Visualisasi ----------
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].bar(diskon.index.astype(str), diskon["avg_profit"], color="steelblue")
axes[0].axhline(0, color="black", linewidth=0.8)
axes[0].set_title("Rata-rata Profit per Transaksi")
axes[0].set_xlabel("Level diskon")

axes[1].bar(diskon.index.astype(str), diskon["pct_rugi"], color="red")
axes[1].set_title("% Transaksi Rugi")
axes[1].set_xlabel("Level diskon")

plt.tight_layout()
plt.show()