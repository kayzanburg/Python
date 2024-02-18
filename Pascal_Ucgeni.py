def pascal_ucgeni(n):
    ucgen = []
    for i in range(n):
        row = [1]
        if ucgen:
            prev_row = ucgen[-1]
            new_row = [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)]
            row.extend(new_row)
            row.append(1)
        ucgen.append(row)
    return ucgen

def print_pascal(ucgen):
    print("Pascal Görünümü:")
    for row in ucgen:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    eleman_sayisi = int(input("Lütfen eleman sayısını giriniz: "))
    pascal_triangle = pascal_ucgeni(eleman_sayisi)
    print_pascal(pascal_triangle)
