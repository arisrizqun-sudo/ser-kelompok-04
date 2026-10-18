def galat_absolut(hasil, acuan):
    return abs(hasil - acuan)

def galat_relatif(hasil, acuan):
    if acuan == 0:
        raise ValueError("acuan 0, galat relatif tidak dapat dihitung")
    return (galat_absolut(hasil, acuan) / abs(acuan)) * 100

TOLERANSI = 0.5

def status(galat_persen):
    if galat_persen <= TOLERANSI:
        return "LULUS"
    return "TIDAK LULUS"