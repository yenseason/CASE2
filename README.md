# Dashboard Analisis Profil Mahasiswa — CASE2

## Identitas Mahasiswa

| Keterangan | Informasi |
|---|---|
| Nama | Neysalva Calista Firlin |
| NPM | 241051005 |
| Mata Kuliah | Visualisasi Data |
| Program Studi | Sistem Informasi |

## 1. Deskripsi Proyek

CASE2 merupakan proyek visualisasi data yang berfokus pada analisis profil mahasiswa menggunakan Python. Proyek ini dikembangkan dengan memanfaatkan Streamlit sebagai framework untuk membangun dashboard interaktif yang menyajikan informasi mengenai karakteristik mahasiswa berdasarkan data yang tersedia.

Dashboard ini bertujuan untuk membantu pengguna memahami gambaran profil mahasiswa melalui penyajian data dalam bentuk ringkasan statistik, tabel, dan visualisasi grafis yang lebih informatif.

## 2. Latar Belakang

Data mahasiswa memiliki berbagai informasi yang dapat digunakan untuk memahami karakteristik dan kondisi akademik mahasiswa. Namun, data yang hanya disajikan dalam bentuk tabel akan membutuhkan waktu lebih lama untuk dipahami, terutama ketika jumlah data cukup banyak.

Oleh karena itu, diperlukan visualisasi data untuk menyajikan informasi secara lebih menarik, terstruktur, dan mudah dipahami.

Melalui proyek CASE2, data profil mahasiswa diolah dan ditampilkan dalam dashboard interaktif sehingga pengguna dapat melihat distribusi mahasiswa berdasarkan jurusan, semester, usia, serta informasi mengenai Indeks Prestasi Kumulatif (IPK).

## 3. Tujuan Proyek

- Melakukan pengolahan dan analisis terhadap dataset profil mahasiswa.
- Menyajikan informasi karakteristik mahasiswa melalui visualisasi data.
- Mengetahui distribusi mahasiswa berdasarkan jurusan dan semester.
- Menampilkan gambaran informasi akademik mahasiswa berdasarkan nilai IPK.
- Mengidentifikasi pola dan karakteristik mahasiswa berdasarkan data yang tersedia.
- Mengembangkan dashboard interaktif sebagai media penyajian hasil analisis data.

## 4. Visualisasi yang Digunakan

Visualisasi dalam dashboard CASE2 digunakan untuk membantu pengguna memahami karakteristik mahasiswa melalui beberapa bentuk penyajian data, antara lain:

1. **Distribusi Mahasiswa Berdasarkan Jurusan**  
   Menampilkan persebaran jumlah mahasiswa pada masing-masing jurusan.

2. **Distribusi Mahasiswa Berdasarkan Semester**  
   Menampilkan jumlah mahasiswa berdasarkan semester yang sedang ditempuh.

3. **Visualisasi IPK Mahasiswa**  
   Menyajikan gambaran nilai IPK mahasiswa untuk membantu memahami kondisi akademik berdasarkan dataset.

4. **Distribusi Usia Mahasiswa**  
   Menampilkan persebaran usia mahasiswa berdasarkan data yang tersedia.

5. **Ringkasan Statistik Mahasiswa**  
   Menampilkan informasi umum mengenai jumlah mahasiswa dan karakteristik data yang dianalisis.

## 5. Fitur Dashboard

Dashboard CASE2 memiliki beberapa fitur utama, yaitu:

- **Ringkasan Data Mahasiswa:** Menampilkan informasi umum mengenai dataset mahasiswa.
- **Analisis Jurusan:** Menampilkan distribusi mahasiswa berdasarkan jurusan.
- **Analisis Semester:** Menampilkan persebaran mahasiswa berdasarkan semester.
- **Analisis IPK:** Menyajikan informasi mengenai nilai akademik mahasiswa.
- **Analisis Usia:** Menampilkan distribusi usia mahasiswa.
- **Visualisasi Interaktif:** Menyajikan informasi melalui grafik yang dapat membantu pengguna memahami data.
- **Tabel Data Mahasiswa:** Menampilkan data mahasiswa sebagai informasi pendukung analisis.

## 6. Hasil Analisis Awal

Berdasarkan dataset profil mahasiswa yang digunakan, terdapat sebanyak **1.000 data mahasiswa** dengan beberapa atribut utama, yaitu jurusan, semester, IPK, dan usia.

Dari data tersebut, analisis awal dapat dilakukan untuk memperoleh gambaran mengenai:

- Persebaran jumlah mahasiswa berdasarkan jurusan.
- Komposisi mahasiswa berdasarkan semester.
- Gambaran nilai IPK mahasiswa.
- Distribusi usia mahasiswa.

Hasil visualisasi membantu menyajikan karakteristik mahasiswa secara lebih terstruktur sehingga informasi dalam dataset dapat dipahami dengan lebih mudah.

## 7. Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman untuk pengolahan data dan pengembangan aplikasi |
| Jupyter Notebook | Lingkungan untuk melakukan analisis data |
| Pandas | Mengolah dan memanipulasi dataset |
| NumPy | Mendukung operasi pengolahan data numerik |
| Streamlit | Membangun dashboard interaktif |
| Plotly | Membuat visualisasi data interaktif |
| Git | Mengelola versi proyek |
| GitHub | Menyimpan dan membagikan source code proyek |

## 8. Live Dashboard

Dashboard CASE2 dikembangkan menggunakan Streamlit Community Cloud agar dapat diakses secara online.

**Link Dashboard:** https://profil-mahasiswa-yenseason.streamlit.app/

## 9. Struktur Folder

```text
CASE2-Analisis-Mahasiswa/
│
├── analisis_data.ipynb
├── app.py
├── dataset_mahasiswa.csv
├── requirements.txt
└── README.md
```

Keterangan:
- `analisis_data.ipynb` : File notebook untuk proses analisis dan pengolahan data mahasiswa.
- `app.py` : File utama untuk menjalankan aplikasi dashboard Streamlit.
- `dataset_mahasiswa.csv` : Dataset yang digunakan dalam analisis profil mahasiswa.
- `requirements.txt` : Daftar library Python yang diperlukan.
- `README.md` : Dokumentasi proyek.

## 10. Cara Menjalankan Secara Lokal

Untuk menjalankan dashboard CASE2 pada komputer lokal, ikuti langkah berikut:

**1. Clone repository GitHub**

```bash
git clone https://github.com/yenseason/CASE2-Analisis-Mahasiswa.git
```

**2. Masuk ke direktori proyek**

```bash
cd CASE2-Analisis-Mahasiswa
```

**3. Install seluruh library yang dibutuhkan**

```bash
pip install -r requirements.txt
```

**4. Jalankan aplikasi Streamlit**

```bash
streamlit run app.py
```

**5. Buka dashboard**

Setelah aplikasi berjalan, buka alamat lokal yang ditampilkan pada terminal, biasanya:

```text
http://localhost:8501
```

## 11. Repository GitHub

Source code dan seluruh file proyek CASE2 dapat diakses melalui repository berikut:

https://github.com/yenseason/CASE2-Analisis-Mahasiswa
