from board import Board
from game import Game
from ai import AI


def main():
    board = Board()
    ai = AI(board)
    game = Game(board, ai)

    game.play_game()


if __name__ == "__main__":
    main()
