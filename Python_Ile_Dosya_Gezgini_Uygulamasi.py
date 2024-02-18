import os
import tkinter as tk
from tkinter import filedialog, messagebox

def dosya_gezgini():
    dosya_yolu = filedialog.askdirectory()
    listele(dosya_yolu)

def listele(dizin):
    dosyalar = os.listdir(dizin)
    dosya_listesi.delete(0, tk.END)
    for dosya in dosyalar:
        dosya_listesi.insert(tk.END, dosya)

def dosya_detaylarini_goster():
    secili_dosya = dosya_listesi.get(tk.ACTIVE)
    dosya_yolu = os.path.join(dizin_yolu, secili_dosya)
    if os.path.isfile(dosya_yolu):
        dosya_boyutu = os.path.getsize(dosya_yolu)
        dosya_detaylari = f"Dosya Adı: {secili_dosya}\nDosya Yolu: {dosya_yolu}\nBoyut: {dosya_boyutu} byte"
        messagebox.showinfo("Dosya Detayları", dosya_detaylari)
    else:
        messagebox.showinfo("Hata", "Lütfen bir dosya seçiniz.")

def kopyala():
    secili_dosya = dosya_listesi.get(tk.ACTIVE)
    dosya_yolu = os.path.join(dizin_yolu, secili_dosya)
    hedef_dizin = filedialog.askdirectory()
    try:
        if os.path.isfile(dosya_yolu):
            hedef_yol = os.path.join(hedef_dizin, secili_dosya)
            if not os.path.exists(hedef_yol):
                with open(dosya_yolu, 'rb') as kaynak:
                    with open(hedef_yol, 'wb') as hedef:
                        hedef.write(kaynak.read())
            else:
                messagebox.showwarning("Uyarı", "Hedef dizinde aynı isimde bir dosya zaten var.")
        else:
            messagebox.showwarning("Hata", "Lütfen bir dosya seçiniz.")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

root = tk.Tk()
root.title("Python Dosya Gezgini")

dizin_yolu = os.getcwd()

gezgin_button = tk.Button(root, text="Dizin Seç", command=dosya_gezgini)
gezgin_button.pack(pady=10)

dosya_listesi = tk.Listbox(root)
dosya_listesi.pack(expand=True, fill=tk.BOTH)

detay_button = tk.Button(root, text="Dosya Detayları", command=dosya_detaylarini_goster)
detay_button.pack(pady=5)

kopyala_button = tk.Button(root, text="Dosya Kopyala", command=kopyala)
kopyala_button.pack(pady=5)

root.mainloop()
