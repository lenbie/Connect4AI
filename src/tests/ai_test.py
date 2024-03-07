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
        """Tests whether the AI can find the correct first move (column 3).
        """
        test_board.clear_board()

        player = 1
        expected_move = 3
        move_count = 0
        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_win_next_move_player2(self):
        """Tests if the AI can find its own win on the next move,
        if it is player 2
        """
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
        """Tests if the AI can find its own win on the next move,
        if it is player 1
        """
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
        """Tests if move sorting works correctly if all columns not full.
        """
        test_board.clear_board()
        moves = self.ai.get_possible_moves()

        self.assertEqual(moves, [3, 2, 4, 1, 5, 0, 6])

    def test_move_sorting_full_col_3(self):
        """Tests if move sorting works correctly if column 3 is full.
        """
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
        """Tests if move sorting works correctly if column 5 is full.
        """
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
        """Tests if move sorting works correctly if all columns are full.
        """
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
        """Tests whether a necessary entry is present in the cache.
        """
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
        # because in this case, the AI should make move 3, meaning it will evaluate it
        # as part of the minimax and store evaluation in cache

        self.assertEqual(check, True)

    def test_minimax_draw(self):
        """Tests whether the minimax returns the correct score and move if 
        the next move inevitably results in a draw.
        """
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

    def test_minimax_multiple_wins(self):
        """Tests whether the minimax returns the score of a win, 
        and one of the winning moves, if there are multiple winning opportunities
        on the next move. This simultaneously tests if winning on the next move
        functions correctly.
        """
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


# minimax losses, wins further away?
# more extensive cache testing? 
# alpha beta pruning tests
    
    def test_evaluate_window_favourable(self):
        """Tests whether a favourable window to the current
            turn's player is correctly evaluated.
        """
        window = [0, 1, 1, 1]
        turn = 1

        score = self.ai._evaluate_window(window, turn)

        self.assertEqual(score, 100)
    
    def test_evaluate_window_unfavourable(self):
        """Tests whether an unfavourable window to the current
            turn's player is correctly evaluated.
        """
        window = [1, 1, 1, 0]
        turn = 2

        score = self.ai._evaluate_window(window, turn)

        self.assertEqual(score, -100)
    
    def test_evaluate_window_all_zeroes(self):
        """Tests whether a window with all zeroes
            is correctly evaluated.
        """
        window = [0, 0, 0, 0]
        turn = 2

        score = self.ai._evaluate_window(window, turn)

        self.assertEqual(score, 0)

    def test_evaluate_board_horizontal(self):
        """Tests whether horizontal windows are correctly evaluated.
        There are no vertical or diagonal scores other than 0 on the board.
        """
        test_board.clear_board()

        ai_player = 1
        turn = 1

        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 2, 2, 2]]

        #We have three 1's and three 2's in the bottom row, score 100 - 100
        #Also, two 1's in the row above, each with one opening on the side, score 10 + 10
        # AI player == turn, so score is positive.

        expected_score = 20

        score = self.ai.evaluate_board(ai_player, turn)
        self.assertEqual(score, expected_score)

    def test_evaluate_board_vertical(self):
        """Tests whether vertical scores are correctly evaluated.
        There are no horizontal or diagonal scores other than 0 on the board.
        """
        test_board.clear_board()

        ai_player = 1
        turn = 2

        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 1, 0, 0],
            [1, 2, 0, 0, 1, 0, 0],
            [1, 2, 0, 2, 1, 2, 0]]

        expected_score = 0

        score = self.ai.evaluate_board(ai_player, turn)
        self.assertEqual(score, expected_score)
    
    def test_evaluate_board_right_downward_diagonal(self):
        """Tests whether right downward diagonal scores are correctly evaluated.
        There are no horizontal, vertical or left downward scores other than 0 on the board.
        """
        test_board.clear_board()

        ai_player = 1
        turn = 1

        #This cannot be tested with a real game situation, so this board would never occur.
        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 2, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0]]

        expected_score = 90

        score = self.ai.evaluate_board(ai_player, turn)
        self.assertEqual(score, expected_score)

    def test_evaluate_board_left_upward_diagonal(self):
        #Tests whether left upward diagonal scores are correctly evaluated.
        #There are no horizontal, vertical or left downward scores other than 0 on the board.
        
        test_board.clear_board()

        ai_player = 1
        turn = 1

        #This cannot be tested with a real game situation, so this board would never occur.
        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0],
            [0, 0, 2, 2, 1, 0, 0],
            [0, 0, 2, 0, 2, 1, 0]]

        expected_score = -40

        score = self.ai.evaluate_board(ai_player, turn)
        self.assertEqual(score, expected_score)


    def test_evaluate_empty_board(self):
        """Tests if the empty board is correctly evaluated
        """
        
        test_board.clear_board()

        ai_player = 1
        turn = 2

        #This cannot be tested with a real game situation, so this board would never occur.
        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        expected_score = 0

        score = self.ai.evaluate_board(ai_player, turn)
        self.assertEqual(score, expected_score)



       

       