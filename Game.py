from Board import Board


class Game:
    def __init__(self, board, computer):
        self._board = board
        self._current_player = 1
        self._computer = computer
        

    @property
    def Board(self):
        return self._board

    @property
    def Current_Player(self):
        return self._current_player
    '''
    - function that receives a column makes a move for the user/player on that column and sets the current player to 2 (computer)
    '''
    def make_player_move(self,column):
        self._board.make_move(column,self._current_player)
        self._current_player = 2

    '''
    - function that makes a move for the computer and sets the current player to 1 (user)
    '''
    def make_computer_move(self):
        self._board.make_move(self._computer.make_move_to_win(self._board),self._current_player)
        self._current_player = 1