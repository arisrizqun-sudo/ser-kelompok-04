class Servo:
    jumlah_servo = 0 # atribut class -- dibagi oleh SELURUH object Servo
    def __init__(self, nama, sudut_awal=90):
        self.nama = nama
        self.sudut = sudut_awal
        Servo.jumlah_servo = Servo.jumlah_servo + 1
    def gerak_ke(self, sudut):
        if sudut < 0:
            sudut = 0
        if sudut > 180:
            sudut = 180
        self.sudut = sudut
    def reset(self):
        self.sudut = 90
    def __str__(self):
        return f"Servo {self.nama}: sudut = {self.sudut} derajat"
if __name__ == "__main__":
    servo_alis = Servo("alis")
    servo_bibir = Servo("bibir", 45)
    print(servo_alis)
    print(servo_bibir)
    print("Jumlah servo yang sudah dibuat:", Servo.jumlah_servo)
    servo_leher = Servo("leher")
    print("Jumlah servo sekarang:", Servo.jumlah_servo)