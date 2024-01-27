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

    def test_valid_move(self):
        self.test_board.clear_board()

        self.test_board._board[5][3] = 1
        self.test_board._board[4][3] = 1
        self.test_board._board[3][3] = 1
        self.test_board._board[2][3] = 2
        self.test_board._board[1][3] = 2
        self.test_board._board[0][3] = 2

        invalid_move = self.test_board._check_valid_move(3)

        self.assertEqual(invalid_move, False)

    def test_check_row_win(self):
        self.test_board.clear_board()

        self.test_board.make_move(2, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(4, 1)
        win = self.test_board._check_row(5, 5, 1)

        self.assertEqual(win, True)

    def test_check_row_no_win(self):
        self.test_board.clear_board()

        self.test_board.make_move(2, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(4, 2)
        win = self.test_board._check_row(5, 5, 1)

        self.assertEqual(win, False)

    def test_check_column_win(self):
        self.test_board.clear_board()

        self.test_board.make_move(2, 1)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(2, 1)
        win = self.test_board._check_column(2, 2, 1)

        self.assertEqual(win, True)

    def test_check_column_no_win(self):
        self.test_board.clear_board()

        self.test_board.make_move(2, 1)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(2, 2)
        win = self.test_board._check_column(2, 2, 1)

        self.assertEqual(win, False)

    def test_check_left_lower_diagonal(self):
        self.test_board.clear_board()

        self.test_board.make_move(1, 1)
        self.test_board.make_move(2, 2)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(1, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(3, 2)
        self.test_board.make_move(0, 1)

        win = self.test_board._check_diagonals(2, 3, 1)
        self.assertEqual(win, True)

    def test_check_right_upper_diagonal(self):
        self.test_board.clear_board()

        self.test_board.make_move(1, 1)
        self.test_board.make_move(2, 2)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(1, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(3, 2)
        self.test_board.make_move(3, 1)

        win = self.test_board._check_diagonals(5, 0, 1)
        self.assertEqual(win, True)

    def test_check_left_upper_diagonal(self):
        self.test_board.clear_board()

        self.test_board.make_move(1, 1)
        self.test_board.make_move(2, 2)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(1, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(1, 2)
        self.test_board.make_move(1, 1)

        win = self.test_board._check_diagonals(5, 4, 1)
        self.assertEqual(win, True)

    def test_check_right_lower_diagonal(self):
        self.test_board.clear_board()

        self.test_board.make_move(1, 1)
        self.test_board.make_move(2, 2)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(2, 1)
        self.test_board.make_move(1, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(3, 1)
        self.test_board.make_move(1, 2)
        self.test_board.make_move(4, 1)

        win = self.test_board._check_diagonals(2, 1, 1)
        self.assertEqual(win, True)
