import unittest

from ai import AI
from board import Board

test_board = Board()


class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI(test_board)
        test_board.clear_board()

    def test_next_move_empty_board(self):
        test_board.clear_board()

        player = 1
        expected_move = 3
        move_count = 0
        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_win_next_move_player2(self):
        test_board.clear_board()
        test_board.make_move(0, 1)
        test_board.make_move(1, 2)
        test_board.make_move(5, 1)
        test_board.make_move(2, 2)
        test_board.make_move(5, 1)
        test_board.make_move(3, 2)
        test_board.make_move(0, 1)

        player = 2
        move_count = 7
        expected_move = 4

        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_win_next_move_player1(self):
        test_board.clear_board()
        test_board.make_move(3, 1)
        test_board.make_move(5, 2)
        test_board.make_move(1, 1)
        test_board.make_move(6, 2)
        test_board.make_move(2, 1)
        test_board.make_move(4, 2)

        player = 1
        move_count = 7
        expected_move = 0

        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_move_sorting_all_possible(self):
        test_board.clear_board()
        moves = self.ai.get_possible_moves()

        self.assertEqual(moves, [3, 2, 4, 1, 5, 0, 6])

    def test_move_sorting_full_col_3(self):
        test_board.clear_board()
        test_board.make_move(3, 1)
        test_board.make_move(3, 2)
        test_board.make_move(3, 1)
        test_board.make_move(3, 2)
        test_board.make_move(3, 1)
        test_board.make_move(3, 1)

        moves = self.ai.get_possible_moves()

        self.assertEqual(moves, [2, 4, 1, 5, 0, 6])

    def test_move_sorting_full_col_5(self):
        test_board.clear_board()
        test_board.make_move(5, 1)
        test_board.make_move(5, 2)
        test_board.make_move(5, 1)
        test_board.make_move(5, 2)
        test_board.make_move(5, 1)
        test_board.make_move(5, 1)

        moves = self.ai.get_possible_moves()

        self.assertEqual(moves, [3, 2, 4, 1, 0, 6])
