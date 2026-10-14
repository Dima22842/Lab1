import time


black = "\033[40m    \033[0m"
tab = "    "

while True:
    print(f"{black}{tab}{black}")
    print(f"{tab}{black}{tab}")
    print(f"{black}{tab}{black}")
    print(tab)

    time.sleep(0.5)
