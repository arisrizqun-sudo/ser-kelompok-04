import pin_tiruan
import servo_layar
from komponen import Mikrofon, Servo
from audio import rekam, ke_level_db
from pemetaan import level_ke_sudut

DURASI = 0.5
JUMLAH = 12

mik = Mikrofon("mik-1")
mulut = Servo("mulut", 0, pin=18)

with open("log_rekam.csv", "w") as log:
    log.write("waktu_ms,level_db\n")
    for i in range(JUMLAH):
        waktu = int(i * DURASI * 1000)
        teks = ""
        try:
            level = ke_level_db(rekam(DURASI))
            teks = str(level)
            mik.baca(level)
            mulut.gerak_ke(level_ke_sudut(level))
            print(waktu, "ms | level", level, "dB | sudut", mulut.proses())
        except ValueError as e:
            print(waktu, "ms | ditolak:", e)
        log.write(f"{waktu},{teks}\n")