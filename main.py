from time import sleep
import random
import os

RED = "\u001b[48;5;88m"
WHITE = "\u001b[47m"
BLUE = "\u001b[48;5;17m"
PIX = "   "
RESET = "\u001b[0m"

#последовательность
def draw_bar(path, bar_width = 25, speed = 0.2):
    #Открываем файл
    file = open(path)
    nums = [float(i) for i in file]
    file.close()
    #Разделяем на нужные группы
    group_1 = [i for i in nums if i > 5]
    group_2 = [i for i in nums if 0 < i < 5]
    lens = len(group_1 + group_2)
    #Считаем процент группы
    procent_1 = round(len(group_1) / lens, 2)
    procent_2 = (1 - procent_1) * 100
    procent_1_on_bar = int(procent_1 * bar_width)
    #отрисовка
    for i in range(1, bar_width + 1):
        if i <= procent_1_on_bar:
            print(f"{RED}{PIX}{RESET}", end = "", flush = True)
            sleep(0.1)
        else:
            print(f"{BLUE}{PIX}{RESET}", end = "", flush = True)
            sleep(0.1)

    print(f"\r{RED}group 1: {procent_1 * 100}%{RESET}\r\u001b[{procent_1_on_bar * len(PIX)}C{BLUE}group 2: {procent_2}%{RESET}")

#флаг_таиланда
def draw_Thailand_flag(scale = 1):
    flag = ""
    sequence = [RED, WHITE, BLUE, BLUE, WHITE, RED]
    line_height = 1 * int(scale)
    width = 9 * int(scale)
    for color in sequence:
        flag += f"{color}{PIX * width}{RESET}\n" * line_height
    print(flag)

#анимация
def run_animation(size = 10, speed = 0.2):
    #получаем центральную позицию в терминале
    X = size // 2
    Y = size // 2
    PIX = " "
    colors = [RED, BLUE, WHITE]
    #запускаем анимацию (делим на 2, так как квадрат расширяется во все направления)
    while True:
        for i in range(0, size // 2):
            #получаем координаты ободка
            coords = [(x, y) for x in range(X - i, X + i + 1) for y in range(Y - i, Y + i + 1) if max(abs(X - x), abs(Y - y)) == i]
            color = colors[random.randint(0, len(colors) - 1)]
            for x, y in coords:
                print(f"\u001b[{y};{x}H", end = "")
                print(f"{color}{PIX}{RESET}", end = "")
            print(f"\u001b[{0};{0}H", end = "")
            print("\n" * size)
            sleep(speed)
            #очищаем терминал
            os.system("cls")

#узор
def draw_design(scale = 1, line = 3, column = 1, speed = 0.1):
    #задает длину первой линии
    height = int(scale * 3)
    for col in range(column):
        print("\n" * (height) , end = "")
        #Рисуем узор
        for c in range(line):
            #Идем по алгоритму: сначала поднимаясь, потом опускаясь
            for i in range(height, 0, - 1):
                print(f"\u001b[1A",end = "")
                for j in range(i):
                    print(f"{RED}{PIX * 1}{RESET}", end="", flush = True)
                    sleep(speed)
            for i in range(2, height + 1):
                print(f"\u001b[1B",end = "")
                for j in range(i):
                    print(f"{RED}{PIX * 1}{RESET}", end="", flush = True)
                    sleep(speed)
            #опускаемся на один вниз, так как в начале поднимаемся
            print(f"\u001b[1B",end = "")

#draw_Thailand_flag(scale = 2)
#draw_design(scale = 1.2, line = 3, column = 3)
run_animation()
#draw_bar("лаба\sequence.txt")
