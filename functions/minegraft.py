from colorama import *
from functions.matriz_juego import *

# default player position PJ(x,y) // 2,11
# 11 is the row
# 2 is the column
x = 2 - 1
y = 11 - 1
wood_blocks= 0
stone_blocks = 0
estado_mira = "undefined"
bloque_destruido = [-1, -1]
look_right = False
changed = False


def draw_player():
    # 2, 11
    global x, y, estado_mira, changed

    if estado_mira == "right":

        # draw_selection
        # draw body
        juego[y - 1][x] = 4
        juego[y][x] = 4
        juego[y + 1][x] = 4
        # draw_selection
        juego[y][x + 1] = 6

    elif estado_mira == "left":
        # draw body
        juego[y - 1][x] = 4
        juego[y][x] = 4
        juego[y + 1][x] = 4
        # draw_selection
        juego[y][x - 1] = 6
    elif estado_mira == "destroy" or  estado_mira == "collect":
        juego[y - 1][x] = 4
        juego[y][x] = 4
        juego[y + 1][x] = 4
        # draw_selection
        juego[y][x + 1] = 6
        # draw_selection
        changed = True
    else:
        juego[y - 1][x] = 4
        juego[y][x] = 4
        juego[y + 1][x] = 4
        # draw_selection
        juego[y][x + 1] = 6


def draw_world():
    global x, y, look_right, changed, wood_blocks, stone_blocks
    draw_player()
    if juego[y][x + 1] == 6:
        look_right = True
    else:
        look_right = False
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
    print("REPORTE")
    print(" WOOD BLOCKS = ", wood_blocks)
    print(" STONE BLOCKS = ", stone_blocks)
    for i in range(0, 20):
        for j in range(0, 30):
            juego[i][j] = copia_juego[i][j]

    if changed:
        copia_juego[y][x + 1] = 0
        changed = False
    return ""

def move_player(instructions):
    # instructions could be : right, left, top, down
    instructions = instructions.split(" ")

    # position
    # 2,11
    # 3,11
    global x, y, muñeco_actual, estado_mira, wood_blocks, stone_blocks


    if instructions != ['']:
        for i, v in enumerate(instructions):
            if v == "right":
                estado_mira = "right"
                x = x + 1
            elif v == "left":
                estado_mira = "left"
                x = x - 1
            elif v == "destroy":
                estado_mira = "destroy"
                bloque_destruido[0] = y
                bloque_destruido[1] = x
                copia_juego[y][x + 1] = 0
            elif v == "collect":
                estado_mira = "destroy"
                bloque_destruido[0] = y
                bloque_destruido[1] = x
                copia_juego[y][x + 1] = 0
                wood_blocks += 1
        draw_world()
