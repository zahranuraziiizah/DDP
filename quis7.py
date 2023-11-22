#1
nama_kendaraan = input ('masukan nama kendaraan ?')
jenis_bensin = input ('masukan jenis bensin ?')
kota = input ('masukan kota ?')

#jenis bensin
if jenis_bensin == 'pertalite':
    harga = 10000
    jarak_tempuh = 12
elif jenis_bensin == 'pertamax':
    harga = 14000        
    jarak_tempuh = 13
elif jenis_bensin == 'pertamax turbo':
    harga = 17000
    jarak_tempuh = 13.5
else :
    print('tidak ada jenis bensin ini')

#kota
if kota == 'Jakarta':
    jarak_kota = 20
elif kota == 'Bekasi':   
    jarak_kota = 35.7
elif kota == 'Depok':
    jarak_kota = 5
elif kota == 'Tangerang':     
    jarak_kota = 99
elif kota == 'Bogor':   
    jarak_kota = 35.7
else :
    print('kota ini tidak ada dalam daftar')

#pemakaian
pemakaian_bensin = jarak_kota/jarak_tempuh

#print
print ("nama kendaraan :", nama_kendaraan)
print ("jenis bensin :", jenis_bensin)
print ("kota :", kota)
print ("pemakaian bensin :", pemakaian_bensin)
print(f"total harga bensin adalah : {pemakaian_bensin * harga}")

#2

#3
for i in range(1,21) :
    if i % 3 == 0 :
        print("STT Nurul Fikri")
    else :
        print(i)