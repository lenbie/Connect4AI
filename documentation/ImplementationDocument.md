# Implementation Document

## Program Structure

The program is divided into four main classes, AI, Game, Board and Main. Main is called to start the game, and then calls the Game class. This class is the UI class and handles the actual game play by the user. It gets inputs through the command line, handles displaying the game board, the start of the game (player choice), consecutive move-making by the human and AI player, and win and draw situation, i.e. printing corresponding messages and giving the option to play again. The AI class is responsible for finding the moves for the AI player to make. It does so using the minimax algorithm with alpha beta pruning and soon also iterative deepening and caching and a heuristic evaluation function. The Board class handles everything to do with the actual game board -- making moves onto the board, checking for valid moves and wins.

## Time and Space Complexities achieved

The theoretical time and space complexities of minimax and alpha beta pruning are as follows:
- Time complexity of Minimax: O(b^m) b = branching factor of tree, m = maximum depth of tree
- Time complexity of Minimax with Alpha-beta pruning: worst case O(b^m), ideally O(b^(m/2))
- Space complexity of Minimax = O(bm)

- Looking at my connect 4 game, the branching factor is at most 7 (number of columns), and the maximum depth is the max depth of the iterative deepening and minimax, set in the AI class.
- Since I have the added optimizations for alpha-beta pruning of iterative deepening and caching, and the optimized move ordering focusing on the centre columns, the time complexity of my algorithm likely lies between the worst case of O(b^m), which is the same as the simple minimax, and the ideal case of O(b^(m/2)). My algorithm is not optimized enough to achieve this lower bound, but it is more optimized compared to simple minimax, hence, it sits in between.
- Space complexity also likely does not differ much from the theory - while pruning branches should reduce the needed space, caching uses additional space. The exact space complexity depends on how much is pruned, and how much space the cache takes. Since I am able to use the Python dictionary as a cache, the needed space is moderate, but my caching is also not optimized (see below).

## Shortcomings and Suggested Improvements

- Further optimizations of caching are possible, to provide narrower boundaries for alpha-beta pruning and thus speed up the algorithm even more.
- Instead of representing the game board as a 2d array, bitboards could be used for a more compact and efficient storage structure, which then could also be used to optimize the cache data structure and operations.
- Other data structure operations could also be implemented more efficiently, e.g. removing the best move from an array and moving it to the front of the list could be done more efficiently.
- The heuristic could be refined further for even more accurate game play.
- Python is not the most efficient programming language, so this inherently leads the program to be less efficient that it could be.
- A graphical UI, e.g. using Pygame, would be nicer for playing the game.

## Use of LLMs

This project used ChatGPT for general research, e.g. to understand the algorithms used, and to help find the best ways to code certain things in Python specifically, e.g. how to format the game board printout to the command line.

## References

https://en.wikipedia.org/wiki/Connect_Four 
https://en.wikipedia.org/wiki/Minimax
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
https://www.javatpoint.com/mini-max-algorithm-in-ai
https://www.javatpoint.com/ai-alpha-beta-pruning
https://www.mygreatlearning.com/blog/alpha-beta-pruning-in-ai/
http://blog.gamesolver.org/solving-connect-four/