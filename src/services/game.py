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

    def play_game(self):
        """Main game loop, managing the AI and human player
            making moves until one of them wins.
        """
        move_count = 0

        self.board.clear_board()
        self._select_start_player()

        if self._human_player == 1:
            while not self._win:
                self._player_move()
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
                    self._player_move()
                    move_count += 1
                    self._check_draw(move_count)

        if self._winner == 1:
            colour = "🟡"
        if self._winner == 2:
            colour = "🔴"
        print(f"Player {colour} wins!")
        self._play_again()

    def _play_again(self):
        again = input("\nDo you want to play again? Please type YES or NO: ")
        if again.lower() == "yes":
            self._win = False
            self._winner = None
            self.play_game()

    def _check_win(self, player):
        """Checks if someone has won the game yet.

        Args:
            player: The current player (human or AI player)
        """
        win = self.board.check_four_connected()
        if win:
            self._win = True
            self._winner = player

    def _check_draw(self, move_count):
        """Checks if a draw has occurred.

        Args:
            move_count (int): The number of moves played so far.

        Returns:
            True, if a draw has occurred - the board is full but no one has won
            False, otherwise
        """

        if move_count == 42 and not self._win:
            print("\nDraw!")
            self._play_again()

    def _ai_move(self, moves):
        """Manages the AI making moves.
        Prints the board once a move has been made.

        Args:
            moves (int): number of moves in the game so far
        """
        player = self._ai_player
        move = self._ai.next_move(player, moves)

        self.board.make_move(move, player)
        self._check_win(player)

        print("AI Move: ")
        self.board.show_board()

    def _player_move(self):
        """Manages the human player making moves via asking for input.
        Prints the board once a move has been made.
        """

        player = self._human_player

        choice = False
        while not choice:
            col = (
                input("\nInto which column from 0 (left) to 6 (right) do you want to make a move?  "))
            try:
                number = int(col)
                if self.board.check_valid_move(number):
                    self.board.make_move(number, player)
                    choice = True
                else:
                    print("\nInput is not a valid move.")
            except ValueError:
                print("\nInput is not a valid integer.")

        self._check_win(player)

        print("\nYour move: ")
        self.board.show_board()

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
