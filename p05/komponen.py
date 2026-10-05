from perangkat import Sensor, Aktuator
from statistik import rata_rata, tertinggi


class Mikrofon(Sensor):
    def __init__(self, nama):
        super().__init__(nama, "dB")

    def proses(self):
        return rata_rata(self.data)


class SensorSuhu(Sensor):
    def __init__(self, nama):
        super().__init__(nama, "C")

    def proses(self):
        return tertinggi(self.data)


class Servo(Aktuator):
    def gerak_ke(self, sudut):
        if sudut < 0:
            sudut = 0

        if sudut > 180:
            sudut = 180

        self.nilai = sudut

    def proses(self):
        return self.nilai
    
class LampuIndikator(Aktuator):
    def atur(self, persen):
        if persen < 0:
            persen = 0

        if persen > 100:
            persen = 100

        self.nilai = persen

    def proses(self):
        return self.nilai / 100