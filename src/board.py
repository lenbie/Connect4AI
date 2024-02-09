
"""Setting constants for board size"""
WIDTH = 7
HEIGHT = 6


class Board:

    """ This class creates the game board, enables making moves on the board,
        including checking valid moves and wins,
        and stores the current state of the board.
    """

    def __init__(self):
        """Class constructor                
        """
        self.board = [[0 for i in range(WIDTH)] for j in range(
            HEIGHT)]  # 0 represents empty cell
        self.win = False #if anyone has won, but idk if needed
        self.move_count = 0
        self.winner = None

    def show_board(self):
        """Temporary board representation to print it to command line for manual tests,
            before UI has been implemented.
        """
        for row in self.board:
            print(row)
        print("")

    def check_valid_move(self, column_index):
        """Checks if a token can be dropped into the chosen column
        Args:
            column_index (int): the integer representing the chosen column

        Returns:
            True, if the column is not full yet
            False, if the column is already full
        """
        if column_index >= 0 and column_index <=6:
            if self.board[0][column_index] == 0:
                return True
        return False

    def make_move(self, column_index, current_player):
        """Makes a move if it is valid and no one has won yet.

        Args:
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player
        """

        if not self.win:
            if self.check_valid_move(column_index):
                free_row = self._check_highest_square(column_index)
                self.board[free_row][column_index] = current_player
                self.move_count += 1
                return True
        return False

    def undo_move(self, column_index):
        """Unmakes the most recent move.

        Args:
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player
        """
        if self.check_valid_move(column_index):
            free_row = self._check_highest_square(column_index)
            self.board[free_row + 1][column_index] = 0
        else:
            self.board[0][column_index] = 0
        self.move_count -= 1

    def _check_highest_square(self, column_index):
        """Checks which square in the column is the highest free one,
            from 0 being the highest row and 5 the lowest..

        Args:
            column_index (int): integer representing the chosen column

        Returns:
            row (int): The row containing the highest free square in the given column
        """
        for row in range(5, -1, -1):
            if self.board[row][column_index] == 0:
                return row

    # idk if current player check necessary
    def check_four_connected(self, current_player):
        """Checks if the specified move will lead the current player to win.
            Calls functions to check if there will be four in a row, a column or a diagonal.

        Args:
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player

        Returns:
            True, if the current player will win on the specified move
            False, if no win can be achieved on this move.
        """
        if current_player == self._check_all_rows() or current_player == self._check_all_cols() or current_player == self._check_diag_whole_board():
            self.winner = current_player
            return True
        return False

    def _check_all_cols(self):
        for row in range(3):
            for col in range(7):
                if self.board[row][col] != 0:
                    if self._check_col(row, col):
                        winner = self.board[row][col]
                        return winner

    def _check_col(self, row, col):
        piece = self.board[row][col]
        for i in range(1, 4):
            if self.board[row+i][col] != piece:
                return False
        return True

    def _check_all_rows(self):
        for col in range(4):
            for row in range(6):
                if self.board[row][col] != 0:
                    if self._check_row(row, col):
                        winner = self.board[row][col]
                        return winner

    def _check_row(self, row, col):
        piece = self.board[row][col]
        for i in range(1, 4):
            if self.board[row][col+i] != piece:
                return False
        return True

    def _check_diag_whole_board(self):  # make sure only 1 winner possible
        for row in range(0, 3):
            for col in range(0, 4):
                # see if we need this, or getting player as input
                if self.board[row][col] != 0:
                    if self._check_right_diagonals(row, col):
                        winner = self.board[row][col]
                        return winner  # return True or winner? currently returns None if no winner

        for row in range(5, 2, -1):
            for col in range(0, 4):
                if self.board[row][col] != 0:
                    if self._check_left_diagonals(row, col):
                        winner = self.board[row][col]
                        return winner  # return True or winner?

    def _check_right_diagonals(self, row, col):
        piece = self.board[row][col]
        for i in range(1, 4):
            if self.board[row+i][col+i] != piece:
                return False
        return True

    def _check_left_diagonals(self, row, col):
        piece = self.board[row][col]
        for i in range(1, 4):
            if self.board[row-i][col+i] != piece:
                return False
        return True

    def clear_board(self):
        """Empties whole board
        """
        self.board = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
        self.win = False
        self.move_count = 0
        self.winner = None

    def check_square(self, row_index, column_index):
        """Returns the content of a specified square

        Args:
            row_index (int): integer representing the chosen row
            column_index (int): integer representing the chosen column
        Returns:
            The content of the specified square (int)
        """
        return self.board[row_index][column_index]


if __name__ == "__main__":
    testboard = Board()
    testboard.make_move(2, 1)
    testboard.make_move(3, 1)
    testboard.make_move(4, 2)
    testboard.make_move(5, 2)
    win = testboard._check_row(5, 2)
    testboard.show_board()
    print(win)
    # print(board.check_four_connected(1))
