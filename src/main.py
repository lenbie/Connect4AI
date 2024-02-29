from services.board import Board
from services.game import Game
from services.ai import AI

def main():
    board = Board()
    ai = AI(board)
    game = Game(board, ai)

    game.play_game()


if __name__ == "__main__":
    main()
