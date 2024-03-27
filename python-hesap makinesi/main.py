import tkinter as tk

def buton_tikla(s):
    if s == "=":
        try:
            hesap = eval(giris.get())
            giris.delete(0, tk.END)
            giris.insert(tk.END, str(hesap))
        except Exception as e:
            giris.delete(0, tk.END)
            giris.insert(tk.END, "Hata")
    elif s == "C":
        giris.delete(0, tk.END)
    else:
        if giris.get() == "Hata":
            giris.delete(0, tk.END)
        giris.insert(tk.END, s)

root = tk.Tk()
root.title("Basit Hesap Makinesi")

giris = tk.Entry(root, width=30, borderwidth=5)
giris.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Numara butonları
for i in range(1, 10):
    buton = tk.Button(root, text=str(i), padx=40, pady=20, command=lambda i=i: buton_tikla(str(i)))
    buton.grid(row=(i-1)//3 + 1, column=(i-1)%3, padx=5, pady=5)

# Sıfır butonu
buton_sifir = tk.Button(root, text="0", padx=40, pady=20, command=lambda: buton_tikla("0"))
buton_sifir.grid(row=4, column=0, padx=5, pady=5)

# İşlem butonları
islem_butonlari = ["+", "-", "*", "/"]
for i, islem in enumerate(islem_butonlari):
    buton = tk.Button(root, text=islem, padx=40, pady=20, command=lambda islem=islem: buton_tikla(islem))
    buton.grid(row=i+1, column=3, padx=5, pady=5)

# Temizle ve hesapla butonları
buton_temizle = tk.Button(root, text="C", padx=40, pady=20, command=lambda: buton_tikla("C"))
buton_temizle.grid(row=4, column=1, padx=5, pady=5)

buton_esittir = tk.Button(root, text="=", padx=40, pady=20, command=lambda: buton_tikla("="))
buton_esittir.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()


