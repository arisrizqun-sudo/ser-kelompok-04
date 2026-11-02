from validasi import periksa

def baca_log(nama_berkas):
    valid = []
    ditolak = []
    with open(nama_berkas) as berkas:
        next(berkas)
        for no, baris in enumerate(berkas, start=2):
            baris = baris.strip()
            kolom = baris.split(",")
            if len(kolom) != 2:
                ditolak.append((no, baris, "jumlah kolom salah"))
                continue
            try:
                valid.append(periksa(kolom[1]))
            except ValueError as e:
                ditolak.append((no, baris, str(e)))
                
    return valid, ditolak  # <-- Pastikan posisi return sejajar dengan "valid = []" di atas

def hitung_alasan(ditolak):
    jumlah = {}
    for no, isi, alasan in ditolak:
        jumlah[alasan] = jumlah.get(alasan, 0) + 1
    return jumlah