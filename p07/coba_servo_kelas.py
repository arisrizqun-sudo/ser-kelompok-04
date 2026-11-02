import pin_tiruan
import servo_layar
from komponen import Servo

alis = Servo("alis", 90, pin=18)
print(alis, alis.proses(), alis.lebar_pulsa())

for sudut in [0, 90, 180, 60.5]:
    alis.gerak_ke(sudut)
    print("sudut", sudut, "| lebar", alis.lebar_pulsa(), "ms")

for sudut in [-5, 181, 180.1, float("nan")]:
    try:
        alis.gerak_ke(sudut)
    except ValueError as e:
        print("ditolak:", sudut, "|", e, "| servo tetap di",
              alis.proses(), "|", alis.lebar_pulsa(), "ms")