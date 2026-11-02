from komponen import Mikrofon, SensorSuhu, Servo, LampuIndikator

mik = Mikrofon("mik-1")
suhu = SensorSuhu("suhu-servo")
alis = Servo("alis", 90)
lampu = LampuIndikator("lampu")

mik.baca(40.0)
mik.baca(55.0)
mik.baca(70.0)

suhu.baca(31.5)
suhu.baca(36.0)
suhu.baca(33.2)

alis.gerak_ke(120)

lampu = LampuIndikator("lampu")

lampu.atur(80)
print("Lampu 80:", lampu.proses())

lampu.atur(150)
print("Lampu 150:", lampu.proses())

lampu.atur(-5)
print("Lampu -5:", lampu.proses())

daftar = [mik, suhu, alis]

for p in daftar:
    p.nyalakan()
    hasil = p.proses()
    print(p, "->", hasil)