
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
        self._board = [[0 for i in range(WIDTH)] for j in range(HEIGHT)] #0 represents empty cell
        self.win = False #Represents whether the current player has won

    def show_board(self):
        """Temporary board representation to print it to command line for manual tests,
            before UI has been implemented.
        """
        for row in self._board:
            print(row)
    
    def _check_valid_move(self, column_index):
        """Checks if a token can be dropped into the chosen column
        Args:
            column_index (int): the integer representing the chosen column

        Returns:
            True, if the column is not full yet
            False, if the column is already full
        """
        if self._board[0][column_index] == 0:
            return True
        else:
            return False
    
    def make_move(self, column_index, current_player):
        """Makes a move if it is valid and no one has won yet.

        Args:
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player
        """

        if not self.win:
            if self._check_valid_move(column_index):
                if self._check_four_connected(column_index, current_player):
                    self.win = True
                    print(f"Player {current_player} wins")

                free_row = self._check_highest_square(column_index)
                self._board[free_row][column_index] = current_player

    def _check_highest_square(self, column_index):
        """Checks which square in the column is the highest free one,
            from 0 being the highest row and 5 the lowest..

        Args:
            column_index (int): integer representing the chosen column

        Returns:
            row (int): The row containing the highest free square in the given column
        """
        for row in range(5, 0, -1):
            if self._board[row][column_index] == 0:     
                return row

    def _check_four_connected(self, column_index, current_player):
        """Checks if the specified move will lead the current player to win.
            Calls functions to check if there will be four in a row, a column or a diagonal.

        Args:
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player

        Returns:
            True, if the current player will win on the specified move
            False, if no win can be achieved on this move.
        """
        row_index = self._check_highest_square(column_index)

        if self._check_row(row_index, column_index, current_player):
            return True
        elif self._check_column(row_index, column_index, current_player):
            return True
        elif self._check_diagonals(row_index, column_index, current_player):
            return True

        return False

    def _check_row(self, row_index, column_index, current_player):
        """Checks if placing a token into the specified square will lead
           the current player to have four tokens in the same row

        Args:
            row_index (int): integer representing the chosen row
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player

        Returns:
            True, if the specified move leads to win in that row
            False, if not
        """
        if column_index <=3:
            for column in range(column_index+1, column_index+4):
                if self._board[row_index][column] != current_player:
                    return False
            return True
        elif column_index >=3:
            for column in range(column_index-1, column_index-4, -1):
                if self._board[row_index][column] != current_player:
                    return False
            return True
 
    def _check_column(self, row_index, column_index, current_player):
        """"Checks if placing a token into the specified square will lead
           the current player to have four tokens in the same column

        Args:
            row_index (int): integer representing the chosen row
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player

        Returns:
            True, if the specified move leads to win in that column
            False, if not
        """
        if row_index <=2:
            for row in range(row_index+1, row_index+4):
                if self._board[row][column_index] != current_player:
                    return False
            return True
        elif row_index >2:
            for row in range(row_index-1, row_index-4, -1):
                if self._board[row][column_index] != current_player:
                    return False
            return True

    def _check_diagonals(self, row_index, column_index, current_player):
        """"Checks if placing a token into the specified square will lead
           the current player to have four tokens on any diagnoal

        Args:
            row_index (int): integer representing the chosen row
            column_index (int): integer representing the chosen column
            current_player (int): player number 1 or 2 representing the current player

        Returns:
            True, if the specified move leads to win on a diagnoal
            False, if not
        """
        #left diagonals
        if column_index - 3 >= 0:
            if row_index - 3 >= 0:
                for num in range(1, 4):
                    if self._board[row_index-num][column_index - num] != current_player:
                        return False
            if row_index + 3 <=5:
                for num in range(1, 4):
                    if self._board[row_index+num][column_index - num] != current_player:
                        return False
                    
        #right diagonals
        elif column_index + 3 <=6:
            if row_index - 3 >= 0:
                for num in range(1, 4):
                    if self._board[row_index-num][column_index + num] != current_player:
                        return False
                    
            if row_index + 3 <=5:
                for num in range(1, 4):
                    if self._board[row_index+num][column_index +num] != current_player:
                        return False
                    
        return True
    
    def clear_board(self):
        """Empties whole board
        """
        self._board = [[0 for i in range(WIDTH)] for j in range(HEIGHT)] 
        
    def check_square(self, row_index, column_index):
        """Returns the content of a specified square

        Args:
            row_index (int): integer representing the chosen row
            column_index (int): integer representing the chosen column
        Returns:
            The content of the specified square (int)
        """
        return self._board[row_index][column_index]
        
        

if __name__ == "__main__":
    board = Board()
    board.make_move(1, 1)
    board.make_move(2, 2)
    board.make_move(2, 1)
    board.make_move(2, 1)
    board.make_move(1, 1)
    board.make_move(3, 1)
    board.make_move(3, 1)
    board.make_move(1, 2)
    board.make_move(1, 1)
    board.make_move(4, 1)
    board.show_board()
