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

        move = self.ai.next_move(player)

        self.assertEqual(move, expected_move)

    def test_win_next_move_player2(self):
        test_board.make_move(0, 1)
        test_board.make_move(1, 2)
        test_board.make_move(5, 1)
        test_board.make_move(2, 2)
        test_board.make_move(5, 1)
        test_board.make_move(3, 2)
        test_board.make_move(0, 1)
        
        player = 2
        expected_move = 4

        move = self.ai.next_move(player)

        self.assertEqual(move, expected_move)
    
    def test_win_next_move_player1(self):
        test_board.make_move(3, 1)
        test_board.make_move(5, 2)
        test_board.make_move(1, 1)
        test_board.make_move(6, 2)
        test_board.make_move(2, 1)
        test_board.make_move(4, 2)

        player = 1
        expected_move = 0

        move = self.ai.next_move(player)

        self.assertEqual(move, expected_move)