from baca_mentah import baca_mentah
from baca_log import baca_log
from statistik import rata_rata
from galat import galat_relatif
from validasi import dalam_rentang, BATAS_BAWAH, BATAS_ATAS

ACUAN_RATA = 62.4412

mentah = baca_mentah("log_mikrofon.csv")
valid, ditolak = baca_log("log_mikrofon.csv")

for nama, data in [("tanpa validasi", mentah), ("dengan validasi", valid)]:
    rata = rata_rata(data)
    g = galat_relatif(rata, ACUAN_RATA)
    wajar = dalam_rentang(rata, BATAS_BAWAH, BATAS_ATAS)
    print(nama, "| n =", len(data), "| rata =", round(rata, 1), "|",
          "galat =", round(g, 2), "% | wajar:", wajar)