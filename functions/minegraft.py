from colorama import *
from functions.matriz_juego import *
# default player position PJ(x,y) // 2,11
# 11 is the row
# 2 is the column
x = 2 - 1
y = 11 - 1
wood_blocks= 0
stone_blocks = 0
estado = ""
m = 0
n = 30
def draw_player():
    # 2, 11
    global x, y
    juego[y - 1][x] = 4
    juego[y][x] = 4
    juego[y + 1][x] = 4
    # draw_selection
    if estado == "left":
        juego[y][x - 1] = 6
    else:
        juego[y][x + 1] = 6
def build():
    global x,y
    copia_juego[y][x+1] = 8
    #aqui se puede recibir por parametro el colo que quiere el usuario poner ahi gaaaaa
def draw_world():
    global x, y, wood_blocks, stone_blocks, m, n
    draw_player()
    for i in range(0, 20):
        for j in range(m, n):
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
    #aqui lo que hago es copiar en juego copia_juego
    for i in range(0, 20):
        for j in range(0, 40):
            juego[i][j] = copia_juego[i][j]
    return ""

def move_player(instructions):
    # instructions could be : right, left, top, down
    instructions = instructions.split(" ")
    # position
    # 2,11
    # 3,11
    global x, y, muñeco_actual, estado, wood_blocks, stone_blocks, m, n
    if instructions != ['']:
        for i, v in enumerate(instructions):
            if v == "right" :
                if x < 38 :
                    estado = "right"
                    x = x + 1
                    print(x)
                    if x >= n - 15 and x < 25:
                        print("entro")
                        m += 1
                        n += 1
                else:
                    print("invalid operation : recuerda que no puedes salir del rango del mapa")

            elif v == "left" :
                if x > 1 :
                    estado = "left"
                    x = x - 1
                    if x <= n - 15 and x >= 15:
                        m -= 1
                        n -= 1
                else:
                    print("invalid operation : recuerda que no puedes salir del rango del mapa")

            elif v == "up" :
                estado = "up"
                y = y - 1
            elif v == "down" :
                estado = "down"
                y = y + 1
            elif v == "destroy":
                #tierra, pasto, sol y agua
                if copia_juego[y][x+1] == 8 or copia_juego[y][x+1] == 2 or copia_juego[y][x+1] == 1 or copia_juego[y][x+1] == 7 :
                    estado = "destroy"
                    copia_juego[y][x + 1] = 0
                else :
                    print("invalid operation")
            elif v == "collect" :
                #madera y piedra
                if copia_juego[y][x+1] == 3 :
                    copia_juego[y][x + 1] = 0
                    wood_blocks += 1
                elif copia_juego[y][x+1] == 5 :
                    copia_juego[y][x + 1] = 0
                    stone_blocks += 1
                else :
                    print("invalid operation")
            elif v == "build" :
                build()
        draw_world()

