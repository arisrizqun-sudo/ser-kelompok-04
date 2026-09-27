import pytest
from suhu import hitung_rata_rata, cari_tertinggi, cek_status
def test_rata_rata_bulat():
 assert hitung_rata_rata([10, 20, 30]) == 20
def test_rata_rata_data_sensor():
 assert hitung_rata_rata([28.5, 30.2, 29.8, 31.0, 27.9]) == pytest.approx(29.48)
def test_tertinggi():
 assert cari_tertinggi([28.5, 30.2, 27.9]) == 30.2
def test_status_panas():
 assert cek_status(31) == "PANAS"
def test_status_batas():
 assert cek_status(30) == "NORMAL"
def test_status_dingin():
 assert cek_status(20) == "DINGIN"