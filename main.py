from functions.minegraft import dibujar_mundo
from colorama import init

iniciar = input("escribe init para iniciar el juego : ")
while iniciar != 'init':
    iniciar = input("escribe init para iniciar el juego : ")


print(dibujar_mundo())