from board import Board
from ai import AI


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
        self._AI_player = 2

        self._win = False

    def play_game(self):
        self._select_start_player()

        if self._human_player == 1:
            while not self._win:
                self._player_move()
                if not self._win:
                    self._ai_move()

        if self._AI_player == 1:
            while not self._win:
                self._ai_move()
                if not self._win:
                    self._player_move()
                    
        print(f"Player {self.board.winner} wins!")
              
    def _check_win(self, player):
        win = self.board.check_four_connected(player)
        if win:
            self._win = True

    def _ai_move(self):
        player = self._AI_player
        move = self._ai.next_move(player)

        self.board.make_move(move, player)
        self._check_win(player)

        print("AI Move: ")
        self.board.show_board()

    def _player_move(self):

        player = self._human_player

        choice = False
        while not choice:
            col = (input("\nInto which column from 0 to 6 do you want to make a move?  "))
            try:
                number = int(col)
                if 0 <= number <= 6:
                    move = self.board.make_move(number, player)
                    if move:
                        choice = True
                else:
                    print("\nInput is not between 0 and 6.")
            except ValueError:
                print("\nInput is not a valid integer.")
        
        self._check_win(player)
        
        print("\nYour move: ")
        self.board.show_board()

    # UI function #player 1 starts, human selects if they are player 1 or 2s
    def _select_start_player(self):
        print("Do you want to play as Player 1 or Player 2?")
        choice = False
        while not choice:
            player_choice = str(
                input("\nPlease enter 1 for Player 1, or 2 for player 2: "))
            if player_choice == "1":
                choice = True

            if player_choice == "2":
                self._human_player = 2
                self._AI_player = 1
                choice = True
