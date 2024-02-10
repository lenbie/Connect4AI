from board import Board


class AI:
    def __init__(self, board: Board):
        self.board = board
        self._current_player = 2

    def next_move(self, player):
        max_score = -999999
        best_move = 0
        depth = 3

        for move in self.get_possible_moves():
            self._current_player = player

            self.board.make_move(move, self._current_player)

            player_one = bool(self._current_player == 1)

            score = self.minimax(depth, player_one)

            if score > max_score:
                max_score = score
                best_move = move
            self.board.undo_move(move)
        return best_move

    def minimax(self, depth, player_one):  # TRUE if player 1, FAlSE if player 2
        if player_one:
            current_player = 1
        else:
            current_player = 2

        if self.board.check_four_connected(current_player): #win
            if current_player == 1:
                return 100000 + depth
            return -100000 - depth

        if self.board.move_count + (5 - depth) == 42:  # draw
            return 0

        if depth == 0:
            return self.evaluate_board()
            #return self.heuristic_evaluation()

        if player_one:
            value = -999999
            for move in self.get_possible_moves():
                self.board.make_move(move, current_player)
                value = max(value, self.minimax(depth-1, False))
                self.board.undo_move(move)

            return value

        value = 999999
        for move in self.get_possible_moves():
            self.board.make_move(move, current_player)
            value = min(value, self.minimax(depth-1, True))
            self.board.undo_move(move)

        return value

    def get_possible_moves(self):
        moves = set()

        for column in range(0, 7):
            valid = self.board.check_valid_move(column)
            if valid:
                moves.add(column)

        return moves

    def _evaluate_window(self, window):
        player = self._current_player
        if player == 1:
            other = 2
        else:
            other = 1

        score = 0
        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(player) == 2 and window.count(0) == 2:
            score += 2

        if window.count(other) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def evaluate_board(self):

        score = 0

        # Check horizontal
        for row in range(6):
            for col in range(4):
                window = [self.board.board[row][col], self.board.board[row][col + 1], self.board.board[row][col + 2], self.board.board[row][col + 3]]
                score += self._evaluate_window(window)

        # Check vertical
        for row in range(3):
            for col in range(7):
                window = [self.board.board[row][col], self.board.board[row + 1][col], self.board.board[row + 2][col], self.board.board[row + 3][col]]
                score += self._evaluate_window(window)

        # Check right downward diagonals
        for row in range(3):
            for col in range(4):
                window = [self.board.board[row][col], self.board.board[row + 1][col + 1], self.board.board[row + 2][col + 2], self.board.board[row + 3][col + 3]]
                score += self._evaluate_window(window)

        # Check left upward diagonals
        for row in range(3):
            for col in range(3, 7):
                window = [self.board.board[row][col], self.board.board[row + 1][col - 1], self.board.board[row + 2][col - 2], self.board.board[row + 3][col - 3]]
                score += self._evaluate_window(window)

        return score

    def heuristic_evaluation(self):
        graph_current = self._create_graph_from_array(
            self.board.board, self._current_player)
        
        if self._current_player == 1:
            other = 2
        else:
            other = 1

        graph_other = self._create_graph_from_array(self.board.board, other)
        
        nodes_current = 0
        degree_count_current = 0
        for value in graph_current.items():
            nodes_current += 1
            degree_count_current += len(value)

        if nodes_current > 0:
            average_node_degree_current = degree_count_current / nodes_current
        else:
            average_node_degree_current = 0

        nodes_other = 0
        degree_count_other = 0
        for value in graph_other.items():
            nodes_other += 1
            degree_count_other += len(value)

        if nodes_other > 0:
            average_node_degree_other = degree_count_other / nodes_other
        else:
            average_node_degree_other = 0

        return average_node_degree_current - average_node_degree_other

    def _create_graph_from_array(self, array, player):
        graph = {}
        rows, cols = 6, 7

        def is_valid(x, y):  # valid coordinates
            return 0 <= x < rows and 0 <= y < cols

        def add_edge(x1, y1, x2, y2):
            if is_valid(x2, y2) and array[x2][y2] == player:
                if (x1, y1) not in graph:
                    graph[(x1, y1)] = []
                graph[(x1, y1)].append((x2, y2))

        for i in range(rows):
            for j in range(cols):
                if array[i][j] == player:

                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # rows and cols
                        add_edge(i, j, i + dx, j + dy)

                    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:  # diagonals
                        add_edge(i, j, i + dx, j + dy)

        return graph
