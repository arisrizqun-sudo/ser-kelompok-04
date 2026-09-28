from servo import Servo
PRESET_EKSPRESI = {
    "senang": {"alis": 60, "bibir": 150},
    "sedih": {"alis": 120, "bibir": 40},
    "netral": {"alis": 90, "bibir": 90},
}
class Wajah:
    def __init__(self):
        self.alis = Servo("alis", 90)
        self.bibir = Servo("bibir", 90)
    def set_ekspresi(self, nama):
            if nama not in PRESET_EKSPRESI:
                print(f"Ekspresi '{nama}' tidak dikenali, dipakai 'netral'")
                nama = "netral"
            sudut = PRESET_EKSPRESI[nama]
            self.alis.gerak_ke(sudut["alis"])
            self.bibir.gerak_ke(sudut["bibir"])
    def tampilkan(self):
            print(self.alis)
            print(self.bibir)
if __name__ == "__main__":
    wajah = Wajah()
    wajah.tampilkan()
    wajah.set_ekspresi("senang")
    wajah.tampilkan()
    wajah.set_ekspresi("marah")
    wajah.tampilkan()
