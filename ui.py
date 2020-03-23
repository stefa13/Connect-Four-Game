from os import system
from sys import exit
from exceptions import GameWonException, NoWinningException
class UI:
    def __init__(self,game):
        self._game = game

    def _print_board(self,print_player = True):
        system("cls")
        print(self._game.Board)
        if print_player:
            print("Player {}, please make a move.".format(self._game.Current_Player))

    def _get_input(self):
        try:
            return int(input("Column: "))
        except ValueError:
            raise ValueError("Column must be an integer!")

    def _next_move(self):
        while True:
            try:
                if self._game.Current_Player == 1:
                    column = self._get_input()
                    self._game.make_player_move(column-1)
                else:
                    self._game.make_computer_move()
                break
            except GameWonException as won:
                self._print_board(False)
                print(str(won)+"\n")
                exit()
            except NoWinningException as nw:
                self._print_board(False)
                print(str(nw)+"\n")
                exit()
            except Exception as e:
                print(str(e)+"\n")

    def run(self):
        while True:
            self._print_board()
            self._next_move()