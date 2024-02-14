import time
import webbrowser
import random

def alarm(saati, video_listesi):
    while True:
        su_an = time.localtime()
        if (su_an.tm_hour, su_an.tm_min) == saati:
            print("Alarm çalıştırılıyor...")
            video_linki = random.choice(video_listesi)
            webbrowser.open(video_linki)
            break
        else:
            time.sleep(60)  # Her dakika kontrol et

if __name__ == "__main__":
    alarm_saati = (int(input("Alarm saatini girin (saat): ")), int(input("Alarm saatini girin (dakika): ")))
    dosya_adi = input("YouTube video bağlantılarının bulunduğu dosyanın adını girin: ")

    try:
        with open(dosya_adi, "r") as dosya:
            video_listesi = dosya.readlines()
            video_listesi = [link.strip() for link in video_listesi if link.strip()]
            alarm(alarm_saati, video_listesi)
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")
    except Exception as e:
        print("Bir hata oluştu:", e)
