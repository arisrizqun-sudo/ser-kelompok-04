from wajah import Wajah
from emosi import Emosi
data_uji = [0.85, 0.2, 0.5, 0.65, 0.05]
wajah = Wajah()
for skor in data_uji:
    e = Emosi(skor)
    label = e.tentukan_label()
    print(f"Skor {skor} -> {label}")
    wajah.set_ekspresi(label)
    wajah.tampilkan()
    print("---")