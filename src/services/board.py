
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

    def show_board(self):
        """UI Function: Board representation to print to command line.
        """

        print("+----+----+----+----+----+----+----+")
        for row in range(6):
            print("|", end="")
            for col in range(7):
                if self.board[row][col] == 0:
                    print("    |", end="")
                elif self.board[row][col] == 1:
                    print(" 🟡 |", end="")
                else:
                    print(" 🔴 |", end="")
            print()
            print("+----+----+----+----+----+----+----+")

    def check_valid_move(self, column_index):
        """Checks if a token can be dropped into the chosen column
        Args:
            column_index (int): the integer representing the chosen column

        Returns:
            True, if the column is not full yet
            False, if the column is already full
        """
        if 0 <= column_index <= 6:
            if self.board[0][column_index] == 0:
                return True
        return False

    def make_move(self, column_index, current_player):
        """Makes a move if it is valid and no one has won yet.

        Args:
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player

        Returns:
            True, if the move was successfully made
            False, otherwise
        """

        if self.check_valid_move(column_index):
            free_row = self._check_highest_square(column_index)
            self.board[free_row][column_index] = current_player
            return True
        return False

    def undo_move(self, column_index):
        """Unmakes the most recent move.

        Args:
            column_index (int): integer representing the chosen column
        """
        if self.check_valid_move(column_index):
            free_row = self._check_highest_square(column_index)
            self.board[free_row + 1][column_index] = 0
        else:
            self.board[0][column_index] = 0

    def _check_highest_square(self, column_index):
        """Checks which square in the column is the highest free one,
            from 0 being the highest row and 5 the lowest..

        Args:
            column_index (int): integer representing the chosen column

        Returns:
            row (int): The row containing the highest free square in the given column
            None, if there is no free square in the column. In practice, this will not occur
                since before calling this function, there is always the
                check_valid_move function to see whether the column is full.
        """
        for row in range(5, -1, -1):
            if self.board[row][column_index] == 0:
                return row
        return None

    def check_four_connected(self):
        """Checks if any player has four pieces in a row, a column or diagonal.

        Args:
            column_index (int): integer representing the chosen column

        Returns:
            True, any player has 4 connected.
            False, if no win has been achieved by anyone.
        """

        if self._check_all_rows() or self._check_all_cols() or self._check_diag_whole_board():
            return True
        return False

    def _check_all_cols(self):
        """Checks if there are four connected of any player in any column of the board.

        This works as follows: We iterate through the first three rows, 
        and for each column in those rows, we call the _check_col function.
        This function checks whether there is four connected in that column
        starting from the given square (row, col). We only need to check the first three rows, 
        as there is 6 rows in total, so there cannot be four connected in a column starting
        any lower than the third row from the top (row index 2).

        Returns:
            True, if any player has four connected in some column
            False, if not.
        """
        for row in range(3):
            for col in range(7):
                if self.board[row][col] != 0:
                    if self._check_col(row, col):
                        return True
        return False

    def _check_col(self, row, col):
        """Checks if there are four connected in a column starting
        from the given row and column indices.
        This function checks which piece is at the given square at index (row, col),
        and then checks if there is the same piece in the next three squares in the same column.

        Args:
            row (int): Starting row index
            col (int): Starting column index

        Returns:
            True, if there are four connected in that part of the column.
            False, if not.
        """
        piece = self.board[row][col]
        for i in range(1, 4):
            if self.board[row+i][col] != piece:
                return False
        return True

    def _check_all_rows(self):
        """Checks if there are four connected of any player in any row of the board.

        This works as follows: We iterate through the first four columns, 
        and for each row in those columns, we call the _check_row function.
        This function checks whether there is four connected in that row
        starting from the given square (row, col). We only need to check the first four columns, 
        as there is 7 columns in total, so there cannot be four connected in a column starting
        any lower than the fourth column from the left (column index 3).

        Returns:
            winner (int or None): If there is a win, the number of the winning player
        """
        for col in range(4):
            for row in range(6):
                if self.board[row][col] != 0:
                    if self._check_row(row, col):
                        return True
        return False

    def _check_row(self, row, col):
        """Checks if there are four connected in a row starting from the row and column index given.
        First, checks which piece is at the given square at index (row, col),
        and then checks if there is the same piece in the next three squares in the same row.

        Args:
            row (int): Starting row index
            col (int): Starting column index

        Returns:
            True, if there are four connected.
            False, if not.
        """
        piece = self.board[row][col]
        for i in range(1, 4):
            if self.board[row][col+i] != piece:
                return False
        return True

    def _check_diag_whole_board(self):
        """Checks if there are four connected of any player
        in any diagonal of the board.

        Returns:
            True, if there are four connected.
            False, if not.
        """
        for row in range(0, 3):
            for col in range(0, 4):
                if self.board[row][col] != 0:
                    if self._check_right_down_diagonals(row, col):
                        return True

        for row in range(5, 2, -1):
            for col in range(0, 4):
                if self.board[row][col] != 0:
                    if self._check_right_up_diagonals(row, col):
                        return True
        return False

    def _check_right_down_diagonals(self, row, col):
        """Checks if there are four connected in a right downward diagonal
        starting from the row and column index given.

        Args:
            row (int): Starting row index
            col (int): Starting column index

        Returns:
            True, if there are four connected.
            False, if not.
        """
        piece = self.board[row][col]
        for i in range(1, 4):
            if self.board[row+i][col+i] != piece:
                return False
        return True

    def _check_right_up_diagonals(self, row, col):
        """Checks if there are four connected in a right upward diagonal
        starting from the row and column index given.

        Args:
            row (int): Starting row index
            col (int): Starting column index

        Returns:
            True, if there are four connected.
            False, if not.
        """
        piece = self.board[row][col]
        for i in range(1, 4):
            if self.board[row-i][col+i] != piece:
                return False
        return True

    def clear_board(self):
        """Empties whole board
        """
        self.board = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

    def _check_square_content(self, row_index, column_index):
        """Returns the content of a specified square

        Args:
            row_index (int): integer representing the chosen row
            column_index (int): integer representing the chosen column
        Returns:
            The content of the specified square (int)
        """
        return self.board[row_index][column_index]


if __name__ == "__main__":
    board = Board()
    board.make_move(3, 1)
    board.show_board()
