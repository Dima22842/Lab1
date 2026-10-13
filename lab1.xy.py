size = int(input("Введите размер графика(желательно нечетное число): "))
space = " "
black = "+"
line1="|"
line2="—"
grafic =[[space] * size for i in range(size)]

center = size // 2

for i in range(size):
    grafic[center][i] = line2
    grafic[i][center] = line1

for x in range(-center, center + 1):
    y = x ** 2

    if y <= center:
        grafic[center - y][center + x] = black

for row in grafic:
    print(*row)