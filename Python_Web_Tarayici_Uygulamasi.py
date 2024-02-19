import requests
from bs4 import BeautifulSoup

def web_tarayici(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a'):
                print(link.get('href'))
        else:
            print("Hata: Sayfa bulunamadı.")
    except Exception as e:
        print("Hata:", str(e))

if __name__ == "__main__":
    url = input("Lütfen bir web sayfası URL'si girin: ")
    web_tarayici(url)
