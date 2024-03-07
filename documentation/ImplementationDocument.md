# Implementation Document

## Program Structure

The program is divided into four main classes, AI, Game, Board and Main. Main is called to start the game, and then calls the Game class. This class handles the actual game play by the user. It gets inputs through the command line, handles the start of the game (player choice), consecutive move-making by the human and AI player, and win and draw situation, i.e. printing corresponding messages and giving the option to play again. The AI class is responsible for finding the moves for the AI player to make. It does so using the minimax algorithm with alpha beta pruning and soon also iterative deepening and caching and a heuristic evaluation function. The Board class handles everything to do with the actual game board -- making moves onto the board, checking for valid moves and wins.

## Time and Space Complexities achieved

*From theory (not evaluated yet specific to this project):*
- *Time complexity of Minimax: O(b^m) b = branching factor of treee, m = maximum depth of tree*
- *Space complexity of Minimax: O(bm)*
- *Time complexity of Minimax with Alpha-beta pruning: worst case O(b^m), ideally O(b^(m/2))*
- *Space complexity of Minimax with Alpha-beta pruning: (bm)*

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