# Klasifikasi Buah Kopi

Aplikasi web sederhana menggunakan Flask dan TensorFlow/Keras untuk mengklasifikasikan gambar buah kopi. Pengguna dapat mengunggah gambar, dan aplikasi akan memprediksi jenis buah kopi berdasarkan model yang telah dilatih.

## Struktur Proyek

```projectcv-app/
├── static/
│   ├── uploads/                # Folder untuk menyimpan gambar yang diunggah
│   │   └── buah_kopi.jpeg
│   └── style.css               # File styling CSS untuk tampilan aplikasi
├── templates/
│   └── index.html              # Template HTML untuk antarmuka pengguna
├── app.py                      # Logika aplikasi Flask utama
├── label_map.json              # File JSON yang memetakan indeks kelas ke nama label
├── model.h5                    # Model Keras yang telah dilatih untuk klasifikasi
└── venv/                       # (Opsional) Lingkungan virtual Python
└── requirements.txt            # Daftar dependensi Python
```

## Fitur

* Unggah gambar buah kopi.
* Prediksi jenis buah kopi menggunakan model `model.h5`.
* Menampilkan hasil prediksi (label) dan gambar yang diunggah.

## Persyaratan Sistem

* Python 3.x
* PIP (manajer paket Python)

## Instalasi

Ikuti langkah-langkah di bawah ini untuk mengatur dan menjalankan aplikasi di lingkungan lokal Anda.

### 1. Klon Repositori (Jika Ada) atau Buat Struktur Folder

Jika ini adalah proyek baru, buat struktur folder seperti yang ditunjukkan di bagian "Struktur Proyek".

### 2. Buat Lingkungan Virtual (Opsional, tapi Direkomendasikan)

Membuat lingkungan virtual akan mengisolasi dependensi proyek Anda dari instalasi Python global.

Buka terminal di direktori `projectcv-app` Anda dan jalankan perintah berikut:

bash
'python -m venv venv'


Tentu, ini README.md untuk proyek klasifikasi buah kopi Anda:

Markdown

# Klasifikasi Buah Kopi

Aplikasi web sederhana menggunakan Flask dan TensorFlow/Keras untuk mengklasifikasikan gambar buah kopi. Pengguna dapat mengunggah gambar, dan aplikasi akan memprediksi jenis buah kopi berdasarkan model yang telah dilatih.

## Struktur Proyek

projectcv-app/
├── static/
│   ├── uploads/                # Folder untuk menyimpan gambar yang diunggah
│   │   └── buah_kopi.jpeg
│   └── style.css               # File styling CSS untuk tampilan aplikasi
├── templates/
│   └── index.html              # Template HTML untuk antarmuka pengguna
├── app.py                      # Logika aplikasi Flask utama
├── label_map.json              # File JSON yang memetakan indeks kelas ke nama label
├── model.h5                    # Model Keras yang telah dilatih untuk klasifikasi
└── venv/                       # (Opsional) Lingkungan virtual Python
└── requirements.txt            # Daftar dependensi Python


## Fitur

* Unggah gambar buah kopi.
* Prediksi jenis buah kopi menggunakan model `model.h5`.
* Menampilkan hasil prediksi (label) dan gambar yang diunggah.

## Persyaratan Sistem

* Python 3.x
* PIP (manajer paket Python)



