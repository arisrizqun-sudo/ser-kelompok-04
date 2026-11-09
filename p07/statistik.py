def rata_rata(data):
    return sum(data) / len(data)


def tertinggi(data):
    return max(data)


def terendah(data):
    return min(data)


def rentang(data):
    return (min(data), max(data))


def ringkasan(data):
    return {
        "jumlah": len(data),
        "rata": round(rata_rata(data), 2),
        "min": min(data),
        "maks": max(data),
        "median": median(data),
    }


def median(data):
    urut = sorted(data)
    n = len(urut)

    tengah = n // 2

    if n % 2 == 1:
        return urut[tengah]
    else:
        return (urut[tengah - 1] + urut[tengah]) / 2