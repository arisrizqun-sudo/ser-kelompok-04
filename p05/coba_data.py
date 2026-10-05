from statistik import rata_rata, rentang, ringkasan

data_level = [40.0, 55.0, 60.0, 50.0, 70.0, 43.0]

print(len(data_level))
print(data_level[0], data_level[-1])
print(data_level[1:4])
print(sorted(data_level))
print(data_level)
print(rata_rata(data_level))

lo, hi = rentang(data_level)
print(lo, hi)

data_level.append(52.0)
print(len(data_level), round(rata_rata(data_level), 2))

#hasil = rentang(data_level)
#hasil[0] = 0

#print(data_level[10])

data_baru = [10.0, 20.0, 30.0, 40.0]
r = ringkasan(data_baru)
print(r["rata"])

for kunci, nilai in r.items():
    print(kunci, "=", nilai)

r["satuan"] = "dB"

print(len(r))

r["rata"] = 0

print(r)