data_suhu = [28.5, 30.2, 29.8, 31.0, 27.9]

def hitung_rata_rata(data):
    total = 0
    for i in range(1, len(data)):          # ← diperbaiki: mulai dari 0
        total = total + data[i]
    return total / len(data)

def cari_tertinggi(data):
    tertinggi = data[0]
    for nilai in data:
        if nilai > tertinggi:
            tertinggi = nilai
    return tertinggi

def cek_status(suhu):
    if suhu > 30:
        return "PANAS"
    elif suhu >= 25:
        return "NORMAL"
    else:
        return "DINGIN"

if __name__ == "__main__":
    rata = hitung_rata_rata(data_suhu)
    print("Rata-rata :", rata)
    print("Tertinggi :", cari_tertinggi(data_suhu))   # ← diperbaiki: typo
    print("Status :", cek_status(rata))
