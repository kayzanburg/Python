from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# ChromeDriver'ı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Web sitesini aç
    driver.get("https://yokatlas.yok.gov.tr/universite.php")
    time.sleep(5)  # Sayfanın yüklenmesi için bekleyin

    # Üniversitelerin listesini çek
    universiteler = driver.find_elements(By.CLASS_NAME, "uniListItem")

    # Tüm bilgileri kaydetme
    with open("C:/Users/Bilal/Desktop/Sistem_Programlama_Odev/textler/universiteler1.txt", "w", encoding="utf-8") as file:
        for uni in universiteler:
            # Üniversite bilgilerini çek
            baslik = uni.find_element(By.CLASS_NAME, "baslik").text
            tur = uni.find_element(By.CLASS_NAME, "tur").text
            sehir = uni.find_element(By.CLASS_NAME, "sehir").text
            website = uni.find_element(By.CSS_SELECTOR, "div.col-md-8 > a").get_attribute("href")
            adres = uni.text.split("Adres: ")[1].split("\n")[0]

            # Dosyaya yaz
            file.write(f"Üniversite Adı: {baslik}\n")
            file.write(f"Üniversite Türü: {tur}\n")
            file.write(f"Şehir: {sehir}\n")
            file.write(f"Web Sitesi: {website}\n")
            file.write(f"Adres: {adres}\n")
            file.write("\n")  # Bir sonraki üniversite için boşluk bırak

    # Sadece üniversite isimlerini kaydetme
    with open("C:/Users/Bilal/Desktop/Sistem_Programlama_Odev/textler/Universite_Ismi.txt", "w", encoding="utf-8") as name_file:
        for uni in universiteler:
            baslik = uni.find_element(By.CLASS_NAME, "baslik").text
            name_file.write(f"{baslik}\n")

    # Üniversite linklerini kaydetme
    with open("C:/Users/Bilal/Desktop/Sistem_Programlama_Odev/textler/Universite_Linkleri.txt", "w", encoding="utf-8") as link_file:
        for uni in universiteler:
            website = uni.find_element(By.CSS_SELECTOR, "div.col-md-8 > a").get_attribute("href")
            link_file.write(f"{website}\n")

    # Resimleri çek
    time.sleep(5)  # Resimlerin yüklenmesini bekleyin
    logolar = driver.find_elements(By.XPATH, "//img[@class='col-md-2 logo']")

    # Resim URL'lerini kaydetme
    with open("C:/Users/Bilal/Desktop/Sistem_Programlama_Odev/textler/resimler.txt", "w", encoding="utf-8") as file:
        for logo in logolar:
            # Resim URL'sini çek
            resim_url = logo.get_attribute("src")

            # Dosyaya yaz
            file.write(f"Resim URL'si: {resim_url}\n")

finally:
    # Tarayıcıyı kapat
    driver.quit()

print("\n\nVeriler, resimler, üniversite isimleri ve üniversite linkleri başarıyla kaydedildi.")
