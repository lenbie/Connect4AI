import math
import time
from services.board import Board

VERY_LARGE_NUMBER = math.inf
VERY_SMALL_NUMBER = -math.inf


class AI:
    def __init__(self, board: Board):
        """Class constructor

        Args:
            board (Board): The game board
        """
        self.board = board

    def next_move(self, ai_player, move_count):
        """Finds the next move to make, aiming to find the best possible one.

        Args:
            ai_player (int): Which player (1 or 2) the AI is playing
            move_count (int): Moves in the game so far

        Returns:
            best_move (int): The column into which the AI makes its next move.
        """

        max_score = VERY_SMALL_NUMBER  # alpha
        min_score = VERY_LARGE_NUMBER  # beta

        best_move = 3
        max_depth = 7

        move_time = 3

        cache = {}

        #Iterative deepening
        start_time = time.time()

        for depth in range(1, max_depth + 1):

            max_score = VERY_SMALL_NUMBER  # alpha
            min_score = VERY_LARGE_NUMBER  # beta

            moves = self.get_possible_moves()
            if best_move in moves:
                moves.remove(best_move)
                moves.insert(0, best_move)

            for move in moves:
                # Time Limit exceeded, return best_move immediately
                if time.time() - start_time >= move_time:
                    print("Time Exceeded")
                    return best_move

                self.board.make_move(move, ai_player)
                move_count += 1

                #Change turn, since AI player just made a move
                turn = 2 if ai_player == 1 else 1

                minimax = self.minimax(
                    depth, turn, max_score, min_score, move, move_count, ai_player, cache)
                score = minimax[0]

                if score > max_score:
                    max_score = score
                    best_move = move

                self.board.undo_move(move)
                move_count -= 1

        return best_move

    def minimax(self, depth: int, turn: int, alpha, beta, prev_move, move_count, ai_player, cache):
        """Recursive minimax algorithm function, with alpha beta pruning.

        Args:
            depth (int): The depth to which the minimax algorithm searches game states
            turn (int): 1 or 2, depending on whose turn it is.
                        If ai_play == turn, it is the maximising (AI) player's turn
            alpha, beta (float): Alpha -beta pruning values
            prev_move (int): The previous move made
            move_count (int): The number of moves made in the game so far
            ai_player (int): Whether the AI is playing player 1 or 2 in this game
            cache (dict): Cache for storing board states and the associated best move per player

        Returns:
            value, best_move : The best move (int representing a column)
                                and game state value belonging to that move
        """

        #Create cache key for the current board state
        state = tuple(map(tuple, self.board.board))
        cache_key = (state, turn)


        #Check whether the previous player's turn led to a win and score accordingly
        if self.board.check_four_connected():
            if turn != ai_player:
                return 1000000 + depth, prev_move
            return -1000000 - depth, prev_move

        #Check whether there is a draw
        if move_count == 42:
            return 0, prev_move

        #Check if depth has reached 0, if yes, return board state evaluation for the current player
        if depth == 0:
            score = self.evaluate_board(ai_player, turn)
            return score, prev_move
        
        #If current board state in cache, put best move to the front of moves list
        moves = self.get_possible_moves()
        if cache_key in cache:
            moves.remove(cache[cache_key][1])
            moves.insert(0, cache[cache_key][1])

        #Maximising player turn
        if turn == ai_player:
            max_value = VERY_SMALL_NUMBER
            for move in moves:
                self.board.make_move(move, turn)
                move_count += 1

                value, _ = self.minimax(
                    depth-1, 3-turn, alpha, beta, move, move_count, ai_player, cache)
                # Since turn is either 1 or 2, 3 - turn gives the other player number

                self.board.undo_move(move)
                move_count -= 1

                if value > max_value:
                    max_value = value
                    best_move = move
                    cache[cache_key] = max_value, best_move

                if value >= beta:
                    break
                alpha = max(alpha, value)

            return max_value, best_move

        #Minimizing player turn
        min_value = VERY_LARGE_NUMBER
        for move in moves:
            self.board.make_move(move, turn)
            move_count += 1

            value, _ = self.minimax(
                depth-1, 3-turn, alpha, beta, move, move_count, ai_player, cache)

            self.board.undo_move(move)
            move_count -= 1

            if value < min_value:
                min_value = value
                best_move = move
                cache[cache_key] = min_value, best_move

            if value <= alpha:
                break
            beta = min(beta, value)

        return min_value, best_move

    def get_possible_moves(self):
        """Finds all columns into which valid moves can be made at
        the current point in the game. Orders these moves according
        to a predefined ideal order.

        Returns:
            sorted_moves: A set of possible columns, ordered according to the ideal move order.
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

    def _evaluate_window(self, window, turn):
        """Part of the heuristic evaluation of the board state
        Assigns points depending on how many pieces each player has
        in the window of four squares. No point assignments happen
        for four in a row, as this should be recognized and evaluated directly
        by the minimax.

        Args:
            window (list): A four-square section of the game board (horizontal, vertical or diagonal)
            turn (int): The player whose turn it is

        Returns:
            score (int): The score assigned for the window.
        """

        score = 0

        #Giving points for favourable positions of the current player
        if window.count(turn) == 3 and window.count(0) == 1:
            score += 100
        if window.count(turn) == 2 and window.count(0) == 2:
            score += 10

        #Subtracting points for favourable positions of the opponent
        if window.count(3 - turn) == 3 and window.count(0) == 1:
            score -= 100
        if window.count(3 - turn) == 2 and window.count(0) == 2:
            score -= 10

        return score

    def evaluate_board(self, ai_player, turn):
        """Main heuristic evaluation function. Splits the game board into window sections 
        to be evaluated by the _evaluate_window function.
        
        Args:
            ai_player (int): The player number of the ai_player in the current game
            turn (int): The player whose turn it currently is

        Returns:
            score (int): The overall heuristic score of the position for the maximizing player.
        """
        score = 0
        #Checking windows in rows
        for row in range(6):
            for col in range(4):
                window = [self.board.board[row][col], self.board.board[row][col + 1],
                          self.board.board[row][col + 2], self.board.board[row][col + 3]]
                score += self._evaluate_window(window, turn)

        #Checking column windows
        for row in range(3):
            for col in range(7):
                window = [self.board.board[row][col], self.board.board[row + 1][col],
                          self.board.board[row + 2][col], self.board.board[row + 3][col]]
                score += self._evaluate_window(window, turn)

        #Checkinf right downward diagonals
        for row in range(3):
            for col in range(4):
                window = [self.board.board[row][col], self.board.board[row + 1][col + 1],
                          self.board.board[row + 2][col + 2], self.board.board[row + 3][col + 3]]
                score += self._evaluate_window(window, turn)

        #Checking left downward diagonals
        for row in range(3):
            for col in range(3, 7):
                window = [self.board.board[row][col], self.board.board[row + 1][col - 1],
                          self.board.board[row + 2][col - 2], self.board.board[row + 3][col - 3]]
                score += self._evaluate_window(window, turn)

        #Return score depending on whether it is the maximising or minimizing player's turn.
        if ai_player == turn:
            return score
        return -score
