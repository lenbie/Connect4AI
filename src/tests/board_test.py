import unittest

from services.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.testboard = Board()
        self.testboard.clear_board()

    def test_move_correct_square(self):
        player = 1
        column_index = 3

        self.testboard.make_move(column_index, player)

        square_content = self.testboard.check_square(5, column_index)

        self.assertEqual(square_content, 1)

    def test_move_overallboard(self):
        self.testboard.clear_board()

        player = 1
        column_index = 3

        correctboard = [[0 for i in range(7)] for j in range(6)]
        correctboard[5][3] = 1

        self.testboard.make_move(column_index, player)

        board = self.testboard.board

        self.assertEqual(board, correctboard)

    def test_valid_move(self):
        self.testboard.clear_board()

        self.testboard.board[5][3] = 1
        self.testboard.board[4][3] = 1
        self.testboard.board[3][3] = 1
        self.testboard.board[2][3] = 2
        self.testboard.board[1][3] = 2
        self.testboard.board[0][3] = 2

        invalid_move = self.testboard.check_valid_move(3)

        self.assertEqual(invalid_move, False)

    def test_check_row_win(self):
        self.testboard.clear_board()

        self.testboard.make_move(2, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(4, 1)
        self.testboard.make_move(5, 1)

        win = self.testboard._check_row(5, 2)

        self.assertEqual(win, True)

    def test_check_row_no_win(self):
        self.testboard.clear_board()

        self.testboard.make_move(2, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(4, 2)
        self.testboard.make_move(5, 2)
        win = self.testboard._check_row(5, 2)

        self.assertEqual(win, False)

    def test_check_column_win(self):
        self.testboard.clear_board()

        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 1)
        win = self.testboard._check_all_cols()

        self.assertEqual(win, 1)

    def test_check_column_no_win(self):
        self.testboard.clear_board()

        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 2)
        win = self.testboard._check_col(2, 2)
        self.assertEqual(win, False)

    def test_check_right_up_diagonal(self):
        self.testboard.clear_board()

        self.testboard.make_move(1, 1)
        self.testboard.make_move(2, 2)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(1, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(3, 2)
        self.testboard.make_move(0, 1)
        self.testboard.make_move(3, 1)

        win = self.testboard._check_diag_whole_board()
        self.assertEqual(win, 1)

    def test_check_right_down_diagonal(self):
        self.testboard.clear_board()

        self.testboard.make_move(1, 1)
        self.testboard.make_move(2, 2)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(1, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(1, 2)
        self.testboard.make_move(1, 1)
        self.testboard.make_move(4, 1)

        win = self.testboard._check_right_down_diagonals(2, 1)
        self.assertEqual(win, True)
