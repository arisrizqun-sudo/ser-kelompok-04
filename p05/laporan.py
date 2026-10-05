from komponen import Mikrofon, SensorSuhu, Servo, LampuIndikator
from statistik import ringkasan

mik = Mikrofon("mik-1")
suhu = SensorSuhu("suhu-servo")
alis = Servo("alis", 90)

led = LampuIndikator("led-1")
led.atur(60)

data_mik = [40.0, 55.0, 60.0, 50.0, 70.0, 43.0]
data_suhu = [31.5, 36.0, 33.2, 34.8]

for nilai in data_mik:
    mik.baca(nilai)

for nilai in data_suhu:
    suhu.baca(nilai)

alis.gerak_ke(120)

peta = {"mik": mik, "suhu": suhu, "alis": alis, "led": led}

print("=== Hasil proses tiap perangkat ===")
for kunci, p in peta.items():
    p.nyalakan()
    print(kunci, "->", p, "hasil proses =", p.proses())

print("=== Ringkasan data Mikrofon ===")
r = ringkasan(mik.data)
for kunci, nilai in r.items():
    print(kunci, "=", nilai)