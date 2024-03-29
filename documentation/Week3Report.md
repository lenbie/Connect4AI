# Week 3 Report

This week, I began the implementation of the central algorithms. I implemented the Minimax algorithm, not yet with alpha-beta pruning. I realised that there are a lot of things to consider here, even if the algorithm seems simple at first. For example, I realised that it would be better to reward early wins and thus adjusted the return values accordingly.

I also created an initial attempt at a heuristic - the idea here was that I wanted to try representing the connect 4 board as a graph - specifically, the nodes of the graph are the tokens of a specified player, and there are edges between nodes if two of the player's tokens are next to each other on the game board. Then, I used the concept of the degree of a node - calculating the average node degree of the graph. The idea behind this is that the more connections there are in the graph - the higher node degrees, the more chances a player has of getting four tokens in a row. And if the opposing player has a graph of high average node degree, that worsens the current player's position. However, I am not yet sure if this heuristic works, I mainly wanted to start with some heuristic to get the game to work, and I can improve it later on.

I have not yet had the chance to write tests for the AI and Game classes. I also realized some mistakes in earlier code and tests, specifically the functions calculating if a move would lead to four connected tokens. I started considering how to revise these functions, and this will be my first task next week. This issue has led to some errors in the game play - the game does not finish when a win is achieved - but otherwise the game can be played. I decided to stick with playing it in the terminal. Starting the game asks the player if they would like to start or not, and then the AI and human take turns making moves. On each turn of the human, the program asks for further input on which move to make via terminal.

My main focus next week is improving the connect four functions, then testing for the minimax algorithm and other new classes. Next, I will add further optimizations, like alpha beta pruning.

Time spent: 8 hours
