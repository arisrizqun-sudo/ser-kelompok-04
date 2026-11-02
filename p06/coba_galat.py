from galat import galat_absolut, galat_relatif, status

pasangan = [(52.5, 50.0), (100.25, 100.0), (45.0, 60.0), (7.0, 0)]

for hasil, acuan in pasangan:
    try:
        g = galat_relatif(hasil, acuan)
        print(hasil, acuan, "|", galat_absolut(hasil, acuan), "|",
              g, "% |", status(g))
    except ValueError as e:
        print(hasil, acuan, "| error:", e)