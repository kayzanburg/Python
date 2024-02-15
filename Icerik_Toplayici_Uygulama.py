import requests
from bs4 import BeautifulSoup

def icerik_toplayici(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        basliklar = soup.find_all('h2')  # Örnek olarak şu anda sadece h2 başlıklarını topluyoruz
        for baslik in basliklar:
            print(baslik.text.strip())
    else:
        print("İstek başarısız oldu. Durum kodu:", response.status_code)

if __name__ == "__main__":
    url = input("Lütfen bir web sitesi URL'si girin: ")
    icerik_toplayici(url)
