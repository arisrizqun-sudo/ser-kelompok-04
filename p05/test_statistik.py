from statistik import rata_rata, rentang, ringkasan, median

def test_rata_rata():
    assert rata_rata([10.0, 20.0, 30.0]) == 20.0

def test_rentang():
    assert rentang([5.0, 1.0, 9.0]) == (1.0, 9.0)

def test_ringkasan():
    r = ringkasan([2.0, 4.0, 6.0])
    assert r["jumlah"] == 3
    assert r["rata"] == 4.0

def test_median_ganjil():
    assert median([30.0, 10.0, 20.0]) == 20.0

def test_median_genap():
    assert median([40.0, 10.0, 30.0, 20.0]) == 25.0

def test_median_tidak_mengubah_data():
    d = [3.0, 1.0, 2.0]
    median(d)
    assert d == [3.0, 1.0, 2.0]