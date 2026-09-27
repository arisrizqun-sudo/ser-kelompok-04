from mikrofon import Mikrofon


def test_kondisi_awal():
    mic = Mikrofon("MIC-1")
    assert mic.nama == "MIC-1"
    assert mic.aktif is False
    assert mic.level == 0


def test_nyalakan():
    mic = Mikrofon("MIC-1")
    mic.nyalakan()
    assert mic.aktif is True


def test_set_level_saat_aktif():
    mic = Mikrofon("MIC-1")
    mic.nyalakan()
    mic.set_level(70)
    assert mic.level == 70


def test_set_level_saat_mati():
    mic = Mikrofon("MIC-1")
    mic.set_level(70)
    assert mic.level == 0


def test_matikan():
    mic = Mikrofon("MIC-1")
    mic.nyalakan()
    mic.set_level(70)
    mic.matikan()
    assert mic.aktif is False
    assert mic.level == 0