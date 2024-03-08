# User Manual

## Starting the game
You can start the project as instructed in README using poetry, or you can run main.py.

First, you are asked:

> Do you want to play as Player 1 🟡 or Player 2 🔴?

> Please enter 1 for 🟡, or 2 for 🔴

If you want to go first, you should input the number 1 and press Enter, otherwise enter 2 and press Enter. The AI will play as the other player.

## Making moves

Throughout the game, you will be prompted to choose a column to make a move into when it is your turn. You do this by entering numbers when prompted. The numbering goes from left to right, from 0 to 6. Imagine playing real connect 4 - if you choose a column, your token will be dropped into that column from the top. It will land in the lowest possible free slot - if the column is empty, your token will be at the bottom. If the column is full, you will be asked to choose a different one.

Consecutive moves are made until there is a win or a draw. After each move from you or the AI, the game board is always printed.

## Game End

The game ends if you or the AI has won, or there is a draw. A corresponding message will be printed. You are then asked if you would like to play again. If yes, type YES and press enter. If not, type anything else or simply close the terminal.

**Have fun!**