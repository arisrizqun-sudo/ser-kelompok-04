from validasi import dalam_rentang, BATAS_BAWAH, BATAS_ATAS

def level_ke_sudut(level):
    if not dalam_rentang(level, BATAS_BAWAH, BATAS_ATAS):
        raise ValueError("level di luar rentang")
    sudut = (level - BATAS_BAWAH) / (BATAS_ATAS - BATAS_BAWAH) * 180
    return round(sudut, 1)