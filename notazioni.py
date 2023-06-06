'''
creare metodo 'posiziona_navi' invece farlo nel main

Verificare che rimuove le navi
Verificare che mi riconosce la fine del gioco

METODO PRINCIPALE:
                'svolgi_gioco':
METODI:
        'crea_campo': Metodo che restituisce una rappresentazione testuale del campo di gioco
        'posiziona_navi': Metodo per posizionare le navi di un giocatore sul campo di gioco
        'aggiorna_campo': Metodo che stampa il campo di gioco mostrando la disposizione delle navi e i colpi sparati -> 'campo_pieno'
        'camppo_vuoto': Metodo che restituisce una stringa che rappresenta il campo di gioco aggiornato -> 'campo_aggiornato'
        'colpisci campo': Metodo che restituisce una stringa che rappresenta l'esito del colpo sparato
        'rimuovi_nave_affondata': Metodo che rimuove l'oggetto nave dal campo di gioco quando viene affondata
        'aggiungi_segnalazione': Metodo che aggiunge un punto dove viene sparato il colpo nel campo di gioco -> 'segno_colpo'


'''
#game_board.py
import sys
import ship_types
import Utils


def create_board(rows, cols, type_list):
    """
    Create the board of the game with each ship
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :param type_list: a list that contains the numbers of ships for each type
    :return: a game board and a list of each ship with its length, orientation, start row, start colum and coordinates
    """
    board = [[0] * cols for r in range(rows)]
    ship_list = []
    for i in type_list:
        Utils.user_message(i)
        successful_insertion = False
        trials = 0

        while not successful_insertion:
            try:
                start_row = int(input(f'\nInsert row. An integer from 1 to {rows}: '))
                start_col = int(input(f'\nInsert column. An integer from 1 to {cols}: '))
            except ValueError:
                print(f'\u001b[31m\nInvalid row and/or column, please try again!\033[0m')
                continue
            if not Utils.check_start_point(rows, cols, start_row, start_col):
                print('\u001b[31m\nError! The given starting point is not valid. Try again\033[0m')
                continue

            orientation = input('\nInsert orientation. Must be horizontal or vertical: \033[0m')
            if not Utils.check_orientation(orientation):
                print(
                    '\u001b[31m\nError! The given orientation is not valid. Try again making sure you spell correctly '
                    'your choice\033[0m')
                continue

            if orientation == 'horizontal':
                error, coordinates = check_horizontal_ship_positioning(rows, cols, board, start_row, start_col, i)
                if not error:
                    successful_insertion = True
            else:
                error, coordinates = check_vertical_ship_positioning(rows, cols, board, start_row, start_col, i)
                if not error:
                    successful_insertion = True
            print_board(board, rows, cols)
            if not successful_insertion:
                trials += 1
                if trials > 3:
                    print("\n"*30)
                    print("\u001b[31mToo many tries. Restart the game. Try using less ships or a bigger "
                          "field\033[0m")
                    sys.exit()

        if i == 5:
            ship = ship_types.Carrier(orientation, start_row, start_col, coordinates)
        elif i == 4:
            ship = ship_types.Battleship(orientation, start_row, start_col, coordinates)
        elif i == 3:
            ship = ship_types.Submarine(orientation, start_row, start_col, coordinates)
        elif i == 2:
            ship = ship_types.Destroyer(orientation, start_row, start_col, coordinates)
        ship_list.append(ship)
    return board, ship_list


def print_board(game_board, rows, cols):
    """
    Print a game board with inputs parameters
    :param game_board: the game board
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :return: the graphics of the board in the current state
    """
    print("\n  " + " ".join(str(x) for x in range(1, cols + 1)))
    for r in range(rows):
        print(str(r + 1) + " " + " ".join(str(c) for c in game_board[r]))
    print()


def check_horizontal_ship_positioning(rows, cols, board, start_row, start_col, size):
    """
    Check the horizontal position of the ship in the board and return a message of warning if the position
    in not valid. If a player fails too many times to position a ship (reasons could be for example: too many
    ships requested for a little field)
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :param board: the game board
    :param start_row: the start point of the row
    :param start_col: the start point of the colum
    :param size: the size of the ship
    :return: a logical parameter that is True is there is an error and false if not, and the coordinate
        of the ship (None if there is an error)
    """
    error = False
    if start_col + size - 1 <= cols:  # Check that the ship is on the board
        i = start_col - 1
        while i < start_col + size - 1 and not error:
            if board[start_row - 1][i] == 1:  # Check that I do not position over another ship
                print("\u001b[31m\n\nError! There is already another ship here\033[0m")
                error = True
                continue
            if start_row == 1:
                if board[start_row][i] == 1:  # If I'm on the first row, check not to have an adjacent ship in the
                    # second row
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_row == rows:  # If I am on the last row, check not to have an adjacent ship in the
                # penultimate row
                if board[start_row - 2][i] == 1:
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if 1 < start_row < rows:  # Check not to have an adjacent ship in the upper and lower row
                if board[start_row][i] == 1 or board[start_row - 2][i] == 1:
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_col != 1:
                if board[start_row - 1][start_col - 2] == 1:  # Check not to have an adjacent ship on the left
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_col + size - 2 != cols - 1:
                if board[start_row - 1][start_col + size - 1] == 1:  # Check not to have an adjacent ship on the right
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            i = i + 1
        if not error:
            coordinates = []
            for i in range(start_col - 1, start_col + size - 1):
                board[start_row - 1][i] = 1
                coordinates.append([start_row, i + 1])
            return error, coordinates
    else:
        error = True
        print("\u001b[31m\n\nError! Ship is out of board\033[0m")
    return error, None


def check_vertical_ship_positioning(rows, cols, board, start_row, start_col, size):
    """
    Check the vertical position of the ship in the board
    and return a message of warning if the position in not valid
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :param board: the game board
    :param start_row: the start point of the row
    :param start_col: the start point of the colum
    :param size: the size of the ship
    :return: a logical parameter that is True is there is an error and false, if not, and the coordinate
        of the ship (None if there is an error)
    """
    error = False
    if start_row + size - 1 <= rows:  # Check that the ship is on the board
        i = start_row - 1
        while i < start_row + size - 1 and not error:
            if board[i][start_col - 1] == 1:  # Check that I do not position over another ship
                print("\u001b[31m\n\nError! There is already another ship here\033[0m")
                error = True
                continue
            if start_col == 1:
                if board[i][start_col] == 1:  # If I'm on the first column, check not to have an adjacent ship
                    # in the second  column
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_col == cols:
                if board[i][start_col - 2] == 1:  # If I am on the last column, check not to have an adjacent
                    # ship in the penultimate column
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if 1 < start_col < cols:  # Check not to have an adjacent ship in the left and
                # right column
                if board[i][start_col] == 1 or board[i][start_col - 2] == 1:
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_row != 1:
                if board[start_row - 2][start_col - 1] == 1:  # Check not to have an adjacent ship above
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_row + size - 2 != rows - 1:
                if board[start_row + size - 1][start_col - 1] == 1:  # Check not to have an adjacent ship below
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            i = i + 1
        if not error:
            coordinates = []
            for i in range(start_row - 1, start_row + size - 1):
                board[i][start_col - 1] = 1
                coordinates.append([i + 1, start_col])
            return error, coordinates
    else:
        print("\u001b[31m\n\nError! Ship is out of board\033[0m")
        error = True
    return error, None

#game.py
import ship_types
import sys
import game_board
import Utils


def player_shoot(ship_list, rows, cols, play_board, player, game_end):
    """
         This method asks the player for the desired row or column for his shot
         then it checks if the shot is a hit, miss, sunks a ship or wins him the game
         :param ship_list: The player's ship list
         :param rows: The input given by the user for the number of rows of the board
         :param cols: The input given by the user for the number of columns of the board
         :param play_board: The player's game board
         :param player: The player shooting
         :param game_end: True if the game is finished, False otherwise
         :return: A console message to describe what the shot did
         :return: hit: Boolean value for the hit. True if the shot hits a ship, False otherwise
         :return: game_end: Boolean value for that describes if a game finished (True) or not (False)
         :return: player: Integer value that represents the player who has just shot. As only to players can play
            this game it can be either 1 or 2
         """
    hit = False
    game_board.print_board(play_board, rows, cols)
    row_guess, col_guess = Utils.choose_and_check_strike_point(rows, cols, play_board)
    for i in ship_list:
        if ship_types.Ship.is_hit(i, row_guess, col_guess):
            hit = True
            play_board[row_guess - 1][col_guess - 1] = 'X'
            if ship_types.Ship.is_sunk(i):
                if is_win(ship_list):
                    print(f'\nPlayer {player} wins the game')
                    game_end = True
                else:
                    print('\nHit and sunk a ship!')
            else:
                print('\nHit!')
    if not hit:
        print('\nMiss!')
        play_board[row_guess - 1][col_guess - 1] = 'O'
    return hit, game_end, player


def start_game(ship_list1, ship_list2, rows, cols, option, play_board1, play_board2):
    """
    This function starts the game in a Console mode and terminates the program as soon as the game ends
    :param ship_list1: Player 1's Ship list
    :param ship_list2: Player 2's Ship list
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :param option: The input given by the user for the game option
    :param play_board1: Player 1's game board
    :param play_board2: Player 2's game board
    :return: None
    """
    print("\n\n\n\n\n\nPlayer 1 will start the game!")
    hit, game_end, player = player_shoot(ship_list2, rows, cols, play_board2, 1, game_end=False)
    while not game_end:
        hit, game_end, player = switch_player(hit, player, ship_list1, ship_list2, rows, cols, option, play_board1, play_board2, game_end)
    sys.exit()


def switch_player(hit, player, ship_list1, ship_list2, rows, cols, option, play_board1, play_board2, game_end):
    """
    This function decides when to switch player turn depending on:
        1) If it's a hit or a miss
        2) The option parameter given to the program
    :param hit: True if the last shot was a hit, False otherwise
    :param player: The player who shot last turn
    :param ship_list1: Player 1's Ship list
    :param ship_list2: Player 2's Ship list
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :param option: The input given by the user for the game option
    :param play_board1: Player 1's game board
    :param play_board2: Player 2's game board
    :param game_end: True if the game is finished, False otherwise
    :return: hit: Boolean value for the hit. True if the shot hits a ship, False otherwise
    :return: game_end: Boolean value for that describes if a game finished (True) or not (False)
    :return: player: The same or the other player depending on the result of the function
    """
    if player == 1:
        if hit and option == 0:
            print('\nYou can shoot again!')
            hit, game_end, player = player_shoot(ship_list2, rows, cols, play_board2, player, game_end)
        else:
            player = 2
            print(f'\nPass the computer to Player {player}')
            hit, game_end, player = player_shoot(ship_list1, rows, cols, play_board1, player, game_end)
    else:
        if hit and option == 0:
            print('\nYou can shoot again!')
            hit, game_end, player = player_shoot(ship_list1, rows, cols, play_board1, player, game_end)
        else:
            player = 1
            print(f'\nPass the computer to Player {player}')
            hit, game_end, player = player_shoot(ship_list2, rows, cols, play_board2, player, game_end)
    return hit, game_end, player


def is_win(ship_list):
    """
    :param ship_list:the list of ships of the enemy player
    :return: a logical value that returns true if the player won the game
    """
    j = 0
    is_alive = False
    while j < len(ship_list) and not is_alive:
        if not (ship_types.Ship.is_sunk(ship_list[j])):
            is_alive = True
        j = j + 1
    return not is_alive

# utils.py
import ship_types
import sys
import game_board
import Utils


def player_shoot(ship_list, rows, cols, play_board, player, game_end):
    """
         This method asks the player for the desired row or column for his shot
         then it checks if the shot is a hit, miss, sunks a ship or wins him the game
         :param ship_list: The player's ship list
         :param rows: The input given by the user for the number of rows of the board
         :param cols: The input given by the user for the number of columns of the board
         :param play_board: The player's game board
         :param player: The player shooting
         :param game_end: True if the game is finished, False otherwise
         :return: A console message to describe what the shot did
         :return: hit: Boolean value for the hit. True if the shot hits a ship, False otherwise
         :return: game_end: Boolean value for that describes if a game finished (True) or not (False)
         :return: player: Integer value that represents the player who has just shot. As only to players can play
            this game it can be either 1 or 2
         """
    hit = False
    game_board.print_board(play_board, rows, cols)
    row_guess, col_guess = Utils.choose_and_check_strike_point(rows, cols, play_board)
    for i in ship_list:
        if ship_types.Ship.is_hit(i, row_guess, col_guess):
            hit = True
            play_board[row_guess - 1][col_guess - 1] = 'X'
            if ship_types.Ship.is_sunk(i):
                if is_win(ship_list):
                    print(f'\nPlayer {player} wins the game')
                    game_end = True
                else:
                    print('\nHit and sunk a ship!')
            else:
                print('\nHit!')
    if not hit:
        print('\nMiss!')
        play_board[row_guess - 1][col_guess - 1] = 'O'
    return hit, game_end, player


def start_game(ship_list1, ship_list2, rows, cols, option, play_board1, play_board2):
    """
    This function starts the game in a Console mode and terminates the program as soon as the game ends
    :param ship_list1: Player 1's Ship list
    :param ship_list2: Player 2's Ship list
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :param option: The input given by the user for the game option
    :param play_board1: Player 1's game board
    :param play_board2: Player 2's game board
    :return: None
    """
    print("\n\n\n\n\n\nPlayer 1 will start the game!")
    hit, game_end, player = player_shoot(ship_list2, rows, cols, play_board2, 1, game_end=False)
    while not game_end:
        hit, game_end, player = switch_player(hit, player, ship_list1, ship_list2, rows, cols, option, play_board1, play_board2, game_end)
    sys.exit()


def switch_player(hit, player, ship_list1, ship_list2, rows, cols, option, play_board1, play_board2, game_end):
    """
    This function decides when to switch player turn depending on:
        1) If it's a hit or a miss
        2) The option parameter given to the program
    :param hit: True if the last shot was a hit, False otherwise
    :param player: The player who shot last turn
    :param ship_list1: Player 1's Ship list
    :param ship_list2: Player 2's Ship list
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :param option: The input given by the user for the game option
    :param play_board1: Player 1's game board
    :param play_board2: Player 2's game board
    :param game_end: True if the game is finished, False otherwise
    :return: hit: Boolean value for the hit. True if the shot hits a ship, False otherwise
    :return: game_end: Boolean value for that describes if a game finished (True) or not (False)
    :return: player: The same or the other player depending on the result of the function
    """
    if player == 1:
        if hit and option == 0:
            print('\nYou can shoot again!')
            hit, game_end, player = player_shoot(ship_list2, rows, cols, play_board2, player, game_end)
        else:
            player = 2
            print(f'\nPass the computer to Player {player}')
            hit, game_end, player = player_shoot(ship_list1, rows, cols, play_board1, player, game_end)
    else:
        if hit and option == 0:
            print('\nYou can shoot again!')
            hit, game_end, player = player_shoot(ship_list1, rows, cols, play_board1, player, game_end)
        else:
            player = 1
            print(f'\nPass the computer to Player {player}')
            hit, game_end, player = player_shoot(ship_list2, rows, cols, play_board2, player, game_end)
    return hit, game_end, player


def is_win(ship_list):
    """
    :param ship_list:the list of ships of the enemy player
    :return: a logical value that returns true if the player won the game
    """
    j = 0
    is_alive = False
    while j < len(ship_list) and not is_alive:
        if not (ship_types.Ship.is_sunk(ship_list[j])):
            is_alive = True
        j = j + 1
    return not is_alive

# inputs.py
import argparse
import sys


def initialize_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--rows",
                        help="Number of rows of the board",
                        type=int,
                        default=9)

    parser.add_argument("-c", "--columns",
                        help="Number of columns of the board",
                        type=int,
                        default=9)

    parser.add_argument("-s1", "--carriers",
                        help="The number of Carriers of your fleet, if not specified, equal to 1. The size of a "
                             "Carrier is 5.",
                        type=int,
                        default=1)

    parser.add_argument("-s2", "--battleships",
                        help="The number of Battleships of your fleet, if not specified, equal to 1. The size of a "
                             "Battleship is 4",
                        type=int,
                        default=1)

    parser.add_argument("-s3", "--submarines",
                        help="The number of Submarines of your fleet, if not specified, equal to 1. The size of a "
                             "Submarine is 3",
                        type=int,
                        default=1)

    parser.add_argument("-s4", "--destroyers",
                        help="The number of Destroyers of your fleet, if not specified, equal to 1. The size of a "
                             "Destroyer is 2",
                        type=int,
                        default=1)

    parser.add_argument("-o", "--option",
                        help="The variant of the game you want to play: 0 if after a Hit you can shoot again, "
                             "1 otherwise",
                        type=int,
                        default=0)

    parser.add_argument("-g", "--graphics",
                        help="If you want to play with graphical interface use 1. If not use 0 or don't call this "
                             "parameter",
                        type=int,
                        default=0)

    return parser.parse_args()


def check_parser(args):
    try:
        check_arguments(args)
    except ValueError:
        sys.exit()


def check_arguments(args):
    if not 0 < args.rows < 100:
        print('\u001b[31mInvalid number of rows\033[0m')
        raise ValueError
    if not 0 < args.columns < 100:
        print('\u001b[31mInvalid number of columns\033[0m')
        raise ValueError
    if not 0 <= args.carriers <= 2:
        print('\u001b[31mInvalid number of carriers\033[0m')
        raise ValueError
    if not 0 <= args.battleships <= 3:
        print('\u001b[31mInvalid number of battleships\033[0m')
        raise ValueError
    if not 0 <= args.submarines <= 4:
        print('\u001b[31mInvalid number of submarines\033[0m')
        raise ValueError
    if not 0 <= args.destroyers <= 5:
        print('\u001b[31mInvalid number of destroyers\033[0m')
        raise ValueError
    if not (args.option == 0 or args.option == 1):
        print('\u001b[31mInvalid input "option". It must be 0 or 1\033[0m')
        raise ValueError
    if not (args.graphics == 0 or args.graphics == 1):
        print('\u001b[31mInvalid input "graphics". It must be 0 or 1\033[0m')
        raise ValueError
# min.py
# This file is for the main execution of the program.

import game_board
import gui
import inputs
import game
import Utils

args = inputs.initialize_parser()
inputs.check_parser(args)

type_list = Utils.create_ship_type_list(args.carriers, args.battleships, args.submarines, args.destroyers)
board_player1, ship_list1 = game_board.create_board(args.rows, args.columns, type_list)
input('\n\nPress enter and pass the computer to the other player:')
print("\n"*30)
board_player2, ship_list2 = game_board.create_board(args.rows, args.columns, type_list)
input('\n\nPress enter and pass the computer to the other player to start playing:')
print("\n"*30)

if args.graphics == 1:
    app = gui.GuiApp(args.rows, args.columns, args.option, ship_list1, ship_list2, board_player1, board_player2)
    app.mainloop()
else:
    play_board1 = [['-'] * args.columns for x in range(args.rows)]
    play_board2 = [['-'] * args.columns for x in range(args.rows)]
    game.start_game(ship_list1, ship_list2, args.rows, args.columns, args.option, play_board1, play_board2)


# ship.py
# This file contains the definition and methods of all the ships that a user can create in the game.


# Base Ship class from which every other sub-Ship-class will inherit
class Ship:
    """
    The constructor which receives:
    :param size: The length of the ship
    :param orientation: The direction of the ship (horizontal or vertical)
    :param start-row/start-col: The starting point of the ship for the positioning
    :param coordinates: A list of the occupied coordinates by the ship
    """

    def __init__(self, size, orientation, start_row, start_col, coordinates=None):
        self.size = size
        self.orientation = orientation
        self.start_row = start_row
        self.start_col = start_col
        self.hits = 0

        if coordinates is None:
            self.coordinates = []
        else:
            self.coordinates = coordinates

    # This method checks if a ship is sunk
    def is_sunk(self):
        """
        This method checks if the ship is sunk
        :return: A Boolean value: True if the ship is sunk, False otherwise
        """
        if self.hits == self.size:
            return True
        else:
            return False

    def is_hit(self, row_guess, col_guess):
        """
        This method verifies if the shot given is a hit. If it is, removes from the ship the coordinates of the hit and
        increments the number of hits taken
        :param row_guess: The row coordinate of the shot
        :param col_guess: The column coordinate of the shot
        :return: A Boolean value: True if the ship is hit, False otherwise
        """
        if self.check_hit(row_guess, col_guess):
            self.coordinates.remove([row_guess, col_guess])
            self.hits += 1
            return True
        return False

    def check_hit(self, row_guess, col_guess):
        """
        This method checks if the shot given is a hit
        :param row_guess: The row coordinate of the shot
        :param col_guess: The column coordinate of the shot
        :return: A Boolean value: True if the ship is hit, False otherwise
        """
        if [row_guess, col_guess] in self.coordinates:
            return True
        return False


# All the subclasses need only a default size, all the other attributes can be inherited for the super_class Ship
class Carrier(Ship):
    def __init__(self, orientation, start_row, start_col, coordinates):
        super().__init__(5, orientation, start_row, start_col, coordinates)


class Battleship(Ship):
    def __init__(self, orientation, start_row, start_col, coordinates):
        super().__init__(4, orientation, start_row, start_col, coordinates)


class Submarine(Ship):
    def __init__(self, orientation, start_row, start_col, coordinates):
        super().__init__(3, orientation, start_row, start_col, coordinates)


class Destroyer(Ship):
    def __init__(self, orientation, start_row, start_col, coordinates):
        super().__init__(2, orientation, start_row, start_col, coordinates)
