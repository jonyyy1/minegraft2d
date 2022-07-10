from functions.minegraft import *
from colorama import init

iniciar = input("Escribe init para iniciar el juego : ")
while iniciar != 'init':
    iniciar = input("Escribe init para iniciar el juego : ")
print("Welcome to the world of minecraft 2d xyz")
print(draw_world())

#una vez inicializado el programa se le pedira al usuario ingresar que accion quiere hace
accion = input("¿Qué acción deseas realizar? : ")
move_player(accion)

while accion != '0':
    accion = input("¿Qué acción deseas realizar? : ")
    move_player(accion)





