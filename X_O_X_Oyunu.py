import pygame
import sys

# Pencere boyutları
GENISLIK = 600
YUKSEKLIK = 600

# Renkler
BEYAZ = (255, 255, 255)
SARI = (255, 255, 0)
MAVI = (0, 0, 255)

# Oyun alanı
ALAN_BOYUTU = 3
KARE_BOYUTU = GENISLIK // ALAN_BOYUTU

# Oyuncular
OYUNCU_X = "X"
OYUNCU_O = "O"

def ekran_ciz():
    ekran.fill(BEYAZ)
    for i in range(1, ALAN_BOYUTU):
        pygame.draw.line(ekran, MAVI, (0, i * KARE_BOYUTU), (GENISLIK, i * KARE_BOYUTU), 2)
        pygame.draw.line(ekran, MAVI, (i * KARE_BOYUTU, 0), (i * KARE_BOYUTU, YUKSEKLIK), 2)

def oyun_alani_hazirla():
    return [[None for _ in range(ALAN_BOYUTU)] for _ in range(ALAN_BOYUTU)]

def kareyi_guncelle(x, y, oyuncu):
    oyun_alani[y][x] = oyuncu

def kare_bos_mu(x, y):
    return oyun_alani[y][x] is None

def kazanan_kontrol(oyuncu):
    for y in range(ALAN_BOYUTU):
        if all(oyuncu == oyun_alani[y][x] for x in range(ALAN_BOYUTU)):
            return True
    for x in range(ALAN_BOYUTU):
        if all(oyuncu == oyun_alani[y][x] for y in range(ALAN_BOYUTU)):
            return True
    if all(oyuncu == oyun_alani[i][i] for i in range(ALAN_BOYUTU)):
        return True
    if all(oyuncu == oyun_alani[i][ALAN_BOYUTU - 1 - i] for i in range(ALAN_BOYUTU)):
        return True
    return False

def oyun_bitti_mi():
    return any(None not in row for row in oyun_alani) or kazanan_kontrol(OYUNCU_X) or kazanan_kontrol(OYUNCU_O)

pygame.init()
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Tic-Tac-Toe")

oyun_alani = oyun_alani_hazirla()
siradaki_oyuncu = OYUNCU_X
oyun_devam = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not oyun_devam:
            continue

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()
            secilen_kare_x = mouseX // KARE_BOYUTU
            secilen_kare_y = mouseY // KARE_BOYUTU

            if kare_bos_mu(secilen_kare_x, secilen_kare_y):
                kareyi_guncelle(secilen_kare_x, secilen_kare_y, siradaki_oyuncu)
                if kazanan_kontrol(siradaki_oyuncu):
                    print(f"{siradaki_oyuncu} kazandı!")
                    oyun_devam = False
                elif oyun_bitti_mi():
                    print("Berabere!")
                    oyun_devam = False
                else:
                    siradaki_oyuncu = OYUNCU_O if siradaki_oyuncu == OYUNCU_X else OYUNCU_X

    ekran_ciz()
    for y in range(ALAN_BOYUTU):
        for x in range(ALAN_BOYUTU):
            if oyun_alani[y][x] == OYUNCU_X:
                pygame.draw.line(ekran, SARI, (x * KARE_BOYUTU, y * KARE_BOYUTU), ((x + 1) * KARE_BOYUTU, (y + 1) * KARE_BOYUTU), 4)
                pygame.draw.line(ekran, SARI, ((x + 1) * KARE_BOYUTU, y * KARE_BOYUTU), (x * KARE_BOYUTU, (y + 1) * KARE_BOYUTU), 4)
            elif oyun_alani[y][x] == OYUNCU_O:
                pygame.draw.circle(ekran, SARI, (x * KARE_BOYUTU + KARE_BOYUTU // 2, y * KARE_BOYUTU + KARE_BOYUTU // 2), KARE_BOYUTU // 2 - 4, 4)

    pygame.display.update()
