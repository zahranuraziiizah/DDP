class Gempa:
    #atribut class
    lokasi = ''
    skala = 0

    #construktur
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    #method
    def data_gempa(self):
        if self.skala < 2 :
            ket = "maka dampak gempa tidak terasa"
        elif self.skala >= 2 and self.skala <= 4:
           ket = "maka dampak bangunan retak-retak"
        elif (self.skala >= 4 and self.skala <= 6):
           ket = "maka dampak bangunan roboh"
        elif (self.skala >6):
           ket = "maka dampak bangunan roboh dan berpotensi tsunami"
        else :
           ket = "Skala tidak valid"
        print(f'Telah terjadi gempa di {self.lokasi} dengan skala {self.skala} {ket}')
    