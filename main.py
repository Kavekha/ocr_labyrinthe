"""
Q = Save & quit
N = North
E = Est
S = Sud
O = Ouest
+nb = Nombre de cases.
(E3 = 3 cases à l'Est)

autosave à chaque coup

proposer plusieurs cartes editables (importées depuis .txt)

si partie existante, proposer de rejouer la partie.
choix de la carte.

O = Mur
. = porte
U = sortie
X = Robot
Si ., le robot peut passer mais X cache .

"""

from enum import Enum
import constantes
from utils.input_validators import is_valid_input
from game.map_builder import Builder
import os



def render_interface(gmap):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(gmap)


def play_input_command(player_input, gmap):
    if not is_valid_input(player_input):
        print(constantes.TXT_NOT_A_VALID_INPUT)
        return False

    dir = player_input[0]
    try:
        nb_moves = int(player_input[1:])
    except Exception as e:
        print(f'[warning] try to move : {e}')
        raise NotImplementedError

    try_to_move(gmap, dir, nb_moves)
    return True


def try_to_move(gmap, dir, nb_moves=1):
    for move in range(1, nb_moves + 1):
        if not gmap.is_tile_available(dir):
            print(constantes.TEXT_NO_PATH_AVAILABLE)
            return
    for move in range(1, nb_moves + 1):
        gmap.move_player(dir)


def main():
    gmap = Builder(constantes.CARTE_WORK).start()

    render_interface(gmap)
    while True:
        player_input = input(constantes.TXT_REQUEST_INPUT)
        play_input_command(player_input, gmap)
        render_interface(gmap)


if __name__ == '__main__':
    main()