# Week 2 Report

Upon the advice of the course instructor, I switched to doing my project in Python. Hence, I changed the repository to be a Python project. I also set up
Poetry for managing dependencies. I implemented the game board (Board class), which allows making valid moves and checks for wins. I was also researching some more about how to make the AI, and discovered that bitboards might be a more efficient representation for the game board when using iterative deepending and caching later on, as recommended by the course instructor. I however decided to start with a simple game board using 2d arrays, so I can finish setting up a basic implementation of the Minimax algorithm and the game soon. So far, it is possible to make moves using the console and see the outcome and if a player wins, but it is not a 2 player game yet.

I also started thinking about how to set up the rest of the game. The next step will be to create a simple UI using Pygame, which I started learning about this week as well. Then, I will know how exactly the game loop is managed and the player input is got, and then I can bring the player input, the AI moves and the board together in a Game class to manage the game play. Also, I aim to implement a basic version of the Minimax algorithm, so the game can be played to some extent, before improving upon the AI in later weeks.

I also set up pytest for testing, and wrote tests for the Board class. I also made docstring documentation for the implemented class, and I set up pylint for code quality checks. I also created tasks, so it is possible to get test and code quality reports using the command line, although this may not work yet for someone else downloading the project, but it will in future weeks.

Time spent: 7 hours