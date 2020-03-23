import unittest
from Board import Board
from Computer import Computer
from Game import Game
from exceptions import *

class Test_Board(unittest.TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        self.computer = Computer()
        self.game  = Game(self.board,self.computer)

    def test_init_board(self):
        self.board._init_board()
        for i in range(len(self.board._data)):
            self.assertEqual(self.board._data[i], [0]*7)


    def test_last_free_row(self):
        self.board._init_board()
        self.board.place_value(5,1,1)
        self.board.place_value(4,1,1)
        self.assertEqual(self.board.last_free_row(1),3)
        with self.assertRaises(InvalidColumnException):
            self.board.last_free_row(-1)
        

    def test_make_move(self):
        self.board._init_board()
        self.board.place_value(5,0,1)
        self.board.make_move(1,1)
        self.board.make_move(2,1)
        with self.assertRaises(GameWonException):
            self.board.make_move(3,1)

    def test_place_value(self):
        self.board._init_board()
        self.board.place_value(1,1,2)
        self.assertEqual(self.board._data[1][1],2)
        self.assertEqual(self.board._data[1][2],0)

    def test_check_if_player_won(self):
        self.board._init_board()
        #on a column
        self.board.place_value(5,0,1)
        self.board.place_value(4,0,1)
        self.board.place_value(3,0,1)
        self.board.place_value(2,0,1)
        self.assertEqual(self.board.check_if_player_won(1),True)
        self.board._init_board()
        self.board.place_value(5,1,1)
        self.assertEqual(self.board.check_if_player_won(1),None)
        #on a row
        self.board.place_value(5,2,1)
        self.board.place_value(5,3,1)
        self.board.place_value(5,4,1)
        self.assertEqual(self.board.check_if_player_won(1),True)
        self.board._init_board()
        #on diagonals
        self.board.place_value(5,0,1)
        self.board.place_value(4,1,1)
        self.board.place_value(3,2,1)
        self.board.place_value(2,3,1)
        self.assertEqual(self.board.check_if_player_won(1),True)
        self.board.place_value(0,0,1)
        self.board.place_value(1,1,1)
        self.board.place_value(2,2,1)
        self.board.place_value(3,3,1)
        self.assertEqual(self.board.check_if_player_won(1),True)

class Test_Game(unittest.TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        self.computer = Computer()
        self.game  = Game(self.board,self.computer)

    def test_make_player_move(self):
        self.board._init_board()
        self.game.make_player_move(3)
        self.assertEqual(self.board._data[5][3],1)
        self.assertEqual(self.game._current_player,2)


    def test_make_computer_move(self):
        self.game.make_computer_move()
        self.assertEqual(self.game._current_player,1)

class Test_Computer(unittest.TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        self.computer = Computer()
        self.game  = Game(self.board,self.computer)

    def test_make_move_to_win(self):
        self.board._init_board()
        self.board.place_value(5,0,2)
        self.board.place_value(5,1,2)
        self.board.place_value(5,2,2)
        self.assertEqual(self.computer.make_move_to_win(self.board),3)
        self.board._init_board()
        self.board.place_value(5,0,1)
        self.board.place_value(5,1,1)
        self.board.place_value(5,2,1)
        self.assertEqual(self.computer.make_move_to_win(self.board),3)

        
    



unittest.main()

