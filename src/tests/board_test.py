import unittest

from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()
        self.test_board.clear_board()

    def test_move_correct_square(self):
        player = 1
        column_index = 3

        self.test_board.make_move(column_index, player)

        square_content = self.test_board.check_square(5, column_index)

        self.assertEqual(square_content, 1)

    def test_move_overall_board(self):
        self.test_board.clear_board()

        player = 1
        column_index = 3

        correct_board = [[0 for i in range(7)] for j in range(6)]
        correct_board[5][3] = 1

        self.test_board.make_move(column_index, player)

        board = self.test_board._board

        self.assertEqual(board, correct_board)

