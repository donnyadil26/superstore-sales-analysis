import pandas as pd
import matplotlib.pyplot as plt

# Baca data bersih
df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

# ---------- 1. Performa per REGION ----------
region = df.groupby("region").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    avg_discount=("discount", "mean"),
    pct_rugi=("is_loss", "mean"),
).round(2)
region["margin_%"] = (region["total_profit"] / region["total_sales"] * 100).round(1)
region["pct_rugi"] = (region["pct_rugi"] * 100).round(1)
print("=== PER REGION ===")
print(region.sort_values("total_profit", ascending=False))

# ---------- 2. Performa per STATE ----------
state = df.groupby("state").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
).round(2)
state["margin_%"] = (state["total_profit"] / state["total_sales"] * 100).round(1)
state = state.sort_values("total_profit")

print("\n=== 10 STATE DENGAN PROFIT TERENDAH ===")
print(state.head(10))

print("\n=== 5 STATE DENGAN PROFIT TERTINGGI ===")
print(state.tail(5).iloc[::-1])

print("\n=== REGION DAN STATE YANG MENDOMINASI PROFIT TERENDAH ===")
print(df.groupby(["region", "state"])["profit"].sum().round(0).sort_values().head(10))

# ---------- 3. Visualisasi ----------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Grafik 1: profit per region
r = region.sort_values("total_profit")
axes[0].barh(r.index, r["total_profit"], color="steelblue")
axes[0].set_title("Total Profit per Region")
axes[0].set_xlabel("Profit")

# Grafik 2: 10 state terendah (merah = rugi)
bawah = state.head(10)
warna = ["red" if x < 0 else "steelblue" for x in bawah["total_profit"]]
axes[1].barh(bawah.index, bawah["total_profit"], color=warna)
axes[1].set_title("10 State dengan Profit Terendah")
axes[1].set_xlabel("Profit")

plt.tight_layout()
plt.show()