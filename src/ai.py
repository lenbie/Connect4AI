import random
from board import Board

class AI:
    def __init__(self, board:Board):
        self._board = board
        self._current_player = None
        
    def random_move(self):
        column = random.randint(0,7)
        return column

    def minimax(self, position, depth, player_one): #TRUE if player 1, FAlSE if player 2
        if player_one:
            self._current_player = 1
        else:
            self._current_player = 2

        if self._board.win:
            if self._current_player == 1:
                return 1000 + depth
            return -1000 - depth
        
        if self._board.move_count + (5 - depth) == 42: #draw
            return 0

        if depth == 0:
            return self.heuristic_evaluation(position)
    
        if player_one:
            value = -999999
            for move in self.get_possible_moves():
                position = self._board.make_move(move, self._current_player)
                value = max(value, self.minimax(position, depth-1, False))
                self._board.undo_move(move)

            return value
        
        else:
            value = 999999
            for move in self.get_possible_moves():
                position = self._board.make_move(move, self._current_player)
                value = min(value, self.minimax(position, depth-1, True))
                self._board.undo_move(move)

            return value
    
    def get_possible_moves(self):
        moves = set()

        for column in range(0, 7):
            valid =  self._board._check_valid_move(column)
            if valid:
                moves.add(column)

        return moves
    
    def heuristic_evaluation(self, position):
        graph_current = self._create_graph_from_array(self._board, self._current_player)
        if self._current_player == 1:
            other = 2
        other = 1
        graph_other = self._create_graph_from_array(self._board, other)

        nodes_current = 0
        degree_count_current = 0
        for key, value in graph_current.items():
            nodes_current += 1
            degree_count_current += len(value)
        
        average_node_degree_current = degree_count_current / nodes_current

        nodes_other = 0
        degree_count_other = 0
        for key, value in graph_other.items():
            nodes_other += 1
            degree_count_other += len(value)
        
        average_node_degree_other = degree_count_other / nodes_other

        return average_node_degree_current - average_node_degree_other


    def _create_graph_from_array(self, array, player):
        graph = {}
        rows, cols = 6, 7
        
        def is_valid(x, y): #valid coordinates
            return 0 <= x < rows and 0 <= y < cols
        
        def add_edge(x1, y1, x2, y2):
            if is_valid(x2, y2) and self.array[x2][y2] == player:
                if (x1, y1) not in graph:
                    graph[(x1, y1)] = []
                graph[(x1, y1)].append((x2, y2))
        
        for i in range(rows):
            for j in range(cols):
                if self.array[i][j] == player:

                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: #rows and cols
                        add_edge(i, j, i + dx, j + dy)
                    
                    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]: #diagonals
                        add_edge(i, j, i + dx, j + dy)
        
        return graph
