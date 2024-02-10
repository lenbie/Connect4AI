# Week 4 Report

This week, I focused on improving my game and AI. First, I made changes to the Board class in order for it to be properly checked, if a player has won.
I also updated the Game class, so now the game can be properly played, and played again, etc. 
I added docstring documentation for all classes.
I realised my old heuristic function was always evaluating both players positions as equal, especially at first, so I made a new heuristic evaluation
function. It is still quite simple and I want to keep improving it, but it already gives better results.
I also worked on fixing some bugs with the minimax and next_move functions in the AI class.
I further added alpha beta pruning to the minimax function.
Next, I started writing tests for the AI function, starting with scenarios and seeing if the move evaluation works correctly.
I will continue on this next week. The first of the tests now fails after the bug fixes I made to the AI class, 
so the first move the AI wants to make as player 1 is column 2, rather than column 3 as it should be.
I'm not sure why this mistake is being made, so clearly there is some further improvement and bug fixing to do before
I can work on improving efficiency of my AI. Also, the AI does not always prevent the human player from making winning moves, 
so I am wondering if there is something wrong with the minimax function, or where the mistake lies. I was struggling to work on this more
this week, as I got sick, but I will do this next week. Maybe the peer review can also give me some insight.


Hours spent: 10