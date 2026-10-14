import os
import random
import time

tab = "    "

while True:
    num1 = random.randint(0, 3)
    num2 = random.randint(4, 7)

    color1 = f"\033[4{num1}m    \033[0m"
    color2 = f"\033[4{num2}m    \033[0m"

    print(f"{color1}{color2}{color1}")
    print(f"{color2}{color1}{color2}")
    print(f"{color1}{color2}{color1}")
    print(tab)

    time.sleep(0.5)

    os.system("cls")
