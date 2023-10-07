import tkinter as tk
import math

# Fungsi untuk menambahkan angka ke layar
def tambah_angka(angka):
    current = layar.get()
    layar.delete(0, tk.END)
    layar.insert(0, current + angka)

# Fungsi untuk menghitung
def hitung():
    try:
        hasil = eval(layar.get())
        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))
    except:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")

# Fungsi untuk menghitung akar
def hitung_akar():
    try:
        angka = float(layar.get())
        hasil = math.sqrt(angka)
        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))
    except:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")

# Fungsi untuk menghitung sin
def hitung_sin():
    try:
        angka = float(layar.get())
        hasil = math.sin(math.radians(angka))
        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))
    except:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")

# Fungsi untuk menghitung cos
def hitung_cos():
    try:
        angka = float(layar.get())
        hasil = math.cos(math.radians(angka))
        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))
    except:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")

# Fungsi untuk menghitung tan
def hitung_tan():
    try:
        angka = float(layar.get())
        hasil = math.tan(math.radians(angka))
        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))
    except:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")

# Membuat layar kalkulator
layar = tk.Entry(root, width=20, font=("Arial", 20))
layar.grid(row=0, column=0, columnspan=5)

# Membuat tombol-tombol
tombol = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "√", "sin", "cos", "tan"
]

row_val = 1
col_val = 0

for tombol_text in tombol:
    if tombol_text == "=":
        tk.Button(root, text=tombol_text, padx=20, pady=20, font=("Arial", 20), command=hitung).grid(row=row_val, column=col_val)
    elif tombol_text == "√":
        tk.Button(root, text=tombol_text, padx=20, pady=20, font=("Arial", 20), command=hitung_akar).grid(row=row_val, column=col_val)
    elif tombol_text == "sin":
        tk.Button(root, text=tombol_text, padx=20, pady=20, font=("Arial", 20), command=hitung_sin).grid(row=row_val, column=col_val)
    elif tombol_text == "cos":
        tk.Button(root, text=tombol_text, padx=20, pady=20, font=("Arial", 20), command=hitung_cos).grid(row=row_val, column=col_val)
    elif tombol_text == "tan":
        tk.Button(root, text=tombol_text, padx=20, pady=20, font=("Arial", 20), command=hitung_tan).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=tombol_text, padx=20, pady=20, font=("Arial", 20), command=lambda text=tombol_text: tambah_angka(text)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Tombol untuk menghapus layar
tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 20), command=lambda: layar.delete(0, tk.END)).grid(row=row_val, column=col_val)

root.mainloop()
