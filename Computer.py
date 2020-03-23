from random import choice

class Computer:

    '''
    -function that makes a list of all the available free columns and picks one randomly
    '''
    def make_random_move(self, board):
        free_columns = []
        for column in range(board.Columns):
            if board.available_column(column):
                free_columns.append(column)
        return choice(free_columns)
    '''
    -function that receives a board and returns a column in such a way that 
    the computer either wins in a single move, or blocks the user from winning;
    if none of them is possible, it will make a random move
    '''
    def make_move_to_win(self,board):
        #win in a single move
        for column in range(board.Columns):
            if board.available_column(column):
                row = board.last_free_row(column)
                board.place_value(row, column , 2)
                if board.check_if_player_won(2):
                    board.place_value(row, column,0)
                    return column
                else:
                    board.place_value(row, column,0)

        #try to block the user from winning
        for column in range(board.Columns):
            if board.available_column(column):
                row = board.last_free_row(column)
                board.place_value(row, column, 1)
                if board.check_if_player_won(1):
                    board.place_value(row, column,0)
                    return column
                else:
                    board.place_value(row, column,0)

        #if the computer cannot win in a single move or cannot block the user it will make a random move
        return self.make_random_move(board)


