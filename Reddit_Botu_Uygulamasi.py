import praw
import time

# Reddit API kimlik bilgilerini girin
reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret='CLIENT_SECRET',
                     username='USERNAME',
                     password='PASSWORD',
                     user_agent='USER_AGENT')

def takip_et(subreddit_adı, beklenen_kelimeler):
    subreddit = reddit.subreddit(subreddit_adı)

    print(f"{subreddit_adı} subreddit'i izleniyor...")

    while True:
        for submission in subreddit.new(limit=10):
            if any(kelime.lower() in submission.title.lower() for kelime in beklenen_kelimeler):
                rapor_ver(submission)
        time.sleep(60)  # Her dakika kontrol et

def rapor_ver(submission):
    print(f"Yeni gönderi bulundu: {submission.title}")
    # Burada rapor alma veya başka bir işlem yapılabilir

if __name__ == "__main__":
    subreddit_adı = input("İzlemek istediğiniz subreddit'in adını girin: ")
    beklenen_kelimeler = input("Rapor almak istediğiniz kelimeleri virgülle ayırarak girin: ").split(',')

    takip_et(subreddit_adı, beklenen_kelimeler)
