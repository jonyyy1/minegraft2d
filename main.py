from functions.minegraft import *
from colorama import init

iniciar = input("escribe init para iniciar el juego : ")
while iniciar != 'init':
    iniciar = input("escribe init para iniciar el juego : ")
print(draw_world())

#una vez inicializado el programa se le pedira al usuario ingresar que accion quiere hace
accion = input("que accion deseas realizar : ")
move_player(accion)
while accion != '0':
    accion = input("que accion deseas realizar : ")
    move_player(accion)





