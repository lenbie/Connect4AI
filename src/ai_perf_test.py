import math
import time
from services.board import Board

VERY_LARGE_NUMBER = math.inf
VERY_SMALL_NUMBER = -math.inf


class AICopy:
    def __init__(self, board: Board):
        """Class constructor

        Args:
            board (Board): The game board
        """
        self.board = board
    
    def next_move_caching(self, ai_player, move_count):


        max_score = VERY_SMALL_NUMBER  # alpha
        min_score = VERY_LARGE_NUMBER  # beta

        best_move = 3
        max_depth = 5

        move_time = 5

        cache = {}

        start_time = time.time()

        for depth in range(1, max_depth + 1):

            max_score = VERY_SMALL_NUMBER  # alpha
            min_score = VERY_LARGE_NUMBER  # beta

            moves = self.get_possible_moves()
            if best_move in moves:
                moves.remove(best_move)
                moves.insert(0, best_move)

            for move in moves:
                if time.time() - start_time >= move_time:  # Time limit exceeded
                    print("Time Exceeded")
                    return best_move

                self.board.make_move(move, ai_player)
                move_count += 1

                turn = 2 if ai_player == 1 else 1

                minimax = self.minimax_caching(
                    depth, turn, max_score, min_score, move, move_count, ai_player, cache)
                score = minimax[0]

                if score > max_score:
                    max_score = score
                    best_move = move

                self.board.undo_move(move)
                move_count -= 1

        return best_move

    def minimax_caching(self, depth: int, turn: int, alpha, beta, prev_move, move_count, ai_player, cache):

        state = tuple(map(tuple, self.board.board))
        cache_key = (state, turn) 

        if self.board.check_four_connected():  # win
            if turn != ai_player:
                return 1000000 + depth, prev_move
            return -1000000 - depth, prev_move

        if move_count == 42:  # draw
            return 0, prev_move

        if depth == 0:
            score = self.evaluate_board(ai_player)
            return score, prev_move

        moves = self.get_possible_moves()
        if cache_key in cache:
            moves.remove(cache[cache_key][1])
            moves.insert(0, cache[cache_key][1])

        #if depth in cached thing is >= we can return score immediately (maybe some alpha beta pruning optimization)
        
        if turn == ai_player:
            max_value = VERY_SMALL_NUMBER
            for move in moves:
                self.board.make_move(move, turn)
                move_count += 1

                value, _ = self.minimax_caching(
                    depth-1, 3-turn, alpha, beta, move, move_count, ai_player, cache)

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

        min_value = VERY_LARGE_NUMBER
        for move in moves:
            self.board.make_move(move, turn)
            move_count += 1

            value, _ = self.minimax_caching(
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

    def next_move_no_alpha_updates(self, ai_player, move_count):

        max_score = alpha = VERY_SMALL_NUMBER
        beta = VERY_LARGE_NUMBER

        best_move = 3
        depth = 5

        for move in self.get_possible_moves():

            self.board.make_move(move, ai_player)
            move_count += 1

            turn = 2 if ai_player == 1 else 1

            minimax = self.minimax(
                depth, turn, alpha, beta, move, move_count, ai_player)
            score = minimax[0]

            if score > max_score:
                max_score = score
                best_move = move

            self.board.undo_move(move)
            move_count -= 1

        return best_move

    def next_move_alpha_updates(self, ai_player, move_count):

        max_score = VERY_SMALL_NUMBER
        min_score = VERY_LARGE_NUMBER

        best_move = 3
        depth = 5

        for move in self.get_possible_moves():

            self.board.make_move(move, ai_player)
            move_count += 1

            turn = 2 if ai_player == 1 else 1

            minimax = self.minimax(
                depth, turn, max_score, min_score, move, move_count, ai_player)
            score = minimax[0]

            if score > max_score:
                max_score = score
                best_move = move

            self.board.undo_move(move)
            move_count -= 1

        return best_move

    def next_move_iterative_deepening(self, ai_player, move_count):

        max_score = VERY_SMALL_NUMBER  # alpha
        min_score = VERY_LARGE_NUMBER  # beta

        best_move = 3
        max_depth = 5

        start_time = time.time()
        move_time = 5

        for depth in range(1, max_depth + 1):

            max_score = VERY_SMALL_NUMBER  # alpha
            min_score = VERY_LARGE_NUMBER  # beta

            moves = self.get_possible_moves()
            if best_move in moves:
                moves.remove(best_move)
                moves.insert(0, best_move)

            for move in moves:
                if time.time() - start_time >= move_time:  # Time limit exceeded
                    print("Time Exceeded")
                    return best_move

                self.board.make_move(move, ai_player)
                move_count += 1

                turn = 2 if ai_player == 1 else 1

                minimax = self.minimax(
                    depth, turn, max_score, min_score, move, move_count, ai_player)
                score = minimax[0]

                if score > max_score:
                    max_score = score
                    best_move = move

                self.board.undo_move(move)
                move_count -= 1

        return best_move

    def minimax(self, depth: int, turn: int, alpha, beta, prev_move, move_count, ai_player):

        if self.board.check_four_connected():  # win
            if turn != ai_player:
                return 1000000 + depth, prev_move
            return -1000000 - depth, prev_move

        if move_count == 42:  # draw
            return 0, prev_move

        if depth == 0:
            score = self.evaluate_board(ai_player)
            return score, prev_move

        if turn == ai_player:
            max_value = VERY_SMALL_NUMBER
            for move in self.get_possible_moves():
                self.board.make_move(move, turn)
                move_count += 1

                # Since turn is either 1 or 2, 3 - turn gives the other player number
                value, _ = self.minimax(
                    depth-1, 3-turn, alpha, beta, move, move_count, ai_player)

                self.board.undo_move(move)
                move_count -= 1

                if value > max_value:
                    max_value = value
                    best_move = move

                if value >= beta:
                    break
                alpha = max(alpha, value)

            return max_value, best_move

        min_value = VERY_LARGE_NUMBER
        for move in self.get_possible_moves():
            self.board.make_move(move, turn)
            move_count += 1

            value, _ = self.minimax(
                depth-1, 3-turn, alpha, beta, move, move_count, ai_player)

            self.board.undo_move(move)
            move_count -= 1

            if value < min_value:
                min_value = value
                best_move = move

            if value <= alpha:
                break
            beta = min(beta, value)

        return min_value, best_move
    
    def simple_next_move(self, ai_player, move_count):
        
        max_score = VERY_SMALL_NUMBER
        best_move = 3
        depth = 5

        for move in self.get_possible_moves():

            self.board.make_move(move, ai_player)
            move_count += 1

            turn = 2 if ai_player == 1 else 1

            minimax = self.simple_minimax(
                depth, turn, move, move_count, ai_player)
            score = minimax[0]

            if score > max_score:
                max_score = score
                best_move = move

            self.board.undo_move(move)
            move_count -= 1

        return best_move
    
    def simple_minimax(self, depth: int, turn: int, prev_move, move_count, ai_player):

        if self.board.check_four_connected():  # win
            if turn != ai_player:
                return 1000000 + depth, prev_move
            return -1000000 - depth, prev_move

        if move_count == 42:  # draw
            return 0, prev_move

        if depth == 0:
            score = self.evaluate_board(ai_player)
            return score, prev_move

        if turn == ai_player:
            max_value = VERY_SMALL_NUMBER
            for move in self.get_possible_moves():
                self.board.make_move(move, turn)
                move_count += 1

                value, _ = self.simple_minimax(
                    depth-1, 3-turn, move, move_count, ai_player)

                self.board.undo_move(move)
                move_count -= 1

                if value > max_value:
                    max_value = value
                    best_move = move

            return max_value, best_move

        min_value = VERY_LARGE_NUMBER
        for move in self.get_possible_moves():
            self.board.make_move(move, turn)
            move_count += 1

            value, _ = self.simple_minimax(
                depth-1, 3-turn, move, move_count, ai_player)

            self.board.undo_move(move)
            move_count -= 1

            if value < min_value:
                min_value = value
                best_move = move

        return min_value, best_move

    def get_possible_moves(self):
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

    def evaluate_board(self, ai_player):
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

        if ai_player == 1:
            return score
        return -score


if __name__ == "__main__":
    test_board = Board()
    ai = AICopy(test_board)

    test_board.make_move(3, 1)
    test_board.make_move(3, 2)
    test_board.make_move(2, 1)
    test_board.make_move(1, 2)
    test_board.make_move(2, 1)

    move_count = 5
    ai_player = 2

    print("Depth 5\n")

    print ("Timing iterative deepening with caching")
    start_time = time.time()
    move = ai.next_move_caching(ai_player, move_count)
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    print("")


    print("Timing iterative deepening no caching")
    start_time = time.time()
    move = ai.next_move_iterative_deepening(ai_player, move_count)
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    print("")

    print("Timing alpha-beta pruning in next move")
    start_time = time.time()
    move = ai.next_move_alpha_updates(ai_player, move_count)
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    print("")

    print("Timing next move without updating alpha")
    start_time = time.time()
    move = ai.next_move_no_alpha_updates(ai_player, move_count)
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    print("")

    print("Timing minimax without alpha beta pruning")
    start_time = time.time()
    move = ai.simple_next_move(ai_player, move_count)
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    print("")

