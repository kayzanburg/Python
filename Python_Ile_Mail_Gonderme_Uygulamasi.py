import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

def eposta_gonder(gonderen, alici, konu, icerik, sifre):
    # E-posta sunucusuna bağlanma
    smtp_server = "smtp.gmail.com"  # E-posta sağlayıcısına göre değiştirilebilir
    port = 587  # TLS bağlantısı için port numarası
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(gonderen, sifre)

        # E-posta oluşturma
        mesaj = MIMEMultipart()
        mesaj["From"] = gonderen
        mesaj["To"] = alici
        mesaj["Subject"] = konu
        mesaj.attach(MIMEText(icerik, "plain"))

        # E-posta gönderme
        server.sendmail(gonderen, alici, mesaj.as_string())
        print("E-posta başarıyla gönderildi.")
        server.quit()
    except Exception as e:
        print("Hata:", e)

if __name__ == "__main__":
    gonderen = input("Gönderen e-posta adresini girin: ")
    sifre = getpass.getpass(prompt="Şifrenizi girin: ")
    alici = input("Alıcı e-posta adresini girin: ")
    konu = input("E-posta konusunu girin: ")
    icerik = input("E-posta içeriğini girin: ")

    eposta_gonder(gonderen, alici, konu, icerik, sifre)
