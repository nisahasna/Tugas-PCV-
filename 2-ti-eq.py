# -*- coding: utf-8 -*-
"""
Transformasi Intensitas dan Ekualisasi Histogram
(tanpa fungsi bawaan package untuk proses utamanya)
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


# ---------- Transformasi intensitas (manual, pakai loop) ----------
def negatif(img):
    h, w = img.shape
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            out[i, j] = 255 - img[i, j]
    return out


def log_transform(img, c=None):
    h, w = img.shape
    if c is None:
        c = 255 / np.log(1 + 255)
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            out[i, j] = min(255, int(c * np.log(1 + float(img[i, j]))))
    return out


def gamma_transform(img, gamma=0.5, c=1.0):
    h, w = img.shape
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            r = img[i, j] / 255.0
            out[i, j] = min(255, int(255 * c * (r ** gamma)))
    return out


def contrast_stretching(img):
    r_min, r_max = int(img.min()), int(img.max())
    h, w = img.shape
    if r_max == r_min:  # gambar polos, tidak ada yang diregangkan
        return img.copy()
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            out[i, j] = int((int(img[i, j]) - r_min) / (r_max - r_min) * 255)
    return out


# ---------- Histogram & ekualisasi (manual) ----------
def hitung_histogram(img):
    hist = np.zeros(256, dtype=int)
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            hist[img[i, j]] += 1
    return hist


def ekualisasi_histogram(img):
    h, w = img.shape
    total = h * w
    hist = hitung_histogram(img)

    pdf = hist / total                 # probabilitas tiap level
    cdf = np.zeros(256)                # kumulatif
    kumulatif = 0
    for k in range(256):
        kumulatif += pdf[k]
        cdf[k] = kumulatif

    lut = np.zeros(256, dtype=np.uint8)  # tabel pemetaan s_k = 255 * cdf
    for k in range(256):
        lut[k] = round(255 * cdf[k])

    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            out[i, j] = lut[img[i, j]]
    return out


if __name__ == "__main__":
    image = cv2.imread('data/chikawa.jpg')
    if image is None:
        raise FileNotFoundError("data/chikawa.jpg tidak ditemukan")
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # versi grayscale untuk diproses

    hasil = {
        "Asli": img,
        "Negatif": negatif(img),
        "Log": log_transform(img),
        "Gamma 0.5": gamma_transform(img, 0.5),
        "Contrast Stretching": contrast_stretching(img),
        "Ekualisasi Histogram": ekualisasi_histogram(img),
    }

    # Tampilkan gambar
    plt.figure(figsize=(14, 8))
    for n, (judul, im) in enumerate(hasil.items(), 1):
        plt.subplot(2, 3, n)
        plt.imshow(im, cmap="gray", vmin=0, vmax=255)
        plt.title(judul)
        plt.axis("off")
    plt.tight_layout()
    plt.show()

    # Bandingkan histogram sebelum & sesudah ekualisasi
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.bar(range(256), hitung_histogram(img))
    plt.title("Histogram Asli")
    plt.subplot(1, 2, 2)
    plt.bar(range(256), hitung_histogram(hasil["Ekualisasi Histogram"]))
    plt.title("Histogram Setelah Ekualisasi")
    plt.tight_layout()
    plt.show()