from texttable import Texttable
from exceptions import InvalidColumnException, GameWonException, NoWinningException

class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._cell_number = 4
        self._init_board()
    @property
    def Columns(self):
        return self._columns

    @property
    def Rows(self):
        return self._rows
    '''
    - function that initializes the matrix (that is going to be the board of the game) with values of 0
    '''
    def _init_board(self):
        self._data = []
        for i in range(self._rows):
            self._data.append([0] * self._columns)

    def get_value(self,row,column):
        return self._data[row][column]
    '''
    - function that returns the last row that is free from a given column
    if there is no such a row, it will raise an exception
    '''
    def last_free_row(self,column):
        if column < 0 or column >= self._columns:
            raise InvalidColumnException("Column must be between {} and {}".format(1, self._columns))
        for row in range(self._rows-1,-1,-1):
            if self._data[row][column] == 0:
                return row
        raise InvalidColumnException("Column is full. Try another column.")
    '''
    - function that checks wheather a column is available(not full) or not and returns True/False accordingly
    '''
    def available_column(self, column):
        try:
            self.last_free_row(column)
            return True
        except InvalidColumnException:
            return False
    '''
    - function that makes a move meaning taht it places 1/2 on the board according to user/computer;
    if someone has won, it raises an exception
    '''
    def make_move(self,column,player):
        row = self.last_free_row(column)
        self.place_value(row,column,player)
        if self.check_if_player_won(player):
            raise GameWonException("Player {} won! Congrats!".format(player))
        if self.no_winning():
            raise NoWinningException("No one won :( ")

    '''
    - function that places a given value on a given row and column
    '''
    def place_value(self,row,column, val):
        self._data[row][column]=val
    '''
    - function that checks wheather a given player has won in one of the 3 situations;
    if it has, it returns True
    '''
    def check_if_player_won(self,player):
        #check rows
        for row in range(self._rows):
            for i in range(self._columns - self._cell_number + 1):
                vals = []
                for j in range(self._cell_number):
                    vals.append(self._data[row][i+j])
                if vals == [player] * self._cell_number:
                    return True

        #check columns
        for column in range(self._columns):
            for i in range(self._rows - self._cell_number + 1):
                vals = []
                for j in range(self._cell_number):
                    vals.append(self._data[i+j][column])
                if vals == [player] * self._cell_number:
                    return True

        #check diagonals
        for row in range(self._rows-self._cell_number+1):
            for column in range(self._columns-self._cell_number+1):
                up=[]
                down=[]
                for i in range(self._cell_number):
                    up.append(self._data[row+i][column+i])
                    down.append(self._data[self._rows-row-i-1][column+i])
                if up==[player] * self._cell_number or down == [player] * self._cell_number:
                    return True

    def no_winning(self):
        for row in range(self._rows):
            for column in range(self._columns):
                if self._data[row][column]==0:
                    return False
        return True


    def __str__(self):
        table = Texttable()
        table.add_rows([list(range(1, self._columns+1))])
        for i in range(self._rows):
            table.add_row(list(map(lambda x: '' if x==0 else x, self._data[i].copy())))
        return table.draw()

            
