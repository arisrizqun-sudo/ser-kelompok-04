from emosi import Emosi
def test_senang():
 e = Emosi(0.8)
 assert e.tentukan_label() == "senang"
def test_sedih():
 e = Emosi(0.1)
 assert e.tentukan_label() == "sedih"
def test_netral():
 e = Emosi(0.5)
 assert e.tentukan_label() == "netral"
def test_batas_senang():
 e = Emosi(0.6)
 assert e.tentukan_label() == "senang"
def test_batas_sedih():
 e = Emosi(0.3)
 assert e.tentukan_label() == "sedih"