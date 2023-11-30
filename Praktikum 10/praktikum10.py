#Nama siswa yang lulus

hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def predikatlulus(data):
    # list untuk mengambil nama dari hasil_akhir yang memiliki nilai lebih dari 65
    lulus = [mahasiswa['nama']
      for mahasiswa in data
      if mahasiswa['nilai'] > 65]
    return lulus

# memanggil fungsi lulus untuk memberikan predikat lulus
hasil = predikatlulus(hasil_akhir)
print('Siswa yang lulus adalah', hasil)

#Membalik nama buah
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def list_buah(buah):
    list_terbalik = []

    for i in range(len(buah)-1, -1, -1):
        list_terbalik.append(buah[i])
    return list_terbalik
    
hasil = list_buah(buah)
print('Hasil urutan terbalik adalah ', hasil)

# duplikasi nama buah
buah2 = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikat(buah):
    list_duplikasi = []

    for b in buah:
        list_duplikasi.append(b)  #menambahkan list pertama
        list_duplikasi.append(b)  #menambahkan list kedua (duplikat)

    return list_duplikasi

# memanggil fungsi duplikat
hasil = duplikat(buah)
print('Hasil duplikat adalah ', hasil)

#Konsonan 
def konsonan(kalimat):
    huruf = ''

    for k in kalimat:
        if k not in 'aiueo':
            # menambahkan konsonan ke string kosong
            huruf += k
    return huruf

# memanggil fungsi konsonan dengan string nurul fikri
hasil = konsonan('Nurul Fikri')
print('Huruf konsonan dari kata Nurul Fikri adalah', hasil)