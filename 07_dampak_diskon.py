import pandas as pd

df = pd.read_csv("superstore_clean.csv", parse_dates=["order_date", "ship_date"])

total_rugi = df.loc[df["profit"] < 0, "profit"].sum()
for batas in [0.2, 0.4]:
    d = df[df["discount"] > batas]
    rugi = d.loc[d["profit"] < 0, "profit"].sum()
    print(f"Diskon > {int(batas*100)}%: {len(d)} transaksi, "
          f"kerugian {rugi:,.0f} ({rugi/total_rugi*100:.1f}% dari total kerugian)")