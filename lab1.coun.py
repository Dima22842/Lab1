minus = 0
plus = 0
zero = 0

sequence = open("sequence.txt", "r")
for number in sequence:
    num = float(number)
    if num > 0:
        plus += 1
    elif num < 0:
        minus += 1
    else:
        zero += 1

tab = "\033[0m    \033[0m"
black = "\033[40m    \033[0m"
line = "|"

maximum = max(plus, minus, zero)
minimum = min(plus, minus, zero)
max2 = plus + minus + zero - maximum - minimum
if (maximum >= 25):
    a=maximum // 10
    b= max2 // 10
    c=minimum // 10
else:
    a=maximum
    b=max2
    c=minimum
i=0
if (minimum!=0):
    c=1
if (a==b):
    a=a+1


while (a > b):
    a=a-1
    print(f"{maximum:4}", line + tab + black)
    i=i+1
    if (i>0):
        maximum-=10
i=0
while (b > c):
    b=b-1
    print(f"{max2:4}", line + tab + black + tab + black)
    i=i+1
    if (i>0):
        max2-=10
i=0
while (c > 0):
    c=c-1
    print(f"{minimum:4}", line + tab + black + tab + black + tab + black)
    i+=1
    if (i>0):
        minimum-=10
numbers = [(plus, "(+)"), (minus, "(-)"), (zero, "(0)")]
numbers.sort(reverse=True)
print(tab * 3 + tab.join(name for tipe, name in numbers))
    
sequence.close()