import pin_tiruan
from gpiozero import AngularServo

servo = AngularServo(18, min_angle=0, max_angle=180)

for sudut in [0, 45, 90, 135, 180, 135, 90, 45, 0]:
    servo.angle = sudut
    lebar = servo.pulse_width * 1000
    print("sudut", sudut, "| posisi", round(servo.angle, 1), "| lebar pulsa", round(lebar, 3), "ms")