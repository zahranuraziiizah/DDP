class animal: 
    def __init__(self, name, makanan, hidup, berkembangBiak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

cetak = animal("Kelinci", "Sayuran", "Darat", "Melahirkan")
print(f"nama hewan : {cetak.name}")
print(f"makanannya : {cetak.makanan}")
print(f"hidup di : {cetak.hidup}")
print(f"berkembang biak dengan cara : {cetak.berkembangBiak}")


print("===========================================")

#ini subclass
class badak(animal):
#ini properti
    def __init__(self, name, makanan, hidup, berkembangBiak):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
    def badak(self):
        print(f"Nama hewan ini adalah {self.name} makanannya adalah {self.makanan} hidupnya di {self.hidup} berkembang biak dengan {self.berkembangBiak}")

#cetak
animal1 = badak("badak", "dedaunan", "darat", "melahirkan")
animal1.badak()

#ini subclass
class ikan(animal):
#ini properti
    def __init__(self, name, makanan, hidup, berkembangBiak):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
    def ikan(self):
        print(f"Nama hewan ini adalah {self.name} makanannya adalah {self.makanan} hidupnya di {self.hidup} berkembang biak dengan {self.berkembangBiak}")

#cetak
animal2 = ikan("ikan", "pelet", "air", "bertelur")
animal2.ikan()

#ini subclass
class ular(animal):
#ini properti
    def __init__(self, name, makanan, hidup, berkembangBiak):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
    def ular(self):
        print(f"Nama hewan ini adalah {self.name} makanannya adalah {self.makanan} hidupnya di {self.hidup} berkembang biak dengan {self.berkembangBiak}")       
    
#cetak
animal3 = ular("ular", "daging", "darat dan air", "bertelur")
animal3.ular()
    