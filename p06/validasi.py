BATAS_BAWAH = 30.0
BATAS_ATAS = 120.0

def ke_angka(teks):
    teks = teks.strip()
    if teks == "":
        raise ValueError("kosong")
    try:
        return float(teks)
    except ValueError:
        raise ValueError("bukan angka")

def dalam_rentang(nilai, bawah, atas):
    return bawah < nilai < atas

def periksa(teks, bawah=BATAS_BAWAH, atas=BATAS_ATAS):
    nilai = ke_angka(teks)
    if not dalam_rentang(nilai, bawah, atas):
        raise ValueError("di luar rentang")
    return nilai        