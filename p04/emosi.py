class Emosi:
    def __init__(self, skor):
        self.skor = skor

    def tentukan_label(self):
        if self.skor >= 0.6:
            return "senang"
        elif self.skor <= 0.3:
            return "sedih"
        else:
            return "netral"