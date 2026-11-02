def baca_mentah(nama_berkas):
  data = []
  with open(nama_berkas) as berkas:
    next(berkas)
    for baris in berkas:
      try:
        waktu, level = baris.strip().split(",")
        data.append(float(level))
      except ValueError:
        pass
  return data