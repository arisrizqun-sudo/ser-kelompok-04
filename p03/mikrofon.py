class Mikrofon:
    def __init__(self, nama):
        self.nama = nama
        self.aktif = False
        self.level = 0

    def nyalakan(self):
        self.aktif = True

    def matikan(self):
        self.aktif = False
        self.level = 0

    def set_level(self, nilai):
        if self.aktif:
            self.level = nilai