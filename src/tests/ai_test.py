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

    def test_next_move_first_two_moves_both_players(self):
        """ Tests whether the AI playing as both players follows
         the ideal first two moves, which is placing in the centre column (3).
        """
        test_board.clear_board()

        move_count = 0
        moves = set()

        for i in range(5):
            player = 1
            if i % 2 == 0:
                player = 2
            move_count += 1
            move = self.ai.next_move(player, move_count)
            moves.add(move)

        expected_moves = False
        if len(moves) == 1 and 3 in moves:
            expected_moves = True

        self.assertEqual(expected_moves, True)

    def test_next_move_win_player2(self):
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

    def test_next_move_loss_player1(self):
        """Tests if the AI can prevent its own loss on the next move,
        if it is player 1
        """
        test_board.clear_board()
        test_board.make_move(0, 1)
        test_board.make_move(1, 2)
        test_board.make_move(5, 1)
        test_board.make_move(2, 2)
        test_board.make_move(5, 1)
        test_board.make_move(3, 2)
        test_board.make_move(0, 1)

        player = 1
        move_count = 7
        expected_move = 4

        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_next_move_win_player1(self):
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

    def test_next_move_loss_player2(self):
        """Tests if the AI can prevent its own loss on the next move,
        if it is player 2
        """
        test_board.clear_board()
        test_board.make_move(3, 1)
        test_board.make_move(5, 2)
        test_board.make_move(1, 1)
        test_board.make_move(6, 2)
        test_board.make_move(2, 1)
        test_board.make_move(4, 2)

        player = 2
        move_count = 7
        expected_move = 0

        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_next_move_win_end_game(self):
        """Tests whether the AI can find the win if the board is quite full.
        """
        test_board.clear_board()

        test_board.board = [
            [2, 1, 2, 2, 2, 0, 2],
            [1, 2, 1, 1, 1, 0, 1],
            [2, 2, 1, 2, 2, 2, 1],
            [1, 1, 2, 1, 1, 1, 2],
            [2, 2, 1, 2, 2, 2, 1],
            [1, 1, 2, 1, 1, 1, 2]]

        player = 1
        move_count = 40
        expected_move = 5

        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_next_move_loss_end_game(self):
        """Tests whether the AI can prevent losing if the board is quite full.
        """
        test_board.clear_board()

        test_board.board = [
            [2, 1, 2, 2, 2, 0, 2],
            [1, 2, 1, 1, 1, 0, 1],
            [2, 2, 1, 2, 2, 2, 1],
            [1, 1, 2, 1, 1, 1, 2],
            [2, 2, 1, 2, 2, 2, 1],
            [1, 1, 2, 1, 1, 1, 2]]

        player = 2
        move_count = 40
        expected_move = 5

        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_next_move_win_mid_game(self):
        """Tests whether the AI finds a win on the next move mid-game.
        """

        test_board.clear_board()

        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0],
            [0, 1, 2, 1, 0, 0, 0],
            [0, 2, 1, 2, 2, 0, 0],
            [1, 1, 2, 1, 1, 0, 2]]

        player = 1
        move_count = 17
        expected_move = 0

        move = self.ai.next_move(player, move_count)

        self.assertEqual(move, expected_move)

    def test_next_move_loss_mid_game(self):
        """Tests whether the AI prevents its own loss on the next move mid-game.
        """

        test_board.clear_board()

        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0],
            [0, 1, 2, 1, 0, 0, 0],
            [0, 2, 1, 2, 2, 0, 0],
            [1, 1, 2, 1, 1, 0, 2]]

        player = 2
        move_count = 17
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

    def test_minimax_cache_entries(self):
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
        key = (state, turn)

        check = False
        for key in cache:
            if key[0] == state:
                check = True
        # because in this case, the AI should make move 3, meaning it will evaluate it
        # as part of the minimax and store evaluation in cache

        self.assertEqual(check, True)

    def test_next_move_minimax_caching_depth_one(self):
        """Tests whether the correct entries are put into the cache at depth 1
        if the AI player starts, by simulating next_move at depth 1. 
        For that purpose, copied code from next_move except for the time limitation
        and increasing depths, as this is not necessary at only depth 1.
        Testing at much higher depth is infeasible as cache grows larger.
        """
        test_board.clear_board()

        # Create list of board states that should be in cache
        board_states = []
        state = test_board.board.copy()
        for col in range(7):
            state[5][col] = 1
            board = tuple(map(tuple, state))
            key = (board, 2)
            board_states.append(board)
            state[5][col] = 0

        ai_player = 1
        depth = 1
        move_count = 0

        max_score = VERY_SMALL_NUMBER  # alpha
        min_score = VERY_LARGE_NUMBER  # beta

        best_move = 3

        cache = {}

        # all moves available since no prior moves
        moves = [3, 2, 4, 1, 5, 0, 6]

        for move in moves:

            test_board.make_move(move, ai_player)
            move_count += 1

            turn = 2 if ai_player == 1 else 1

            minimax = self.ai.minimax(
                depth, turn, max_score, min_score, move, move_count, ai_player, cache)
            score = minimax[0]

            if score > max_score:
                max_score = score
                best_move = move

            test_board.undo_move(move)
            move_count -= 1

        check = True
        for key in cache:
            if key[0] not in board_states:
                check = False

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

    def test_minimax_loss(self):
        """Tests whether the minimax returns the score of a loss, 
        and the move to prevent losing on the next move.
        """
        test_board.clear_board()

        test_board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 2, 0, 2],
            [2, 2, 1, 2, 1, 0, 1],
            [1, 2, 1, 1, 2, 1, 1],
            [2, 1, 1, 1, 2, 1, 2]]

        loss_prevention = 2

        turn = 1
        ai_player = 2

        score, move = self.ai.minimax(
            5, turn, VERY_SMALL_NUMBER, VERY_LARGE_NUMBER, 3, 26, ai_player, {})

        self.assertEqual(score < -10000, True)
        self.assertEqual(loss_prevention, move)

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

        # We have three 1's and three 2's in the bottom row, score 100 - 100
        # Also, two 1's in the row above, each with one opening on the side, score 10 + 10
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

        # This cannot be tested with a real game situation, so this board would never occur.
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
        # Tests whether left upward diagonal scores are correctly evaluated.
        # There are no horizontal, vertical or left downward scores other than 0 on the board.

        test_board.clear_board()

        ai_player = 1
        turn = 1

        # This cannot be tested with a real game situation, so this board would never occur.
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

        # This cannot be tested with a real game situation, so this board would never occur.
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
