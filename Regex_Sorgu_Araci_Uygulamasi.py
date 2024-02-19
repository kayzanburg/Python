import re

def regex_query(regex_pattern, text):
    matches = re.finditer(regex_pattern, text, re.MULTILINE | re.IGNORECASE)
    for matchNum, match in enumerate(matches, start=1):
        print("Eşleşme {matchNum}:".format(matchNum=matchNum))
        print("Başlangıç pozisyonu: {start}".format(start=match.start()))
        print("Bitiş pozisyonu: {end}".format(end=match.end()))
        print("Eşleşen metin: {group}".format(group=match.group()))
        print("-----------------------")

def main():
    # Kullanıcıdan regex sorgusu ve metin girişi alınır
    regex_pattern = input("Regex sorgusu girin: ")
    text = input("Metin girin: ")

    # Regex sorgusu çalıştırılır
    regex_query(regex_pattern, text)

if __name__ == "__main__":
    main()
