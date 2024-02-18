import random

# 100 adet random sayı oluşturma
random_numbers = [random.randint(1, 10000) for _ in range(10)]

# Permütasyon sıralama
random_numbers.sort()

# Sıralanmış hali
print("Sıralanmış Hali:")
for num in random_numbers:
    print(num)
