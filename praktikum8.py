#data diri
def data_diri(nama, alamat, gender, umur, hobi):
    print("Nama saya adalah", nama)
    print("Tempat tinggal saya saat ini di", alamat)
    print("Saya berjenis kelamin", gender)
    print("Tahun ini saya berumur", umur)
    print("Hobi saya", hobi)

data_diri("Zahra Nur Azizah", "Kabupaten Bogor", "perempuan", "18 tahun", "membaca")

#nilai
def penilaian(nilai):
    if nilai <= 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Maaf nilai yang anda masukan tidak valid"
    
print(penilaian(60))

#mencetak bilangan ganjil
def mencetak_bilangan_ganjil(n):
    for i in range(1, n+1, 2):
        print(i)

mencetak_bilangan_ganjil(100)