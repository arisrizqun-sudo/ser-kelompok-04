import numpy as np
from audio import hitung_dbfs, ke_level_db

uji = [
    ("konstan 0.1", np.full(100, 0.1)),
    ("konstan 0.01", np.full(100, 0.01)),
    ("konstan 0.001", np.full(100, 0.001)),
    ("konstan 0.5", np.full(100, 0.5)),
    ("nol semua", np.zeros(100)),
]

for nama, sinyal in uji:
    try:
        print(nama, "->", round(hitung_dbfs(sinyal), 2), "dBFS ->",
              ke_level_db(sinyal), "dB")
    except ValueError as e:
        print(nama, "-> ditolak:", e)