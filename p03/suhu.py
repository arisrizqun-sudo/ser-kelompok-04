data_suhu = [28.5, 30.2, 29.8, 31.0, 27.9]

def hitung_rata_rata(data):
    """Menghitung rata-rata dari sebuah list angka.

    Input : data (list angka)
    Output: rata-rata (float)
    """
    return sum(data) / len(data)


def cari_tertinggi(data):
    """Mencari nilai tertinggi dari sebuah list angka.

    Input : data (list angka)
    Output: nilai tertinggi (int/float)
    """
    return max(data)


def cek_status(suhu):
    """Menentukan status suhu berdasarkan batas kategori:
    - > 30       : PANAS
    - 21 - 30    : NORMAL
    - <= 20      : DINGIN

    Input : suhu (int/float)
    Output: status suhu (str)
    """
    if suhu > 30:
        return "PANAS"
    elif suhu >= 21:
        return "NORMAL"
    else:
        return "DINGIN"