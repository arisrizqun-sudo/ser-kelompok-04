import numpy as np
import sounddevice as sd

LAJU_CUPLIK = 16000
OFFSET_DB = 60.0

def daftar_masukan():
    hasil = []
    for no, perangkat in enumerate(sd.query_devices()):
        if perangkat["max_input_channels"] > 0:
            hasil.append((no, perangkat["name"]))
    return hasil

def rekam(detik):
    jumlah = int(detik * LAJU_CUPLIK)
    data = sd.rec(jumlah, samplerate=LAJU_CUPLIK, channels=1,
                  dtype="float32")
    sd.wait()
    return data[:, 0]

def ke_level_db(sinyal):
    return round(float(hitung_dbfs(sinyal)) + OFFSET_DB, 1)

def hitung_dbfs(sinyal):
    rms = float(np.sqrt(np.mean(np.square(sinyal))))
    if rms == 0.0:
        raise ValueError("sinyal kosong, RMS sama dengan 0")
    return 20 * np.log10(rms)