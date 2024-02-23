import math
from board import Board

VERY_LARGE_NUMBER = math.inf
VERY_SMALL_NUMBER = -math.inf


class AI:
    def __init__(self, board: Board):
        """Class constructor

        Args:
            board (Board): The game board
        """
        self.board = board
        self._current_player = 2  # AI plays second by default

    def next_move(self, player, move_count):
        """Finds the next move to make, aiming to find the best possible one.

        Args:
            player (int): Which player (1 or 2) the AI is playing
            move_count (int): Moves in the game so far

        Returns:
            best_move (int): The column into which the AI makes its next move.
        """
        self._current_player = player

        max_score = alpha = VERY_SMALL_NUMBER
        min_score = beta = VERY_LARGE_NUMBER

        best_move = 0
        depth = 4

        for move in self.get_possible_moves():

            self.board.make_move(move, self._current_player)
            move_count +=1

            player_one = bool(self._current_player == 1)

            minimax = self.minimax(depth, not player_one, alpha, beta, move, move_count)
            score = minimax[0]

            print(score)
            if score >= max_score:
                max_score = score
                best_move = minimax[1]
                alpha = score

            self.board.undo_move(move)
            move_count-=1

        return best_move

    def minimax(self, depth: int, player_one: bool, alpha, beta, prev_move, move_count):
        """Recursive minimax algorithm function, with alpha beta pruning.

        Args:
            depth (int): The depth to which the minimax algorithm searches game states
            player_one (bool): True if the AI is player 1, False if player 2
            alpha, beta (float): Alpha -beta pruning values
            prev_move (int): The previous move made
            move_count (int): The number of moves made in the game so far


        Returns:
            value, best_move : The best move (int representing a column) and game state value belonging to that move
        """
        if player_one:
            current_player = 1
        else:
            current_player = 2

        if self.board.check_four_connected():#current_player):  # win
            if not player_one:
                return 1000000 + depth, prev_move
            return -1000000 - depth, prev_move

        if move_count == 42:  # draw
            return 0, prev_move

        if depth == 0:
            score = self.evaluate_board()
            return score, prev_move

        if player_one:
            max_value = VERY_SMALL_NUMBER
            for move in self.get_possible_moves():
                self.board.make_move(move, current_player)
                move_count +=1

                value, _ = self.minimax(depth-1, False, alpha, beta, move, move_count)

                self.board.undo_move(move)
                move_count -=1

                if value > max_value:
                    max_value = value
                    best_move = move

                if value >= beta:
                    break
                alpha = max(alpha, value)

            return max_value, best_move

        min_value = VERY_LARGE_NUMBER
        for move in self.get_possible_moves():
            self.board.make_move(move, current_player)
            move_count +=1

            value, _ = self.minimax(depth-1, True, alpha, beta, move, move_count)

            self.board.undo_move(move)
            move_count -=1

            if value < min_value:
                min_value = value
                best_move = move

            if value <= alpha:
                break
            beta = min(beta, value)

        return min_value, best_move

    def get_possible_moves(self):
        """Finds all columns into which valid moves can be made at
        the current point in the game.

        Returns:
            moves: A set of possible columns
        """
        moves = []
        ideal_move_order = [3, 2, 4, 1, 5, 0, 6]

        for column in range(0, 7):
            valid = self.board.check_valid_move(column)
            if valid:
                moves.append(column)

        sorted_moves = sorted(moves, key=lambda x: ideal_move_order.index(
            x) if x in ideal_move_order else len(ideal_move_order))

        return sorted_moves

    def _evaluate_window(self, window):
        """Part of the heuristic evaluation of the board state for the current player.
        Assigns points depending on how many pieces the player (and opponent) has
        in the vicinity of four squares.

        Args:
            window: A section of the game board (horizontal, vertical or diagonal)
            player (int): current player

        Returns:
            score (int): The points assigned to the current player for that window.
        """

        score = 0
        if window.count(1) == 4:
            score += 10000
        if window.count(1) == 3 and window.count(0) == 1:
            score += 100
        if window.count(1) == 2 and window.count(0) == 2:
            score += 10

        if window.count(2) == 4:
            score -= 10000
        if window.count(2) == 3 and window.count(0) == 1:
            score -= 100
        if window.count(2) == 2 and window.count(0) == 2:
            score -= 10

        return score

    def evaluate_board(self):
        """Main heuristic evaluation function. Splits the game board into window sections 
        to be evaluated by the _evaluate_window function.

        Returns:
            score (int): The overall heuristic score of the position for the current player.
        """
        score = 0
        # Check horizontal
        for row in range(6):
            for col in range(4):
                window = [self.board.board[row][col], self.board.board[row][col + 1],
                          self.board.board[row][col + 2], self.board.board[row][col + 3]]
                score += self._evaluate_window(window)

        # Check vertical
        for row in range(3):
            for col in range(7):
                window = [self.board.board[row][col], self.board.board[row + 1][col],
                          self.board.board[row + 2][col], self.board.board[row + 3][col]]
                score += self._evaluate_window(window)

        # Check right downward diagonals
        for row in range(3):
            for col in range(4):
                window = [self.board.board[row][col], self.board.board[row + 1][col + 1],
                          self.board.board[row + 2][col + 2], self.board.board[row + 3][col + 3]]
                score += self._evaluate_window(window)

        # Check left upward diagonals
        for row in range(3):
            for col in range(3, 7):
                window = [self.board.board[row][col], self.board.board[row + 1][col - 1],
                          self.board.board[row + 2][col - 2], self.board.board[row + 3][col - 3]]
                score += self._evaluate_window(window)

        return score
