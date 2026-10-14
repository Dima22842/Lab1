size = int(input("Введите размер графика (желательно нечетное число): "))

space = " "
dot = "+"
line1 = "|"
line2 = "—"

graphic = [[space] * size for _ in range(size)]
center = size // 2

for i in range(size):
    graphic[center][i] = line2
    graphic[i][center] = line1

for x in range(-center, center + 1):
    y = x ** 2

    if y <= center:
        graphic[center - y][center + x] = dot

for row in graphic:
    print(*row)
