from galat import galat_absolut, galat_relatif, status

pasangan = [
    (52.5, 50.0),
    (100.25, 100.0),
    (45.0, 60.0),
    (7.0, 0)
]

for hasil, acuan in pasangan:
    try:
        ga = galat_absolut(hasil, acuan)
        gr = galat_relatif(hasil, acuan)
        st = status(gr)
        print(f"Hasil: {hasil}, Acuan: {acuan} -> Absolut: {ga}, Relatif: {gr:.2f}%, Status: {st}")
    except ValueError as e:
        print(f"Hasil: {hasil}, Acuan: {acuan} -> Ditolak: {e}")