# Tugas Pengolahan Citra dan Video (PCV)

Kumpulan implementasi dasar pengolahan citra digital menggunakan **Python**, **NumPy**, dan **OpenCV**. Sebagian besar algoritma ditulis secara manual (tanpa fungsi bawaan package) untuk memperlihatkan cara kerja di balik setiap operasi.

> **Mata kuliah:** Pengolahan Citra dan Video
> **Penulis:** Anisa Hasna Mufida

---

## Daftar Isi

- [Deskripsi](#deskripsi)
- [Struktur Repository](#struktur-repository)
- [Teknologi](#teknologi)
- [Instalasi](#instalasi)
- [Cara Menjalankan](#cara-menjalankan)
- [Ringkasan Tugas](#ringkasan-tugas)
  - [1. Intro: Membaca, Menampilkan, dan Filter Warna](#1-intro-membaca-menampilkan-dan-filter-warna)
  - [2. Transformasi Intensitas dan Ekualisasi Histogram](#2-transformasi-intensitas-dan-ekualisasi-histogram)
  - [3. Filter Spasial](#3-filter-spasial)
  - [4. Model Warna](#4-model-warna)
  - [5. Operasi Morfologi](#5-operasi-morfologi)
- [Hasil](#hasil)
- [Catatan Penting](#catatan-penting)
- [Troubleshooting](#troubleshooting)
- [Referensi](#referensi)

---

## Deskripsi

Repository ini berisi tugas praktikum Pengolahan Citra dan Video (*repo live code*) yang mencakup lima topik utama:

| No | File | Topik |
|----|------|-------|
| 1 | `1-intro.py` | Membaca citra, menampilkan citra, filter warna pada citra, dan filter warna pada video |
| 2 | `2-ti-eq.py` | Transformasi intensitas dan ekualisasi histogram (tanpa fungsi bawaan package) |
| 3 | `3-filter-spasial.py` | Penerapan filter spasial (smoothing dan sharpening) |
| 4 | `4-model-warna.py` | Konversi model warna RGB ke CMYK, HSI, dan HSV |
| 5 | `5-morphology.py` | Operasi morfologi: erosi, dilasi, opening, closing |

Setiap file dapat dijalankan secara mandiri dan menampilkan hasil pemrosesan.

## Struktur Repository

```
.
├── 1-intro.py              # Baca/tampil citra, filter warna citra & video
├── 2-ti-eq.py              # Transformasi intensitas & ekualisasi histogram
├── 3-filter-spasial.py     # Filter spasial
├── 4-model-warna.py        # Konversi model warna
├── 5-morphology.py         # Operasi morfologi
├── data/
│   ├── chikawa.jpg         # Citra uji
│   └── <video>.mp4         # Video uji (untuk filter warna video)
└── README.md
```

## Teknologi

| Komponen | Kegunaan |
|----------|----------|
| Python 3.8+ | Bahasa pemrograman |
| NumPy | Representasi citra sebagai array dan operasi numerik |
| OpenCV (`cv2`) | Membaca citra dan konversi dasar BGR ke RGB / grayscale |
| Matplotlib | Menampilkan citra dan histogram |
| Spyder | IDE yang digunakan |

## Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/<username>/<nama-repo>.git
   cd <nama-repo>
   ```
2. Install dependensi:
   ```bash
   pip install numpy opencv-python matplotlib
   ```
3. Pastikan citra uji tersedia di `data/chikawa.jpg` (dan video uji di folder `data/` untuk `1-intro.py`).

## Cara Menjalankan

**Melalui Spyder**

1. Buka file `.py` yang diinginkan (**File → Open**).
2. Pastikan *working directory* Spyder menunjuk ke folder induk repository (folder yang berisi `data/`).
3. Tekan **F5** (*Run file*).
4. Hasil tampil di panel **Plots**.

**Melalui terminal**

```bash
python 1-intro.py
python 2-ti-eq.py
python 3-filter-spasial.py
python 4-model-warna.py
python 5-morphology.py
```

> Jalankan perintah dari folder induk repository agar path `data/chikawa.jpg` terbaca.

## Ringkasan Tugas

### 1. Intro: Membaca, Menampilkan, dan Filter Warna

**File:** `1-intro.py`
Pengenalan dasar pengolahan citra dan video menggunakan OpenCV.

| Topik | Keterangan |
|-------|------------|
| Membaca citra | Memuat file citra ke dalam array NumPy dengan `cv2.imread()` |
| Menampilkan citra | Menampilkan citra hasil pembacaan (`cv2.imshow()` atau Matplotlib) |
| Filter warna pada citra | Menyaring atau memisahkan warna tertentu pada citra |
| Filter warna pada video | Menerapkan filter warna yang sama pada setiap frame video |

**Output:** citra asli dan hasil filter warna, serta tampilan video yang sudah difilter.

> Sesuaikan deskripsi di atas dengan isi `1-intro.py` milikmu (misalnya jenis filter warna yang dipakai).

### 2. Transformasi Intensitas dan Ekualisasi Histogram

**File:** `2-ti-eq.py`
Seluruh proses ditulis manual dengan loop piksel, tanpa fungsi bawaan package (OpenCV hanya dipakai untuk membaca citra).

| Fungsi | Rumus | Efek |
|--------|-------|------|
| `negatif` | `s = 255 - r` | Membalik terang dan gelap |
| `log_transform` | `s = c · log(1 + r)` | Mencerahkan area gelap |
| `gamma_transform` | `s = c · r^γ` | Mengatur kecerahan (γ < 1 lebih terang, γ > 1 lebih gelap) |
| `contrast_stretching` | `s = (r - r_min) / (r_max - r_min) · 255` | Meregangkan kontras ke rentang penuh 0 sampai 255 |
| `hitung_histogram` | — | Menghitung jumlah piksel pada tiap level intensitas |
| `ekualisasi_histogram` | `s_k = 255 · CDF(r_k)` | Meratakan sebaran intensitas untuk meningkatkan kontras |

**Alur ekualisasi histogram:** histogram → PDF → CDF → tabel pemetaan (LUT) → terapkan ke setiap piksel.

**Output:** grid 6 citra (asli, negatif, log, gamma, contrast stretching, ekualisasi) dan perbandingan histogram sebelum dan sesudah ekualisasi.

### 3. Filter Spasial

**File:** `3-filter-spasial.py`
Berisi fungsi `konvolusi()` manual (zero padding) yang dipakai oleh semua filter berbasis kernel.

| Filter | Jenis | Keterangan |
|--------|-------|------------|
| Mean 3×3 | Smoothing | Rata-rata tetangga, mengurangi noise |
| Gaussian 5×5 (σ = 1) | Smoothing | Rata-rata berbobot, hasil lebih halus alami |
| Median 3×3 | Smoothing (non-linear) | Efektif untuk noise *salt and pepper* |
| Laplacian | Sharpening | Penajaman dengan `f - Laplacian(f)` |
| Sobel | Deteksi tepi | Magnitudo gradien `√(Gx² + Gy²)` |

**Output:** grid 6 citra (asli dan kelima hasil filter).

### 4. Model Warna

**File:** `4-model-warna.py`
Konversi dari RGB ke model warna lain menggunakan rumus manual berbasis NumPy.

| Model | Komponen | Rentang |
|-------|----------|---------|
| RGB | R, G, B | 0 sampai 255 |
| CMYK | C, M, Y, K | 0 sampai 1 |
| HSV | H, S, V | H: 0 sampai 360°, S dan V: 0 sampai 1 |
| HSI | H, S, I | H: 0 sampai 360°, S dan I: 0 sampai 1 |

**Catatan:** OpenCV membaca citra dalam urutan BGR, sehingga dikonversi ke RGB terlebih dahulu sebelum dihitung.

**Output:** setiap kanal dari tiap model ditampilkan sebagai citra grayscale terpisah.

### 5. Operasi Morfologi

**File:** `5-morphology.py`
Operasi pada citra biner dengan *structuring element* 3×3 yang dapat diubah.

| Operasi | Definisi | Efek |
|---------|----------|------|
| Erosi | Piksel = 1 jika seluruh area SE bernilai 1 | Mengecilkan objek, menghilangkan noise kecil |
| Dilasi | Piksel = 1 jika minimal satu area SE bernilai 1 | Membesarkan objek, menutup celah kecil |
| Opening | Erosi lalu dilasi | Menghapus noise tanpa banyak mengubah ukuran objek |
| Closing | Dilasi lalu erosi | Menutup lubang kecil pada objek |

Citra diubah ke biner dengan ambang (*threshold*) 127.

**Output:** grid 5 citra (biner asli, erosi, dilasi, opening, closing).

## Catatan Penting

- **Kecepatan:** semua operasi memakai loop piksel manual sehingga lambat pada citra besar. Untuk uji coba, perkecil citra, misalnya `img = cv2.resize(img, (320, 240))`.
- **Tipe data:** citra bertipe `uint8`. Perhitungan yang bisa melebihi 255 (misalnya `log`) harus dikonversi ke `float` terlebih dahulu agar tidak terjadi overflow.
- **Grayscale:** `2-ti-eq.py`, `3-filter-spasial.py`, dan `5-morphology.py` bekerja pada citra grayscale (2 dimensi), sedangkan `1-intro.py` dan `4-model-warna.py` pada citra berwarna.
- **Video:** `1-intro.py` memproses video frame demi frame. Tekan tombol keluar yang ditentukan di kode (misalnya `q`) untuk menutup jendela video.

## Troubleshooting

| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| `FileNotFoundError: data/chikawa.jpg` | Path atau working directory salah | Jalankan dari folder induk repository dan pastikan file ada di `data/` |
| `too many values to unpack (expected 2, got 3)` | Citra masih berwarna (3 kanal) | Pastikan sudah dikonversi dengan `cv2.cvtColor(..., cv2.COLOR_BGR2GRAY)` |
| `OverflowError: cannot convert float infinity to integer` | Overflow `uint8` pada `log` | Gunakan `float(img[i, j])` di dalam `np.log` |
| Grafik tidak muncul di Spyder | Grafik ada di panel Plots | Buka tab **Plots**, atau ubah backend di **Tools → Preferences → IPython console → Graphics** |
| Proses sangat lama | Citra terlalu besar | Perkecil citra dengan `cv2.resize` |

## Referensi

- Gonzalez, R. C., & Woods, R. E. *Digital Image Processing*. Pearson.
- Dokumentasi OpenCV: https://docs.opencv.org/
- Dokumentasi NumPy: https://numpy.org/doc/
- Dokumentasi Matplotlib: https://matplotlib.org/stable/

---

<p align="center">Dibuat untuk keperluan tugas mata kuliah Pengolahan Citra dan Video.</p>
