import math

#tambah
def tambah(bil1, bil2):
    hasil = bil1+bil2
    print("hasil tambah dari", bil1, "+", bil2, "=", hasil)

#kurang
def kurang(bil1, bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari", bil1, "-", bil2, "=", hasil)

#kali
def kali(bil1, bil2):
    hasil = bil1*bil2
    print("hasil perkalian dari", bil1, "*", bil2, "=", hasil)

#bagi
def bagi(bil1, bil2):
    hasil = bil1/bil2
    print("hasil pembagian dari", bil1, "/", bil2, "=", hasil)

#pangkat
def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari", bil1, "^", bil2, "=", hasil)

#log
def log(bil1):
    hasil = math.log(bil1)
    print("hasil log dari", bil1,  "=", hasil)
    
#akar
def akar(bil1):
    hasil = math.sqrt(bil1)
    print("hasil pengakaran dari", bil1,  "=", hasil)

#sin
def sin(bil1):
    hasil = math.sin(bil1)
    print("hasil sin dari", bil1, "=", hasil)

#cos
def cos(bil1):
    hasil = math.cos(bil1)
    print("hasil cos dari", bil1, "=", hasil)

#tan
def tan(bil1):
    hasil = math.tan(bil1)
    print("hasil tan dari", bil1, "=", hasil)