def baca_mentah(nama_berkas):
    data = []
    with open(nama_berkas) as berkas:
        next(berkas)
        for baris in berkas:
            try:
                waktu, level = baris.strip().split(",")
                data.append(float(level))
            except ValueError:
                print("dilewati:", baris.strip()) # Diubah dari pass
    return data

if __name__ == "__main__":
    data = baca_mentah("log_mikrofon.csv")
    print("jumlah data:", len(data))
    print("min:", min(data), "| maks:", max(data))
    print("rata-rata:", sum(data) / len(data))