from baca_log import baca_log, hitung_alasan
from statistik import ringkasan

valid, ditolak = baca_log("log_rekam.csv")
print("Data valid   :", len(valid))
print("Data ditolak:", len(ditolak))
print(hitung_alasan(ditolak))
if len(valid) > 0:
    print(ringkasan(valid))