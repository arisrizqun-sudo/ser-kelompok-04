from audio import daftar_masukan, rekam, ke_level_db

masukan = daftar_masukan()
print("Perangkat input terdeteksi:", len(masukan))
for no, nama in masukan:
    print(" ", no, "|", nama)

print("Rekam 2 detik, silakan berbicara...")
sinyal = rekam(2.0)
print("Jumlah sampel:", len(sinyal))
print("Nilai terkecil:", round(float(sinyal.min()), 4),
      "| terbesar:", round(float(sinyal.max()), 4))
print("Level:", ke_level_db(sinyal), "dB")