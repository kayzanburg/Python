import pytube

def video_indir(video_url, kayit_yolu, video_kalite):
    try:
        youtube_video = pytube.YouTube(video_url)
        if video_kalite == "yüksek":
            video = youtube_video.streams.get_highest_resolution()
        elif video_kalite == "düşük":
            video = youtube_video.streams.get_lowest_resolution()
        else:
            video = youtube_video.streams.filter(res=video_kalite).first()
        video.download(kayit_yolu)
        print("Video başarıyla indirildi!")
    except Exception as e:
        print("Hata:", e)

if __name__ == "__main__":
    url = input("İndirmek istediğiniz YouTube videosunun URL'sini girin: ")
    kayit_yolu = input("Videoyu kaydetmek istediğiniz dizini girin (örneğin: C:/Klasor/): ")
    video_kalite = input("İndirme kalitesini seçin (yüksek, düşük veya özel bir çözünürlük girin): ")

    video_indir(url, kayit_yolu, video_kalite)
