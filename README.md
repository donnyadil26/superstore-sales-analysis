# Analisis Penjualan Superstore

## Latar Belakang
Analisis data penjualan retail Superstore (9.994 transaksi, 2014-2017)
untuk mencari faktor yang memengaruhi profit.

## Dataset
Sumber: Kaggle, `vivek468/superstore-dataset-final`

## Pertanyaan Bisnis
1. Kategori dan sub-kategori apa yang paling untung dan rugi?
2. Bagaimana tren sales dan profit?
3. Region mana yang paling lemah?
4. Apakah diskon besar menurunkan profit?
5. Segmen pelanggan mana yang paling bernilai?

## Tools
Python (pandas, matplotlib), kagglehub

## Temuan Utama
- (isi 4-5 temuan dengan angka)

## Dugaan yang Diuji
(tempel tabel: dugaan | hasil)

## Rekomendasi
(isi 5 rekomendasi di atas)

## Keterbatasan
- Dataset tidak memiliki data biaya produk
- Korelasi tidak sama dengan sebab-akibat
- Sub-kategori seperti Machines hanya punya 24-33 transaksi per tahun,
  sehingga hasilnya mudah dipengaruhi beberapa order

## Cara Menjalankan
pip install kagglehub[pandas-datasets] pandas matplotlib
python 01_prepare_data.py
python 02_eda_kategori.py
...