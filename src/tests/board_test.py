import unittest

from services.board import Board


"""Setting constants for board size"""
WIDTH = 7
HEIGHT = 6

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.testboard = Board()
        self.testboard.clear_board()

    def test_valid_move(self):
        """Tests whether check_valid_move returns True if the column is not full
        """
        self.testboard.clear_board()

        self.testboard.board[5][1] = 1
        self.testboard.board[4][2] = 1
        self.testboard.board[3][3] = 1
        self.testboard.board[2][4] = 2
        self.testboard.board[1][4] = 2
        self.testboard.board[0][1] = 2

        valid_move = self.testboard.check_valid_move(3)

        self.assertEqual(valid_move, True)

    def test_invalid_move_full_col(self):
        """Tests whether check_valid_move returns False if the column is full
        """
        self.testboard.clear_board()

        self.testboard.board[5][3] = 1
        self.testboard.board[4][3] = 1
        self.testboard.board[3][3] = 1
        self.testboard.board[2][3] = 2
        self.testboard.board[1][3] = 2
        self.testboard.board[0][3] = 2

        invalid_move = self.testboard.check_valid_move(3)

        self.assertEqual(invalid_move, False)
    
    def test_invalid_move_col_num(self):
        """Tests whether check_valid_move returns False
        if a column number outside the range from 0 to 6 is given.
        """
        self.testboard.clear_board()

        invalid_move = self.testboard.check_valid_move(7)

        self.assertEqual(invalid_move, False)
    
    def test_check_square_content(self):
        """Tests that the _check_square_content function returns the correct content of the square.
        """
        self.testboard.board[0][0] = 1

        square_content = self.testboard._check_square_content(0, 0)

        self.assertEqual(square_content, 1)

    def test_move_correct_square(self):
        """Tests that the make_move function results in the correct change in the board
        - puts the correct player piece on the correct square.
        """
        player = 1
        column_index = 3

        self.testboard.make_move(column_index, player)

        row_index = 5 #Since the board is empty before the move was made, the token is dropped to the bottom row

        square_content = self.testboard._check_square_content(row_index, column_index)

        self.assertEqual(square_content, 1)

    def test_move_overallboard(self):
        """Tests that make_move changes the entire board appropriately, 
        i.e. that there are no changes except on the desired square.
        """
        self.testboard.clear_board()

        player = 1
        column_index = 3

        correctboard = [[0 for i in range(7)] for j in range(6)]
        correctboard[5][3] = 1

        self.testboard.make_move(column_index, player)

        board = self.testboard.board

        self.assertEqual(board, correctboard)

    def test_make_move_returns_True(self):
        """Tests that make_move returns True upon making a valid move
        """
        self.testboard.clear_board()

        column_index = 0
        player = 1
        move = self.testboard.make_move(column_index, player)

        self.assertEqual(move, True)

    def test_make_move_returns_False(self):
        """Tests that make_move returns False if attempting to make an invalid move.
        """
        self.testboard.clear_board()

        column_index = 7 #invalid column
        player = 1
        move = self.testboard.make_move(column_index, player)

        self.assertEqual(move, False)

    def test_make_move_no_change_invalid_move(self):
        """Tests that the board does not change if attempting invalid move.
        """
        self.testboard.clear_board()

        player = 1
        column_index = 7 #invalid column

        correctboard = [[0 for i in range(7)] for j in range(6)]

        self.testboard.make_move(column_index, player)

        board = self.testboard.board

        self.assertEqual(board, correctboard)

    def test_make_move_no_change_full_board(self):
        """Tests that make move makes no changes if the board is full.
        """
        self.testboard.clear_board()

        check_board = [
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2]]
        
        self.testboard.board = check_board
        
        column_index = 0
        player = 2
        #Tests that the top left square does not change content
        self.testboard.make_move(column_index, player)

        self.assertEqual(self.testboard.board, check_board)

    def test_clear_board(self):
        """Tests that clear_board actually clears the entire board.
        """
        self.testboard.clear_board()
        self.testboard.make_move(2, 1)
        self.testboard.make_move(3, 2)

        clear_board = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

        self.testboard.clear_board()

        self.assertEqual(self.testboard.board, clear_board)

    def test_check_highest_square(self):
        """Test that _check_highest_square returns the correct row index
        """
        self.testboard.clear_board()

        bottom_row = 5
        row_index = self.testboard._check_highest_square(0)

        self.assertEqual(bottom_row, row_index)

    def test_check_highest_square_full_column(self):
        """Test that _check_highest_square returns None if the column is full
        """
        self.testboard.clear_board()

        self.testboard.board[5][3] = 1
        self.testboard.board[4][3] = 1
        self.testboard.board[3][3] = 1
        self.testboard.board[2][3] = 2
        self.testboard.board[1][3] = 2
        self.testboard.board[0][3] = 2

        row_index = self.testboard._check_highest_square(3)

        self.assertEqual(None, row_index)
    
    def test_undo_move_full_col(self):
        """Tests that undo_move sets the top square in the given column to 0
        """
        self.testboard.clear_board()

        column = 3
        self.testboard.board[5][column] = 1
        self.testboard.board[4][column] = 1
        self.testboard.board[3][column] = 1
        self.testboard.board[2][column] = 2
        self.testboard.board[1][column] = 2
        self.testboard.board[0][column] = 2

        self.testboard.undo_move(column)

        square_content = self.testboard.board[0][column]
        self.assertEqual(square_content, 0)
    
    def test_undo_move_non_full_col(self):
        """Tests that undo_move sets the highest taken square in the col to 0
        """
        self.testboard.clear_board()

        column = 3
        self.testboard.board[5][column] = 1
        self.testboard.board[4][column] = 1
        self.testboard.board[3][column] = 1
        #Highest taken square is row 3 column 3

        self.testboard.undo_move(column)

        square_content = self.testboard.board[3][column]
        self.assertEqual(square_content, 0)
        
    def test_check_row_win(self):
        """Tests if the _check_row function returns True if there are 
        four connected from the given index
        """
        self.testboard.clear_board()

        self.testboard.make_move(2, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(4, 1)
        self.testboard.make_move(5, 1)

        row_index = 5 #bottom row
        col_index = 2

        win = self.testboard._check_row(row_index, col_index)

        self.assertEqual(win, True)

    def test_check_row_no_win(self):
        """Tests if the _check_row function returns False if there are
        not four connected from the given index
        """
        self.testboard.clear_board()

        self.testboard.make_move(2, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(4, 2)
        self.testboard.make_move(5, 2)

        row_index = 5 #bottom row
        col_index = 2

        win = self.testboard._check_row(row_index, col_index)

        self.assertEqual(win, False)

    def test_check_all_rows_win_case1(self):
        """Tests if _check_all_rows returns True if a player has a win
        """
        self.testboard.clear_board()

        self.testboard.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 1, 2, 1, 0],
        [2, 2, 2, 2, 1, 1, 0],
        [1, 1, 2, 2, 1, 1, 0]]

        win = self.testboard._check_all_rows()

        self.assertEqual(win, True)

    def test_check_all_rows_win_case2(self):
        """Tests if _check_all_rows returns True if another player has a win
        """
        self.testboard.clear_board()

        self.testboard.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 2, 1, 1, 1, 1],
        [0, 0, 2, 1, 2, 2, 2],
        [0, 0, 2, 2, 2, 1, 1]]

        win = self.testboard._check_all_rows()

        self.assertEqual(win, True)
    
    def test_check_all_rows_no_win(self):
        """Tests if _check_all_rows returns False if no player has a win
        """
        self.testboard.clear_board()

        self.testboard.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 2, 1, 2, 2],
        [0, 0, 2, 2, 1, 1, 2],
        [0, 0, 2, 2, 1, 1, 1]]

        win = self.testboard._check_all_rows()

        self.assertEqual(win, False)
    
    def test_check_four_connected_row_win(self):
        """Tests if the check_four_connected function returns True if any player has 
        4 connected in any row.
        """
        self.testboard.clear_board()

        self.testboard.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 2, 1, 1, 1, 1],
        [0, 0, 2, 1, 2, 2, 2],
        [0, 0, 2, 2, 2, 1, 1]]

        win = self.testboard.check_four_connected()

        self.assertEqual(win, True)

    def test_check_col_win(self):
        """Tests if the _check_col function returns True if there is four connected
        of the same player starting from the given index.
        """
        self.testboard.clear_board()

        col = 2
        self.testboard.make_move(col, 1)
        self.testboard.make_move(col, 1)
        self.testboard.make_move(col, 1)
        self.testboard.make_move(col, 1)

        row = 2 #since 4 rows filled from bottom up, and the search goes from top to bottom
        win = self.testboard._check_col(row, col)

        self.assertEqual(win, True)

    def test_check_col_no_win(self):
        """Tests if the _check_col function returns False if there is not four connected
        of the same player starting from the given index.
        """
        self.testboard.clear_board()

        col = 2
        self.testboard.make_move(col, 1)
        self.testboard.make_move(col, 1)
        self.testboard.make_move(col, 2)
        self.testboard.make_move(col, 2)

        row = 2 #since 4 rows filled from bottom up, and the search goes from top to bottom

        win = self.testboard._check_col(row, col)
        self.assertEqual(win, False)
    
    def test_check_all_cols_no_win(self):
        """Tests that the _check_all_cols function returns False
        if no player has four connected in any column
        """
        self.testboard.clear_board()

        self.testboard.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 2, 1, 2, 1, 1],
        [0, 0, 2, 1, 2, 2, 2],
        [0, 0, 2, 2, 2, 1, 1]]

        win = self.testboard._check_all_cols()

        self.assertEqual(win, False)
    
    def test_check_all_cols_win_case1(self):
        """Tests that the _check_all_cols function returns True
        if a player has four connected in any column 
        """
        self.testboard.clear_board()

        self.testboard.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 2, 0, 0],
        [1, 0, 2, 1, 2, 0, 0],
        [1, 0, 2, 1, 1, 2, 2],
        [2, 1, 2, 2, 2, 1, 1]]

        win = self.testboard._check_all_cols()

        self.assertEqual(win, True)
    
    def test_check_all_cols_win_case2(self):
        """Tests that the _check_all_cols function returns True
        if a player has four connected in any column 
        """
        self.testboard.clear_board()

        self.testboard.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 2],
        [2, 0, 2, 1, 0, 0, 2],
        [1, 1, 2, 1, 0, 0, 2],
        [1, 1, 1, 2, 2, 1, 2]]

        win = self.testboard._check_all_cols()

        self.assertEqual(win, True)

    def test_four_connected_col_win(self):
        """Tests if the check_four_connected function returns True if any player has 
        4 connected in any column.
        """
        self.testboard.clear_board()

        self.testboard.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 2],
        [2, 0, 2, 1, 0, 0, 2],
        [1, 1, 2, 1, 0, 0, 2],
        [1, 1, 1, 2, 2, 1, 2]]

        win = self.testboard.check_four_connected()

        self.assertEqual(win, True)
    
#DIAGNOALS

    def test_check_right_up_diagonal(self):
        self.testboard.clear_board()

        self.testboard.make_move(1, 1)
        self.testboard.make_move(2, 2)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(1, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(3, 2)
        self.testboard.make_move(0, 1)
        self.testboard.make_move(3, 1)

        win = self.testboard._check_diag_whole_board()
        self.assertEqual(win, 1)

    def test_check_right_down_diagonal(self):
        self.testboard.clear_board()

        self.testboard.make_move(1, 1)
        self.testboard.make_move(2, 2)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(2, 1)
        self.testboard.make_move(1, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(3, 1)
        self.testboard.make_move(1, 2)
        self.testboard.make_move(1, 1)
        self.testboard.make_move(4, 1)

        win = self.testboard._check_right_down_diagonals(2, 1)
        self.assertEqual(win, True)

    def test_check_four_connected_no_win_draw(self):
        """Tests if check_four_connected returns False
        if neither player has a win on the board due to a draw.
        """
        self.testboard.clear_board()

        self.testboard.board = [
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2]] 
        #Draw board

        win = self.testboard.check_four_connected()
        self.assertEqual(win, False)
    
    def test_check_four_connected_no_win_yet(self):
        """Tests if check_four_connected returns False
        if neither player has a win on the board yet.
        """
        self.testboard.clear_board()

        self.testboard.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 2, 1, 2, 2],
            [0, 0, 2, 2, 1, 1, 2],
            [0, 0, 2, 2, 1, 1, 1]]
            
        win = self.testboard.check_four_connected()
        self.assertEqual(win, False)