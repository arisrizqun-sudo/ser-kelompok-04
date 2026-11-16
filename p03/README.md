# Proyek Sistem Otomasi - Job 3

Repositori ini berisi latihan pemrograman Python untuk debugging, pengujian menggunakan `pytest`, dokumentasi kode (*docstring*), serta pengenalan dasar Pemrograman Berorientasi Objek (OOP) untuk memodelkan komponen sistem otomasi seperti Servo dan Mikrofon[cite: 5, 9, 10].

## Deskripsi Program
Program ini mencakup modul perhitungan sensor suhu (`suhu.py`), pengujian otomatis (`test_suhu.py`), serta pemodelan class `Servo` dan `Mikrofon` untuk persiapan proyek akhir sistem robotika[cite: 9, 10].

## Cara Menjalankan Program
Pastikan virtual environment (`.venv`) Anda sudah aktif, lalu jalankan program utama dengan perintah:
```powershell
python suhu.py

Cara Menjalankan Program Test:
python -m pytest -v

Identitas Mahasiswa:
Nama: Mochamad Ainnur Wachid
NIM : 33132501005

# Proyek Pemrograman Terapan - Jobsheet 03

Proyek ini berisi latihan debugging, pengujian unit menggunakan pytest, penulisan dokumentasi, serta pengenalan pemrograman berorientasi objek (OOP) Python untuk memodelkan komponen sistem otomasi.

## Daftar Program & Penjelasan
- `suhu.py`: Program untuk menghitung rata-rata, mencari nilai tertinggi, dan mengecek status suhu dari data sensor.
- `servo.py`: Implementasi class `Servo` untuk memodelkan kendali sudut motor servo pada sistem robot (dilengkapi constructor, atribut, serta method `gerak_ke`, `reset`, `tampilkan`, dan `putar`)[cite: 7].
- `mikrofon.py`: Implementasi class `Mikrofon` untuk memodelkan komponen mikrofon beserta status keaktifan dan pengaturan level sensitivitasnya[cite: 7, 8].

## Cara Menjalankan Program
1. Pastikan terminal berada di dalam folder `p03` dan *virtual environment* (`(.venv)`) sudah aktif.
2. Jalankan program utama dengan perintah:
   ```bash
   python suhu.py
   python servo.py