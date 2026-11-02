from validasi import periksa

contoh = [
    "61.8",
    " 61.8 ",
    "ERR",
    "",
    "-999",
    "30.0",
    "29.9",
    "120.0",
    "120.1",
    "75.5",
    "0"
]

for nilai in contoh:
    try:
        hasil = periksa(nilai)
        print(nilai, "diterima:", hasil)
    except ValueError as e:
        print(nilai, "ditolak:", e)