import random
import csv
from datetime import datetime

#piedra = 1, papel = 2, tijera = 3 / rock = 1, paper = 2, scissors = 3

#función que calcula la opción de la pc, luego configurado para elegir entre 1 y 3
#it calculates a random number for the pc
def pc_turn (min, max):
    result = random.randint(min, max)
    return result

#función que muestra la elección de cada valor, piedra para 1, papel para 2 y tijera para 3
#it shows the chosen option
def choices (digit):
    alert = ''
    if(digit == 1):
        alert = 'PIEDRA ✊'
    elif(digit == 2):
        alert = 'PAPEL ✋'
    elif(digit == 3):
        alert = 'TIJERA ✌'
    else:
        #raise ValueError('Ingresaste un número incorrecto.') se desestima ya que corta el programa y se usa un bucle while en su lugar
        alert = 'Ingresaste un número incorrecto.'
    return alert

#función que pone en funcionamiento el juego, se implementa un bucle if para los 3 posibles escenarios
#se decide crear un historial que guarde la información del resultado y la fecha
#function to play the game, with 3 possible outcomes: tie, win, lose
#there is a history file which saves the outcome of the game and its date
def play_game(player, pc):
    if(player == pc):
        print('Empate 😐')
        with open('history.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().replace(microsecond=0), ' empate'])
    elif(player - pc == -2 or player - pc == 1):
        print('¡Ganaste! 😁')
        with open('history.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().replace(microsecond=0), ' victoria'])
    else:
        print('Perdiste 🙁')
        with open('history.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().replace(microsecond=0), ' derrota'])

#elección de la pc
pc_choose = pc_turn(1,3)

#elección del jugador, formateado a número entero
#the player enters a number
player_choose = int(input('Elige 1 para piedra, 2 para papel y 3 para tijeras'))

#el bucle while se usa en caso de que se ingresen valores diferentes a los solicitados
#while loop, in case the player enters a wrong number
while(player_choose != 1 and player_choose != 2 and player_choose != 3):
    print(choices(player_choose))
    repeat = int(input('Elige 1 para piedra, 2 para papel y 3 para tijeras'))
    player_choose = repeat
else:
    print('Elegiste', choices(player_choose))
    print('La PC elige', choices(pc_choose))
    play_game(player_choose, pc_choose)