import numpy as np

def max_min_matris():
    # 10x10 boyutunda 100'lük random bir matris oluştur
    matris = np.random.randint(10, 1000, size=(10, 10))
    
    # Matrisin max ve min değerlerini bul
    matris_max = np.max(matris)
    matris_min = np.min(matris)
    
    return matris, matris_max, matris_min

def main():
    print("100'lük randomlu matrisin max ve min değerlerini bulma")

    matris, matris_max, matris_min = max_min_matris()

    print("Matris:")
    print(matris)

    print(f"Max : {matris_max}")
    print(f"Min : {matris_min}")

if __name__ == "__main__":
    main()
