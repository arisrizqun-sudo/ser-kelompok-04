from baca_log import baca_log, hitung_alasan

valid, ditolak = baca_log("log_mikrofon.csv")

print("Data valid :", len(valid))
print("Data ditolak:", len(ditolak))
for no, isi, alasan in ditolak:
    print(" baris", no, "|", isi, "|", alasan)
print(hitung_alasan(ditolak))