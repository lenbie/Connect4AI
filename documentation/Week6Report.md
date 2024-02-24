# Week 6 Report

- game move count implemented as suggested on labtool
- if col full, it doestn ask u to put again - fixed 
- fixed winning in minimax at least manual testing it performs well, gotta add unit tests still
- didnt need to rewrite connect 4 checker, could still do it for efficiency but it wasnt the problem
- updating alpha in next move was an issue, and also the player turns - since next move is kinda first iteration of minimax, needs to call the minimizing player first, and then also player one was maximising by default, and now it was changed to use the self._ai_player and then check if its that players turn, which means its maximizing 
- fixed that the correct player number of the winner is shown again, since connect 4 now checks for a win in general, and not for a specific person
- now, draw should lead to play again - _check_draw function added, and play again turned into own function -also gotta write tests for this

TO DO
- update UI with the coloured emojis
- add iterative deepening and caching
- add documentation

