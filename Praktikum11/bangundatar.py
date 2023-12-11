#persegi
def persegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi
    print("jadi luas persegi adalah", luas)
    print("jadi keliling persegi adalah", keliling)

#segitiga
def segitiga(alas, tinggi, miring):
    luas = 0.5 * (alas*tinggi)
    keliling = alas+tinggi+miring
    print("jadi luas segitiga adalah", luas)
    print("jadi keliling segitiga adalah", keliling)

#persegi panjang
def persegi_panjang(panjang, lebar):
    luas = panjang*lebar
    keliling = 2 * (panjang*lebar)
    print("jadi luas persegi panjang adalah", luas)
    print("jadi keliling persegi panjang adalah", keliling)

#jajar genjang
def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas*tinggi
    keliling = 2 * (alas+sisi_miring)
    print("jadi luas jajar genjang adalah", luas)
    print("jadi keliling jajar genjang adalah", keliling)
    

#belah ketupat
def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * (diagonal1*diagonal2)
    keliling = 4*sisi
    print("jadi luas belah ketupat adalah", luas)
    print("jadi keliling belah ketupat adalah", keliling)

#lingkaran
def lingkaran(jari2):
    luas = 22/7 * (jari2*jari2)
    keliling = 2 * 22/7 * (jari2)
    print("jadi luas belah ketupat adalah", luas)
    print("jadi keliling belah ketupat adalah", keliling)

#trapesium
def trapesium(a, b, c, d, tinggi):
    luas = 0.5 * (a+b) * tinggi
    keliling = a+b+c+d
    print("jadi luas trapesium adalah", luas)
    print("jadi keliling trapesium adalah", keliling)