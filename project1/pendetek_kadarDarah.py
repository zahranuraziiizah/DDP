import tkinter as tk

def kadar_gulaDarah():
    nilai_gula = int(entry_nilai_gula.get())

    if 0 <= nilai_gula < 100:
        ket_gula_darah = "Normal"
    elif 100 <= nilai_gula < 180:
        ket_gula_darah = "Batas Normal"
    else:
        ket_gula_darah = "Tinggi, menandakan pasien menderita Diabetes"
    
    hasil_nilai_gula_label.config(text=f"Kadar Gula Darah: {ket_gula_darah}")

def kadar_asamUrat():
    nilai_asamUrat = float(entry_nilai_asamUrat.get())

    if 0 <= nilai_asamUrat < 3.5:
        ket_asam_urat = "Normal"
    elif 3.5 <= nilai_asamUrat < 7:
        ket_asam_urat = "Batas Normal"
    else:
        ket_asam_urat = "Tinggi, menandakan pasien menderita Asam Urat"

    hasil_nilai_asamUrat_label.config(text=f"Kadar Asam Urat: {ket_asam_urat}")

def kadar_kolesterol():
    nilai_kolesterol = int(entry_nilai_kolesterol.get())

    if 0 <= nilai_kolesterol < 200:
        ket_kolesterol = "Normal"
    else:
        ket_kolesterol = "Tinggi, menandakan pasien menderita Kolesterol"

    hasil_nilai_kolesterol_label.config(text=f"Kadar Kolesterol: {ket_kolesterol}")



# tampilan jendela utama
root = tk.Tk()
root.title("Aplikasi Pendetek Kadar Darah dalam Tubuh")

# GULA DARAH
# Label dan entry untuk memasukkan nilai kadar gula
label_nilai_gula = tk.Label(root, text="Masukkan Nilai Kadar Gula:")
label_nilai_gula.pack()
entry_nilai_gula = tk.Entry(root)
entry_nilai_gula.pack()

# Tombol untuk mendetek Kadar gula
kadar_gulaDarah_button = tk.Button(root, text="Cek Kadar Gula", command=kadar_gulaDarah)
kadar_gulaDarah_button.pack()

# Label untuk menampilkan hasil kadar gula
hasil_nilai_gula_label = tk.Label(root, text="")
hasil_nilai_gula_label.pack()

# ASAM URAT
# Label dan entry untuk memasukkan nilai kadar asam urat
label_nilai_asamUrat = tk.Label(root, text="Masukkan Nilai Kadar Asam Urat:")
label_nilai_asamUrat.pack()
entry_nilai_asamUrat = tk.Entry(root)
entry_nilai_asamUrat.pack()

# Tombol untuk mendetek Kadar asam urat
kadar_asamUrat_button = tk.Button(root, text="Cek Kadar Asam Urat", command=kadar_asamUrat)
kadar_asamUrat_button.pack()

# Label untuk menampilkan hasil kadar asam urat
hasil_nilai_asamUrat_label = tk.Label(root, text="")
hasil_nilai_asamUrat_label.pack()

# KOLESTEROL
# Label dan entry untuk memasukkan nilai kadar kolesterol
label_nilai_kolesterol = tk.Label(root, text="Masukkan Nilai Kadar Kolesterol:")
label_nilai_kolesterol.pack()
entry_nilai_kolesterol = tk.Entry(root)
entry_nilai_kolesterol.pack()

# Tombol untuk mendetek Kadar asam urat
kadar_kolesterol_button = tk.Button(root, text="Cek Kadar Kolesterol", command=kadar_kolesterol)
kadar_kolesterol_button.pack()

# Label untuk menampilkan hasil kadar asam urat
hasil_nilai_kolesterol_label = tk.Label(root, text="")
hasil_nilai_kolesterol_label.pack()

# Menampilkan jendela
root.mainloop()