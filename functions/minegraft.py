from colorama import *

colores = ['RED', 'BLUE', 'YELLOW', 'CYAN', 'WHITE']
juego = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 3, 0, 0, 2, 0, 0, 0, 2, 0],
         [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 2, 2, 2, 0, 2, 2, 2],
         [0, 4, 0, 0, 3, 0, 0, 5, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 3, 0],
         [0, 4, 6, 0, 3, 0, 5, 5, 5, 0, 3, 0, 0, 0, 0, 5, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 3, 0],
         [0, 4, 0, 0, 3, 0, 5, 5, 5, 0, 3, 5, 0, 0, 5, 5, 3, 0, 0, 5, 0, 3, 0, 0, 3, 0, 0, 0, 3, 5],
         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 7, 7, 2, 2],
         [8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 8, 8],
         [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 8, 5, 7, 7, 7, 8, 8],
         [8, 8, 8, 8, 8, 8, 5, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 7, 7, 7, 8, 8],
         [8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 7, 7, 7, 8, 8],
         [8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 8, 8],
         [8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 8],
         [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
         ]



def dibujar_mundo():
    for i in range(0, 20):
        for j in range(0, 30):
            if juego[i][j] == 0:
                print(Back.WHITE + '   ', end="")
                print(Style.RESET_ALL+'',end="")
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
                print(Back.YELLOW + '   ', end="")
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
