from functions.minegraft import *
from colorama import init

iniciar = input("escribe init para iniciar el juego : ")
while iniciar != 'init':
    iniciar = input("escribe init para iniciar el juego : ")
print(draw_world())


move_player = move_player("right right left left left right")





