BATAS_BAWAH = 30.0
BATAS_ATAS = 120.0

# BAGIAN A
def ke_angka(nilai):
    try:
        return float(nilai.strip())
    except ValueError:
        raise ValueError("bukan angka")


# BAGIAN B
def dalam_rentang(nilai, bawah, atas):
    return bawah <= nilai <= atas


# BAGIAN C
def periksa(nilai, bawah=BATAS_BAWAH, atas=BATAS_ATAS):
    angka = ke_angka(nilai)

    if not dalam_rentang(angka, bawah, atas):
        raise ValueError("di luar rentang")

    return angka