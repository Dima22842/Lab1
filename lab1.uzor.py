import time;
black= "\033[40m    \033[0m"
white= "\033[0m    \033[0m"
while True:
    print(black+white+black)
    print(white+black+white)
    print(black+white+black)
    print(white)
    time.sleep(0.5)