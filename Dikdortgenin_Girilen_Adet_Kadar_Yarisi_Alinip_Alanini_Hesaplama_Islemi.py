def dikdortgen_alani(boy, en):
    return boy * en

def main():
    boy = 200
    en = 100
    for i in range(10):
        alan = dikdortgen_alani(boy, en)
        print(f"Boyu: {boy} Eni: {en} Alanı: {alan}")
        boy /= 2
        en /= 2

if __name__ == "__main__":
    main()
