# 🎓 Dashboard Analisis Profil Mahasiswa

## Deskripsi Project

Dashboard Analisis Profil Mahasiswa merupakan project visualisasi data yang dibuat untuk memenuhi tugas **Visualisasi Data – Case 2**.

Project ini bertujuan untuk mengolah, menganalisis, dan menyajikan data akademik mahasiswa dalam bentuk visualisasi interaktif menggunakan Python dan Streamlit. Dashboard ini membantu pengguna memahami distribusi mahasiswa berdasarkan jurusan, semester, usia, serta pencapaian Indeks Prestasi Kumulatif (IPK).

Data yang digunakan merupakan data sintetis sebanyak 1.000 mahasiswa yang dibuat menggunakan Python.

## Tujuan Project

1. Mengolah dan mengeksplorasi data profil mahasiswa.
2. Menampilkan informasi akademik mahasiswa dalam bentuk visualisasi.
3. Menganalisis distribusi mahasiswa berdasarkan jurusan dan semester.
4. Menampilkan gambaran pencapaian akademik berdasarkan IPK.
5. Menyediakan dashboard interaktif untuk membantu memahami karakteristik data mahasiswa.

## Fitur Dashboard

Dashboard ini memiliki beberapa fitur utama:

- **Informasi Statistik (KPI):** Menampilkan total mahasiswa, rata-rata IPK, IPK tertinggi, rata-rata usia, dan jumlah mahasiswa dengan IPK di atas 3,50.
- **Distribusi Mahasiswa per Semester:** Menampilkan jumlah mahasiswa berdasarkan semester.
- **Jumlah Mahasiswa per Jurusan:** Menampilkan distribusi mahasiswa pada setiap jurusan.
- **Proporsi Prestasi IPK:** Menampilkan kategori pencapaian IPK mahasiswa.
- **Hubungan Semester dan IPK:** Menampilkan hubungan antara semester dengan nilai IPK menggunakan Scatter Plot.
- **Distribusi IPK:** Menampilkan persebaran nilai IPK mahasiswa menggunakan Histogram.
- **Sebaran Usia Mahasiswa:** Menampilkan distribusi usia dan outlier berdasarkan jurusan menggunakan Box Plot.
- **Ringkasan Performa Akademik:** Menampilkan tabel statistik akademik untuk setiap jurusan.
- **Data Mahasiswa:** Menampilkan keseluruhan data mahasiswa melalui tabel interaktif.
- **Filter Interaktif:** Memungkinkan pengguna menyaring data berdasarkan jurusan, rentang semester, dan kategori IPK.

## Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman |
| JupyterLab | Pengolahan dan pembuatan dataset |
| Pandas | Pengolahan data |
| NumPy | Pembuatan data sintetis |
| Streamlit | Pembuatan dashboard interaktif |
| Plotly | Visualisasi data |
| Git & GitHub | Pengelolaan dan penyimpanan project |

## Struktur Project

```text
CASE2/
│
├── analisis_data.ipynb
├── app.py
├── dataset_mahasiswa.csv
├── requirements.txt
└── README.md
```

## Dataset

Dataset yang digunakan bernama `dataset_mahasiswa.csv` dengan jumlah 1.000 data sintetis mahasiswa.

Dataset memiliki empat atribut utama:

| Atribut | Keterangan |
|---|---|
| Jurusan | Program studi mahasiswa |
| Semester | Semester mahasiswa (1–8) |
| IPK | Indeks Prestasi Kumulatif |
| Usia | Usia mahasiswa dalam tahun |

Data sintetis dibuat menggunakan Python dengan bantuan library Pandas dan NumPy.

## Instalasi dan Menjalankan Project

### 1. Clone Repository

```bash
git clone https://github.com/yenseason/CASE2-Analisis-Mahasiswa.git
```

### 2. Masuk ke Folder Project

```bash
cd CASE2-Analisis-Mahasiswa
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Dashboard

```bash
streamlit run app.py
```

Dashboard akan berjalan melalui browser menggunakan alamat lokal yang diberikan oleh Streamlit.

## Dashboard Online

Aplikasi dapat diakses melalui Streamlit Community Cloud:

**Link Dashboard:** [Tambahkan link Streamlit setelah deployment berhasil]

## Repository

GitHub: https://github.com/yenseason/CASE2-Analisis-Mahasiswa

---

**Project Visualisasi Data – Case 2**

Dashboard Analisis Profil Mahasiswa