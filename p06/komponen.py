from perangkat import Sensor, Aktuator
from statistik import rata_rata, tertinggi
from validasi import dalam_rentang, BATAS_BAWAH, BATAS_ATAS

class Mikrofon(Sensor):
    def __init__(self, nama):
        super().__init__(nama, "dB")

    def baca(self, nilai):
        if not dalam_rentang(nilai, BATAS_BAWAH, BATAS_ATAS):
            raise ValueError("level di luar rentang mikrofon")
        super().baca(nilai)

    def proses(self):
        if len(self.data) == 0:
            raise ValueError("Mikrofon belum memiliki data")
        return rata_rata(self.data)


class SensorSuhu(Sensor):
    def __init__(self, nama):
        super().__init__(nama, "C")

    def proses(self):
        return tertinggi(self.data)


class Servo(Aktuator):
    def gerak_ke(self, sudut):
        if sudut < 0 or sudut > 180:
            raise ValueError("sudut harus 0 sampai 180")

        self.nilai = sudut

    def proses(self):
        return self.nilai