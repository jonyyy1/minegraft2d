from colorama import *

colores = ['RED', 'BLUE', 'YELLOW', 'CYAN', 'WHITE']
juego = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 3, 0, 0, 2, 0, 0, 0, 2, 0],
         [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 2, 2, 2, 0, 2, 2, 2],
         [0, 0., 0, 0, 3, 0, 0, 5, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 3, 0],
         [0, 0., 0, 0, 3, 0, 5, 5, 5, 0, 3, 0, 0, 0, 0, 5, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 3, 0],
         [0, 0., 0, 0, 3, 0, 5, 5, 5, 0, 3, 5, 0, 0, 5, 5, 3, 0, 0, 5, 0, 3, 0, 0, 3, 0, 0, 0, 3, 5],
         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 7, 7, 2, 2],
         [8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 8, 8],
         [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 8, 5, 7, 7, 7, 8, 8],
         [8, 8, 8, 8, 8, 8, 5, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 7, 7, 7, 8, 8],
         [8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 7, 7, 7, 8, 8],
         [8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 8, 8],
         [8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 8],
         [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
         ]



def draw_world():
    for i in range(0, 20):
        for j in range(0, 30):
            if juego[i][j] == 0:
                print(Back.LIGHTWHITE_EX + '   ', end="")
                print(Style.RESET_ALL+'', end="")
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

def draw_player(x,y):
    #11,2
    x = x-1
    y = y-1
    juego[y-1][x] = 4
    juego[y][x] = 4
    juego[y + 1][x] = 4
def draw_selection(x,y):
    x = x - 1
    y = y - 1
    juego[y][x]= 6


def move_player(cadena):
    #right left top down
    cadena = cadena.split(" ")
    #posicion
    #2,11
    #3,11
    x = 2-1
    y = 11-1
    juego[y -1][x] = 0
    juego[y][x] = 0
    juego[y +1][x] = 0
    juego[y][x+1] = 0
    for i in cadena:
        if i == "right":
            print("entro")
            juego[y-1][x+1]=4
            juego[y][x+1]=4
            juego[y+1][x+1]=4
            juego[y][x+2] = 6
        elif i == "left":
            print("left")
        elif i == "top":
            print("top")
        elif i == "down":
            print("down")

