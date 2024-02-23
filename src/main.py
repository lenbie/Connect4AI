from board import Board
from game import Game
from ai import AI

#from board_copy import Board
#from game_copy import Game
#from ai_copy import AI

def main():
    board = Board()
    ai = AI(board)
    game = Game(board, ai)

    game.play_game()


if __name__ == "__main__":
    main()
