# Membuat list kendaraan
kendaraan = ['honda genio', 'matic', '110cc','navy', '2']
print (kendaraan)

# Menambahkan harga kendaraan dan tipe kendaraan
kendaraan.append('19 juta')
kendaraan.append('honda')
print (kendaraan)

# Menambahkan merk kendaraan di index 2
kendaraan.insert(2,'CBS-ISS')
print (kendaraan)

ket = '''selamat datang di aplikasi menghitung luas bangun datar
masukan pilihan
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
'''
pilihan = input (ket)

match pilihan:
   case '1':
     print ('kamu memilih 1 untuk menghitung luas persegi')
     sisi = int(input('masukan sisi?'))
     luasP = sisi*sisi
     print('luas persegi yang sisinya', sisi, 'adalah', luasP)

   case '2':
     print ('kamu memilih 2 untuk menghitung luas lingkaran')
     jari2 = float(input('masukan jari-jari?'))
     luasL = 3.14 * jari2 * jari2
     print('luas lingkaran yang jari-jarinya', jari2, 'adalah', luasL)

   case '3':
     print ('kamu memilih 3 untuk menghitung luas segitiga')
     alas = int(input ('masukan alas?'))
     tinggi = int(input ('masukan tinggi?'))
     luasS = 0.5 * alas * tinggi
     print('luas segitiga yang alasnya', alas, 'dan tingginya', tinggi, 'adalah', int(luasS))

   case _:
     print ('salah memilih pilihan')