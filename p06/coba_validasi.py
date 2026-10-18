from validasi import periksa

contoh = ["61.8", " 61.8 ", "", "ERR", "--", "-999", "250",
          "30.0", "29.9", "120", "120.1", "61,8", "6e1", "nan"]

for teks in contoh:
    try:
        nilai = periksa(teks)
        print(repr(teks), "-> diterima", nilai)
    except ValueError as e:
        print(repr(teks), "-> ditolak:", e)