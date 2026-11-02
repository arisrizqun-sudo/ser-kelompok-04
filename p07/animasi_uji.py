import pin_tiruan
import servo_layar
from komponen import Mikrofon, Servo
from pemetaan import level_ke_sudut

mik = Mikrofon("mik-1")
mulut = Servo("mulut", 0, pin=18)

# Ganti sementara LEVEL_UJI dengan ini:
LEVEL_UJI = [30.0, 60.0, 75.0, 120.0, 125.0]

for level in LEVEL_UJI:
    try:
        mik.baca(level)
        sudut = level_ke_sudut(level)
        mulut.gerak_ke(sudut)
        print("level", level, "-> sudut", sudut, "| lebar", mulut.lebar_pulsa(), "ms")
    except ValueError as e:
        print("level", level, "-> ditolak:", e)

print("Data tersimpan:", len(mik.data), "| rata-rata:", round(mik.proses(), 2))