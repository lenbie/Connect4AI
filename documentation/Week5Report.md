# Week 5 Report

This week, I tried to solve the previous issues with my minimax. 
This included changing the move ordering as instructed on moodle, so center column moves are evaluated first. This makes alpha-beta pruning more efficient.
I also added unit tests for this. Upon the recommendation of my peer reviewer, I also added constants into the AI class for the very large and small numbers.
I made the heuristic evaluation function player neutral, meaning it now basically returns score - opponent score, and the player is not needed as input anymore. This improved the outcome. I also changed the next_move and minimax function, so minimax now returns both the score and best move for the starting move set in next_move.

A few problems remain, which I will work on in the next days, before then implementing iterative deepending and caching, and increasing test coverage.

First, I think when I check for the win in minimax, it wrongly checks the win for the current player, when the win would be from the previous player. The scoring should be done accordingly. I tried to change this around, but could not get it to work properly. I am thinking that I may need to change the way I check for a win entirely, as discussed with Hannu. Then, this may become easier. Also, we discussed that for checking a draw, I could use a move count. However, this cannot be for the minimax only, as the move count encompasses the entire game - but this would again be the global variable board.move_count, which was not good practice. I could make a function that counts how many moves have been made, but this does not seem more efficient than checking if there are available moves, so I've stuck to that for now.

Beyond that, I spent time on the peer review this week, which was fun.

Hours spent: 8