# Analisis Penjualan Superstore: Dari Mana Kerugian Berasal?

Analisis eksplorasi data (EDA) pada 9.994 transaksi retail Superstore periode 2014-2017 menggunakan Python. Fokus utamanya: faktor apa yang memengaruhi profit, dan di mana bisnis kehilangan keuntungan.

## Ringkasan

Total sales 2014-2017 sekitar **2,30 juta** dengan total profit **286 ribu** (margin sekitar 12,5%). Sekitar **18,7%** transaksi merugi. Temuan paling penting: **transaksi dengan diskon di atas 20% hanya 13,9% dari seluruh transaksi, tetapi menyumbang 88,7% dari total kerugian.**

## Dataset

- Sumber: Kaggle, [`vivek468/superstore-dataset-final`](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- 9.994 baris, 21 kolom, tanpa missing value dan tanpa duplikat
- Data tidak memuat biaya produk, hanya sales, quantity, discount, dan profit

## Pertanyaan Bisnis

1. Kategori dan sub-kategori apa yang paling untung dan paling rugi?
2. Bagaimana tren sales dan profit?
3. Region mana yang paling lemah?
4. Apakah diskon besar menurunkan profit?
5. Segmen pelanggan mana yang paling bernilai?

## Tools

Python (pandas, matplotlib), kagglehub

## Temuan Utama

**1. Furniture besar tetapi nyaris tidak menguntungkan.**
Furniture punya sales 742 ribu (kedua tertinggi) tetapi profit hanya 18,5 ribu, margin 2,5%. Technology (17,4%) dan Office Supplies (17,0%) jauh lebih sehat. Tiga sub-kategori merugi: Tables (-17.725), Bookcases (-3.473), dan Supplies (-1.189).

**2. Sales tumbuh, tetapi tidak stabil, dan margin turun di 2017.**
Sales naik dari 484 ribu (2014) ke 733 ribu (2017), dengan tahun 2015 turun 2,8%, 2016 naik 29,5%, dan 2017 naik 20,4%. Margin bergerak 10,2% → 13,1% → 13,4% → 12,7%. Penjualan memuncak di November (352 ribu), Desember (325 ribu), dan September (308 ribu), jauh di atas Januari (95 ribu) dan Februari (60 ribu).

**3. Diskon di atas 20% adalah sumber kerugian utama.**

| Level diskon | Transaksi | % transaksi rugi | Margin |
|---|---|---|---|
| 0% | 4.798 | 0,0% | 29,5% |
| 1-20% | 3.803 | 14,0% | 11,9% |
| 21-40% | 460 | 90,0% | -15,3% |
| 41-60% | 215 | 100,0% | -40,7% |
| 61-80% | 718 | 100,0% | -122,6% |

Diskon di atas 20% terjadi pada 1.393 transaksi (13,9%) dengan kerugian 138.515 (88,7% dari total kerugian). Diskon di atas 40% hanya 933 transaksi (9,3%) tetapi menyumbang 63,8% kerugian. Korelasi linear diskon vs profit hanya -0,219 (lemah), karena hubungannya berbentuk ambang batas, bukan garis lurus.

**4. Central adalah region terlemah.**
Central punya margin 7,9% dan 32% transaksinya rugi, dengan rata-rata diskon 24% (West hanya 11%). Sales Central (501 ribu) lebih besar dari South (392 ribu), tetapi profitnya lebih kecil (39,7 ribu vs 46,7 ribu). Secara nominal, kerugian terbesar ada di Texas (-25.729), Ohio (-16.971), Pennsylvania (-15.560), dan Illinois (-12.608).

**5. Consumer terbesar, Home Office paling bernilai per pelanggan.**
Consumer unggul di total profit (134 ribu), tetapi Home Office punya margin tertinggi (14,0%) dan profit per pelanggan tertinggi (407 vs 328 di Consumer). Diskon dan persentase transaksi rugi hampir sama antar segmen, sehingga bukan penjelas perbedaan ini. Sebanyak 155 dari 793 pelanggan (19,5%) merugi, dan pelanggan rugi rata-rata mendapat diskon 23,8% dibanding 13,8% pada pelanggan untung.

## Studi Kasus: Mengapa Margin 2017 Turun?

Sales 2017 naik 20,4% tetapi profit hanya naik sekitar 14,2%, sehingga margin turun dari 13,4% ke 12,7%. Beberapa dugaan diuji satu per satu:

| Dugaan | Hasil |
|---|---|
| Diskon tinggi berkaitan dengan kerugian | **Didukung kuat** (ambang sekitar 20%) |
| Pelanggan rugi menerima diskon lebih tinggi | **Didukung** (23,8% vs 13,8%) |
| Rata-rata diskon naik di 2017 | Gugur (15,5% → 15,6%) |
| Porsi transaksi diskon > 20% naik di 2017 | Gugur (14,0% → 13,7%) |
| Komposisi kategori berubah ke arah margin rendah | Gugur (porsi Furniture justru turun ke 29,4%) |
| Diskon Machines dan Tables naik di 2017 | Gugur (Machines 32% → 30%, Tables tetap 27%) |
| Machines anjlok sebagai tren | Gugur, disebabkan 2 transaksi berdiskon 50% dan 70% |
| Tables rugi secara struktural | **Didukung** (rugi 4 tahun berturut-turut, diskon 24-27%) |
| Perbedaan margin antar segmen berasal dari komposisi produk | Belum diuji |

**Penjelasan:** penurunan terpusat di Machines dan Tables.

- **Machines:** profit berubah dari +2.907 (2016) menjadi -2.869 (2017). Dua transaksi (Cubify 3D Printer, diskon 50%, -3.840; Lexmark Laser Printer, diskon 70%, -3.400) totalnya -7.240. Tanpa Cubify saja, profit Machines 2017 kembali +971. Dengan hanya 33 transaksi setahun, beberapa order bisa mengubah hasil.
- **Tables:** kerugian membengkak dari -2.951 ke -8.141. Lima transaksi terburuk (diskon 40-50%) menyumbang -3.811, sekitar 47% dari kerugian 2017.

**Pelajaran:** rata-rata bisa menyembunyikan outlier. Rata-rata diskon stabil, tetapi beberapa transaksi ekstrem tetap merusak hasil setahun.

## Rekomendasi

1. **Batasi diskon maksimal 20%.** Di atas ambang ini 90-100% transaksi merugi, dan 13,9% transaksi menyumbang 88,7% kerugian. Ini prioritas utama.
2. **Wajibkan persetujuan manajer untuk diskon di atas 40%.** Hanya 9,3% transaksi, tetapi 63,8% kerugian. Transaksi terburuk Machines dan Tables 2017 semuanya berada di rentang ini.
3. **Evaluasi harga dan diskon Tables.** Rugi empat tahun berturut-turut (margin -6,8%, -9,0%, -4,9%, -13,4%) dengan diskon 24-27%. Pertimbangkan menaikkan harga dasar, menurunkan diskon, atau meninjau pemasoknya.
4. **Tinjau wilayah Central dan state dengan kerugian terbesar.** Mulai dari Texas dan Illinois, dengan fokus pada kebijakan diskon (rata-rata Central 24%, 32% transaksi rugi).
5. **Siapkan stok dan promosi di September, November, dan Desember**, tiga bulan dengan sales tertinggi. Pastikan promosi di periode ramai tetap berada di bawah batas diskon 20%.

> Angka kerugian dari diskon (138.515) adalah **batas atas teoretis**, bukan prediksi kenaikan profit. Sebagian transaksi berdiskon tinggi mungkin tidak akan terjadi tanpa diskon, dan sebagian masih untung.

## Keterbatasan

- Dataset tidak memiliki data biaya produk, sehingga penyebab pasti margin rendah tidak bisa dipastikan.
- Temuan bersifat korelasi, belum membuktikan sebab-akibat.
- Sub-kategori seperti Machines hanya memiliki 24-33 transaksi per tahun, sehingga hasilnya mudah dipengaruhi beberapa order.
- Cakupan data hanya 2014-2017 dan satu perusahaan, sehingga belum tentu berlaku umum.
- Dugaan "komposisi produk menjelaskan perbedaan margin antar segmen" belum diuji.

## Cara Menjalankan

```bash
pip install kagglehub[pandas-datasets] pandas matplotlib
```

Jalankan `01_prepare_data.py` terlebih dahulu. File ini mengunduh data dari Kaggle dan membuat `superstore_clean.csv` (file ini tidak disertakan di repository). Setelah itu, file lain bisa dijalankan dalam urutan apa pun:

| File | Isi |
|---|---|
| `01_prepare_data.py` | Load data, cleaning, feature engineering |
| `02_eda_kategori.py` | Profit per kategori dan sub-kategori |
| `03_eda_tren.py` | Tren tahunan, bulanan, dan musiman |
| `04_eda_region.py` | Performa per region dan state |
| `05_eda_diskon.py` | Diskon vs profit, diskon per tahun dan kategori |
| `05b_cek_2017.py` | Uji penyebab margin 2017: diskon dan komposisi |
| `05c_cek_subkategori.py` | Perubahan profit per sub-kategori 2016 ke 2017 |
| `05d_cek_machines_tables.py` | Diskon dan margin Machines dan Tables per tahun |
| `05e_cek_transaksi_rugi.py` | Transaksi terburuk Machines dan Tables 2017 |
| `06_eda_segmen.py` | Performa segmen dan pelanggan |
| `06b_cek_pelanggan_rugi.py` | Diskon pelanggan rugi vs untung |
| `07_dampak_diskon.py` | Kontribusi diskon tinggi terhadap total kerugian |