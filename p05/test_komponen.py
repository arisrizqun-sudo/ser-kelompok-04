from komponen import Mikrofon, SensorSuhu, Servo

def test_mikrofon_rata_rata():
    m = Mikrofon("m")
    m.baca(10.0)
    m.baca(30.0)
    assert m.proses() == 20.0

def test_sensor_suhu_tertinggi():
    s = SensorSuhu("s")
    s.baca(30.0)
    s.baca(35.0)
    assert s.proses() == 35.0

def test_servo_dibatasi():
    sv = Servo("sv")
    sv.gerak_ke(200)
    assert sv.proses() == 180