from board import Board
from ai import AI


class Game:
    """This class manages playing a game of connect 4,
        including the 2 players making moves, and a win/loss or draw occurring.

    """

    def __init__(self, board: Board, ai:AI):
        """Class constructor

        Args:
            board (Board): Game board
            ai (AI): Connect 4 bot
        """
        self._board = board
        self._ai = ai

        self._human_player = 1 #human goes first by default
        self._AI_player = 2
        self._choice = False
        self._move = False

        self._move_count = 0 

    def _make_move(self):
        pass

    def ai_move(self):
        column = self._ai.random_move() #AI class returning column of desired move
        player = self._AI_player

        while not self._move:  #actually this loop doesnt make sense bc will need new number from the AI if move doesnt work 
            move = self._board.make_move(column, player)
            if move:
                self._move = True
                self._move_count += 1
        
        self._board.show_board()


    def player_move(self):
        pass

    def select_start_player(self): #UI function #player 1 starts, human selects if they are player 1 or 2s
        print("Do you want to play as Player 1 or Player 2?")
        while not self._choice:
            player_choice = str(input("Please enter 1 for Player 1, or 2 for player 2: "))
            if player_choice == "1":
                self._choice = True
            if player_choice == "2":
                self._human_player = 2
                self._AI_player = 1
                self._choice = True


if __name__ == "__main__":
    board = Board()
    ai = AI()
    game = Game(board, ai)
    #game.select_start_player()
    game.ai_move()