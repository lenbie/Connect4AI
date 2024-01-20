# Project Specification

Degree Programme: BSc
Project language: English

This project aims to create a Connect4 game and bot, against which a human player can play.

The project will be done in Java.

## Data Structures and Algorithms

The central algorithm used in this project is the Minimax algorithm with Alpha-beta pruning. This is a very suitable algorithm for turn-based two-player games like Connect4. While Connect4 has been solved, Alpha-beta pruning is used to make the bot more efficient, by reducing the number of nodes in the game tree which the Minimax algorithm evaluates.

Time complexity of Minimax: O(b^m) b = branching factor of treee, m = maximum depth of tree
Space complexity of Minimax: O(bm)
Time complexity of Minimax with Alpha-beta pruning: worst case O(b^m), ideally O(b^(m/2))
Space complexity of Minimax with Alpha-beta pruning: (bm)

A datastructure that will be used for representing the six-row, seven-column game grid is a matrix / 2-d array.

## Program Input
The program has a UI for the human player to interact with. Upon the player choosing to start the game, either the player or the AI will start, depending on the player's choice. When it is the player's turn, they can then input their move - drop a token into a column of the grid into the lowest possible free square. Upon the game's end, the player can choose to play again. The player can also terminate the game at any point.


## Sources
https://en.wikipedia.org/wiki/Connect_Four 
https://www.javatpoint.com/mini-max-algorithm-in-ai
https://www.javatpoint.com/ai-alpha-beta-pruning
https://www.mygreatlearning.com/blog/alpha-beta-pruning-in-ai/

