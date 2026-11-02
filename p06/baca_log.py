from validasi import periksa


def baca_log(nama_file="log_mikrofon.csv"):
    valid = []
    ditolak = []

    with open(nama_file, encoding="utf-8") as file:
        next(file)
        for nomor, baris in enumerate(file, start=2):
            isi = baris.strip()
            kolom = isi.split(",")

            if len(kolom) != 2:
                ditolak.append((nomor, isi, "jumlah kolom bukan dua"))
                continue

            try:
                valid.append(periksa(kolom[1]))
            except ValueError as e:
                ditolak.append((nomor, isi, str(e)))

    return valid, ditolak


def hitung_alasan(ditolak):
    jumlah = {}

    for nomor, baris, alasan in ditolak:
        jumlah[alasan] = jumlah.get(alasan, 0) + 1

    return jumlah