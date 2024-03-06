import unittest
import math

from services.ai import AI
from services.board import Board

VERY_LARGE_NUMBER = math.inf
VERY_SMALL_NUMBER = -math.inf

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

    def test_move_sorting_all_full(self):
        test_board.clear_board()

        test_board.board = [
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2]]

        moves = self.ai.get_possible_moves()

        self.assertEqual(moves, [])

    def test_cache_entries(self):
        test_board.clear_board()
        test_board.make_move(3, 1)

        ai_player = turn = 2
        depth = 2
        cache = {}
        alpha = VERY_SMALL_NUMBER
        beta = VERY_LARGE_NUMBER
        prev_move = 3
        move_count = 1

        self.ai.minimax(depth, turn, alpha, beta, prev_move,
                        move_count, ai_player, cache)

        state = test_board.board.copy()
        state[4][3] = 2
        state = tuple(map(tuple, state))
        key = (state, turn, depth)

        check = False
        for key in cache:
            if key[0] == state:
                check = True
        # because in this case, the AI should make move 3, meaning it will evaluate it as part of the minimax and store evaluation in cache

        self.assertEqual(check, True)

    def test_draw(self):
        test_board.clear_board()

        test_board.board = [
            [0, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2]]

        score, move = self.ai.minimax(
            4, 1, VERY_SMALL_NUMBER, VERY_LARGE_NUMBER, 1, 41, 1, {})

        self.assertEqual(score, 0)
        self.assertEqual(move, 0)

    def test_multiple_wins(self):
        test_board.clear_board()

        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 2, 0, 2],
            [2, 2, 1, 2, 1, 1, 1],
            [1, 2, 1, 1, 2, 1, 1],
            [2, 1, 1, 1, 2, 1, 2]]

        wins = [2, 5]

        score, move = self.ai.minimax(
            4, 1, VERY_SMALL_NUMBER, VERY_LARGE_NUMBER, 1, 27, 1, {})
        found_move = move in wins

        self.assertEqual(score > 10000, True)
        self.assertEqual(found_move, True)
