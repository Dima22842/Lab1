minus = 0
plus = 0
zero = 0

tab = "    "
black = "\033[40m    \033[0m"
line = "|"

with open("sequence.txt", "r", encoding="utf-8") as sequence_txt:
    for number in sequence_txt:
        num = float(number)

        if num > 0:
            plus += 1
        elif num < 0:
            minus += 1
        else:
            zero += 1

maximum = max(plus, minus, zero)
minimum = min(plus, minus, zero)
middle = plus + minus + zero - maximum - minimum

maximum_part = maximum // 10
middle_part = middle // 10
minimum_part = minimum // 10

if minimum != 0:
    minimum_part = 1

if maximum_part == middle_part:
    maximum_part += 1

while maximum_part > middle_part:
    maximum_part -= 1
    print(f"{maximum:4}", line + tab + black)
    maximum -= 10

while middle_part > minimum_part:
    middle_part -= 1
    print(f"{middle:4}", line + tab + black + tab + black)
    middle -= 10

while minimum_part > 0:
    minimum_part -= 1
    print(f"{minimum:4}", line + tab + black + tab + black + tab + black)
    minimum -= 10

signs = [(plus, "(+)"), (minus, "(-)"), (zero, "(0)")]
signs.sort(reverse=True)

print(tab * 3 + tab.join(name for count, name in signs))
