from services.board import Board
from services.ai import AI


class Game:
    """This class manages playing a game of connect 4,
        including the 2 players making moves, and a win/loss or draw occurring.

    """

    def __init__(self, board: Board, ai: AI):
        """Class constructor

        Args:
            board (Board): Game board
            ai (AI): Connect 4 bot
        """
        self.board = board
        self._ai = ai

        self._human_player = 1  # human goes first by default
        self._ai_player = 2

        self._win = False
        self._winner = None
        
    def show_board(self):
        """UI Function: Board representation to print to command line.
        """

        print("+----+----+----+----+----+----+----+")
        for row in range(6):
            print("|", end="")
            for col in range(7):
                if self.board.board[row][col] == 0:
                    print("    |", end="")
                elif self.board.board[row][col] == 1:
                    print(" 🟡 |", end="")
                else:
                    print(" 🔴 |", end="")
            print()
            print("+----+----+----+----+----+----+----+")

    def play_game(self):
        """Main game loop, managing the AI and human player
            making moves until one of them wins.
        """
        move_count = 0

        self.board.clear_board()
        self._select_start_player()

        if self._human_player == 1:
            while not self._win:
                self._player_move(move_count)
                move_count += 1
                self._check_draw(move_count)
                if not self._win:
                    self._ai_move(move_count)
                    move_count += 1
                    self._check_draw(move_count)

        if self._ai_player == 1:
            while not self._win:
                self._ai_move(move_count)
                move_count += 1
                self._check_draw(move_count)
                if not self._win:
                    self._player_move(move_count)
                    move_count += 1
                    self._check_draw(move_count)

        #Determining winner, progressing to game end or next game
        if self._winner == 1:
            colour = "🟡"
        if self._winner == 2:
            colour = "🔴"
        print(f"Player {colour} wins!")
        self._play_again()

    def _play_again(self):
        """Manages the possibility to play again, asks for player choice
        and resets global variables.
        """
        again = input("\nPlease type YES to play again: ")
        if again.lower() == "yes":
            self._win = False
            self._winner = None
            self.play_game()

    def _check_win(self, player):
        """Checks if someone has won the game yet, 
        and sets global variables appropriately.

        Args:
            player: The current player (human or AI player)
        """
        win = self.board.check_four_connected()
        if win:
            self._win = True
            self._winner = player

    def _check_draw(self, move_count):
        """Checks if a draw has occurred and calls the _play_again function

        Args:
            move_count (int): The number of moves played so far.
        """

        if move_count == 42 and not self._win:
            print("\nDraw!")
            self._play_again()

    def _ai_move(self, move_count):
        """Manages the AI making moves.
        Prints the board once a move has been made.

        Args:
            move_count (int): number of moves in the game so far
        """
        player = self._ai_player
        move = self._ai.next_move(player, move_count)

        self.board.make_move(move, player)
        self._check_win(player)

        print("AI Move: ")
        self.show_board()
        print(self.board.board)


    def _player_move(self, move_count):
        """Manages the human player making moves via asking for input.
        This includes re-prompting upon invalid input, making the move, and checking for win.
        Prints the board once a move has been made.
        """

        player = self._human_player

        move = self._ai.next_move(player, move_count)

        self.board.make_move(move, player)
        #choice = False
        #while not choice:
        #    col = (input(
        #    """\nInto which column from 0 (left) to 6(right) do you want to make a move?  """))
        #    try:
        #        number = int(col)
        #        if self.board.check_valid_move(number):
        #            self.board.make_move(number, player)
        #            choice = True
        #        else:
        #            print("\nInput is not a valid move.")
        #    except ValueError:
        #        print("\nInput is not a valid integer.")

        self._check_win(player)

        print("\nYour move: ")
        self.show_board()
        print(self.board.board)

    def _select_start_player(self):
        """Manages the choice for starting player via terminal input.
        The human player can select Player 1 (starting player) or player 2.
        The AI will be the player the human does not select.
        """
        print("\nDo you want to play as Player 1 🟡 or Player 2 🔴?")
        choice = False
        while not choice:
            player_choice = str(
                input("\nPlease enter 1 for 🟡, or 2 for 🔴: "))
            if player_choice == "1":
                self._human_player = 1
                self._ai_player = 2
                choice = True

            if player_choice == "2":
                self._human_player = 2
                self._ai_player = 1
                choice = True
