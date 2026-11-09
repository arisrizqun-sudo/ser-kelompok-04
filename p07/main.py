from komponen import Mikrofon, SensorSuhu, Servo

mik = Mikrofon("mik-1")
suhu = SensorSuhu("suhu-servo")
alis = Servo("alis", 90)

mik.baca(40.0)
mik.baca(55.0)
mik.baca(70.0)

suhu.baca(31.5)
suhu.baca(36.0)
suhu.baca(33.2)

alis.gerak_ke(120)

daftar = [mik, suhu, alis]

for p in daftar:
    p.nyalakan()
    hasil = p.proses()
    print(p, "->", hasil)