import constantes


def is_valid_direction(mut_player_input):
    """mut_player_input has been modified for : lower case. Only one char.
    return True if valid direction"""
    if mut_player_input in constantes.GAME_AVAILABLE_DIRECTIONS:
        return True
    return False


def is_valid_move_number(mut_player_input):
    """mut_player_input est une serie de chiffres de type str
    return True if valid move number ou rien"""
    if not mut_player_input:
        return True

    try:
        int(mut_player_input)
        return True
    except ValueError:
        # ne peut pas etre converti en nombre.
        return False
    except Exception as e:
        print(f'[WARNING] error in is_valid_move_number : {e}')
        raise Exception


def is_valid_input(player_input):
    """ player_input est modifié pour offrir une marge d'erreur à l'utilisateur (maj au lieu de minuscule etc)
    on check la direction puis le nombre de cases."""

    if type(player_input) == int:
        player_input = str(player_input)
    player_input = player_input.lower()

    if not is_valid_direction(player_input[0]):
        return False

    if len(player_input) < 2:
        return True

    if is_valid_move_number(player_input[1:]):
        return True

    return False