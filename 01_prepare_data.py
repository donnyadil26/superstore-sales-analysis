import kagglehub
import pandas as pd
from kagglehub import KaggleDatasetAdapter

# 1. Load data dari Kaggle
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "vivek468/superstore-dataset-final",
    "Sample - Superstore.csv",
    pandas_kwargs={"encoding": "latin-1"},
)

# 2. Rapikan nama kolom
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# 3. Ubah kolom tanggal
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

# 4. Feature engineering
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["order_ym"] = df["order_date"].dt.to_period("M").astype(str)
df["ship_days"] = (df["ship_date"] - df["order_date"]).dt.days
df["profit_margin"] = df["profit"] / df["sales"] * 100
df["is_loss"] = df["profit"] < 0

# 5. Simpan data bersih
df.to_csv("superstore_clean.csv", index=False)
print("Selesai. Data tersimpan:", df.shape)