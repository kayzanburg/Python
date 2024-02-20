import random

def zar_atis():
    print("Yarışmaya A kişisi ve B kişisi katılıyor.")
    input("Yarışmaya başlamak için herhangi bir tuşa basıp ENTER'a basın.\n\nYazdığınız İfade : ")

    skor_A = 0
    skor_B = 0
    set_sayisi = 5

    for i in range(1, set_sayisi + 1):
        zar_A = random.randint(1, 6)
        zar_B = random.randint(1, 6)

        print(f"A kişisi : {zar_A} B kişisi : {zar_B}")

        if zar_A > zar_B:
            skor_A += 1
            print("Bu turu kazanan kişi A'dır.")
        elif zar_B > zar_A:
            skor_B += 1
            print("Bu turu kazanan kişi B'dir.")
        else:
            print("Bu tur berabere.")

        print(f"A= {skor_A} B= {skor_B}")
        input("Lütfen herhangi bir tuşa basıp ENTER'a basın.\n\nYazdığınız İfade : ")

    print(f"\n\nYarışma bitmiştir... \n\nSonuç: A = {skor_A} B = {skor_B}")

if __name__ == "__main__":
    zar_atis()
