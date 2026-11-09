class Perangkat:
    def __init__(self, nama):
        self.nama = nama
        self.aktif = False

    def nyalakan(self):
        self.aktif = True

    def matikan(self):
        self.aktif = False

    def proses(self):
        raise NotImplementedError("Class turunan harus menulis proses()")

    def __str__(self):
        if self.aktif:
            status = "ON"
        else:
            status = "OFF"
        return f"{self.nama} [{status}]"


class Sensor(Perangkat):
    def __init__(self, nama, satuan):
        super().__init__(nama)
        self.satuan = satuan
        self.data = []

    def baca(self, nilai):
        self.data.append(nilai)


class Aktuator(Perangkat):
    def __init__(self, nama, nilai_awal=0):
        super().__init__(nama)
        self.nilai = nilai_awal