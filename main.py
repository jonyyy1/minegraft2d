from functions.minegraft import *
from colorama import init

iniciar = input("escribe init para iniciar el juego : ")
while iniciar != 'init':
    iniciar = input("escribe init para iniciar el juego : ")

print(draw_selection(3, 11))
print(draw_player(2, 11))

move_player = move_player("right ")
print(draw_world())
