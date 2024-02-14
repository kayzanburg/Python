import tkinter as tk
from tkinter import ttk

def donustur():
    miktar = float(giris.get())
    secili_giris = giris_para_birimi.get()
    secili_cikis = cikis_para_birimi.get()

    if secili_giris == "Türk Lirası" and secili_cikis == "ABD Doları":
        sonuc = miktar * 0.12
    elif secili_giris == "Türk Lirası" and secili_cikis == "Euro":
        sonuc = miktar * 0.10
    elif secili_giris == "Türk Lirası" and secili_cikis == "İngiliz Sterlini":
        sonuc = miktar * 0.09
    elif secili_giris == "ABD Doları" and secili_cikis == "Türk Lirası":
        sonuc = miktar * 8.54
    elif secili_giris == "ABD Doları" and secili_cikis == "Euro":
        sonuc = miktar * 0.82
    elif secili_giris == "ABD Doları" and secili_cikis == "İngiliz Sterlini":
        sonuc = miktar * 0.72
    elif secili_giris == "Euro" and secili_cikis == "Türk Lirası":
        sonuc = miktar * 10.16
    elif secili_giris == "Euro" and secili_cikis == "ABD Doları":
        sonuc = miktar * 1.22
    elif secili_giris == "Euro" and secili_cikis == "İngiliz Sterlini":
        sonuc = miktar * 0.88
    elif secili_giris == "İngiliz Sterlini" and secili_cikis == "Türk Lirası":
        sonuc = miktar * 11.34
    elif secili_giris == "İngiliz Sterlini" and secili_cikis == "ABD Doları":
        sonuc = miktar * 1.39
    elif secili_giris == "İngiliz Sterlini" and secili_cikis == "Euro":
        sonuc = miktar * 1.14

    label_sonuc.config(text=str(sonuc))

# Ana pencere
root = tk.Tk()
root.title("Döviz Çevirici")

# Giriş miktarı
giris_label = tk.Label(root, text="Miktar:")
giris_label.grid(row=0, column=0, padx=5, pady=5)

giris = tk.Entry(root)
giris.grid(row=0, column=1, padx=5, pady=5)

# Giriş para birimi
giris_para_birimi_label = tk.Label(root, text="Giriş Para Birimi:")
giris_para_birimi_label.grid(row=1, column=0, padx=5, pady=5)

giris_para_birimi = ttk.Combobox(root, values=["Türk Lirası", "ABD Doları", "Euro", "İngiliz Sterlini"])
giris_para_birimi.grid(row=1, column=1, padx=5, pady=5)
giris_para_birimi.current(0)

# Çıkış para birimi
cikis_para_birimi_label = tk.Label(root, text="Çıkış Para Birimi:")
cikis_para_birimi_label.grid(row=2, column=0, padx=5, pady=5)

cikis_para_birimi = ttk.Combobox(root, values=["Türk Lirası", "ABD Doları", "Euro", "İngiliz Sterlini"])
cikis_para_birimi.grid(row=2, column=1, padx=5, pady=5)
cikis_para_birimi.current(1)

# Dönüştürme butonu
donustur_button = tk.Button(root, text="Dönüştür", command=donustur)
donustur_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Sonuç
label_sonuc = tk.Label(root, text="")
label_sonuc.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
