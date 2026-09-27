class Servo:
    def __init__(self, nama, sudut_awal=90):
        self.nama = nama
        self.sudut = sudut_awal
 
    def gerak_ke(self, sudut):
        if sudut < 0:
            sudut = 0
        if sudut > 180:
            sudut = 180
        self.sudut = sudut
 
    def reset(self):
        self.sudut = 90
 
    def tampilkan(self):
        print(f"Servo {self.nama}: sudut = {self.sudut} derajat")
 
 
if __name__ == "__main__":
    servo_alis = Servo("alis")
    servo_bibir = Servo("bibir", 45)
    servo_alis.gerak_ke(120)
    servo_alis.tampilkan()
    servo_bibir.tampilkan()
    servo_alis.gerak_ke(200)
    servo_alis.tampilkan()