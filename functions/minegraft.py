from colorama import *
from functions.matriz_juego import *

# default player position PJ(x,y) // 2,11
# 11 is the row
# 2 is the column
x = 2 - 1
y = 11 - 1

def draw_player():
    # 2, 11
    global x, y
    # draw body
    juego[y - 1][x] = 4
    juego[y][x] = 4
    juego[y + 1][x] = 4
    # draw_selection
    juego[y][x + 1] = 6


draw_player()


def draw_world():
    for i in range(0, 20):
        for j in range(0, 30):
            if juego[i][j] == 0:
                print(Back.LIGHTWHITE_EX + '   ', end="")
                print(Style.RESET_ALL + '', end="")
            elif juego[i][j] == 1:
                print(Back.YELLOW + '   ', end="")
                print(Style.RESET_ALL + '', end="")
            elif juego[i][j] == 2:
                print(Back.GREEN + '   ', end="")
                print(Style.RESET_ALL + '', end="")
            elif juego[i][j] == 3:
                print(Back.RED + '   ', end="")
                print(Style.RESET_ALL + '', end="")
            elif juego[i][j] == 4:
                print(Back.CYAN + '   ', end="")
                print(Style.RESET_ALL + '', end="")
            elif juego[i][j] == 5:
                print(Back.LIGHTBLACK_EX + '   ', end="")
                print(Style.RESET_ALL + '', end="")
            elif juego[i][j] == 6:
                print(Back.MAGENTA + '   ', end="")
                print(Style.RESET_ALL + '', end="")
            elif juego[i][j] == 7:
                print(Back.BLUE + '   ', end="")
                print(Style.RESET_ALL + '', end="")
            elif juego[i][j] == 8:
                print(Back.BLACK + '   ', end="")
                print(Style.RESET_ALL + '', end="")

        print("")
    return ""


def move_player(instructions):
    # instructions could be : right, left, top, down
    instructions = instructions.split(" ")
    print(instructions)
    # position
    # 2,11
    # 3,11
    global x, y
    print("x", x)
    print("y", y)

    if instructions != ['']:
        for i, v in enumerate(instructions):
            '''saber si el muñeco esta mirando hacia la derecha o izquierda
            True -> mirando hacia la derecha
            False -> mirando hacia la izquierda'''

            if juego[y][x + 1] == 6:
                look_right = True
            else:
                look_right = False

            if look_right:
                juego[y][x + 1] = 0
                juego[y - 1][x] = 0
                juego[y][x] = 0
                juego[y + 1][x] = 0
            else:
                juego[y][x - 1] = 0
                juego[y - 1][x] = 0
                juego[y][x] = 0
                juego[y + 1][x] = 0

            if v == "right":
                print("entro a right")
                if look_right:
                    juego[y - 1][x + 1] = 4
                    juego[y][x + 1] = 4
                    juego[y + 1][x + 1] = 4
                    juego[y][x + 2] = 6
                    x = x + 1
                else:
                    juego[y - 1][x] = 4
                    juego[y][x] = 4
                    juego[y + 1][x] = 4
                    juego[y][x + 1] = 6


            elif v == "left":
                print("entro a left")
                print(juego[y][x + 1])
                # si cumple esto es porque el muñeco esta a la mirando hacia la derecha
                if look_right:
                    juego[y - 1][x] = 4
                    juego[y][x] = 4
                    juego[y + 1][x] = 4
                    juego[y][x - 1] = 6
                else:  # esta mirando hacia la izquierda
                    juego[y - 1][x - 1] = 4
                    juego[y][x - 1] = 4
                    juego[y + 1][x - 1] = 4
                    juego[y][x - 2] = 6
                    x = x - 1

            elif v == "top":
                juego[y - 2][x] = 4
                juego[y - 1][x] = 4
                juego[y][x] = 4
                if juego[x + 1] == 6:
                    juego[y - 1][x + 1] = 6
                else:
                    juego[y - 1][x - 1] = 6
                print("top")
            elif v == "down":
                print("down")

        draw_world()
