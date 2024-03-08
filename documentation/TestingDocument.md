# Testing Document

## Unit Testing

Unit testing for this project is done using pytest. 

Tests were created for the AI and Board classes and all their methods, where applicable testing realistic game situations, e.g. wins and losses on the next move to check next_move and minimax work correctly, and various inputs (e.g. invalid columns for making moves in the Board class). The test files can be found in the tests directory, and each test is accompanied brief comments explaining its working.

The Game class was not unit tested, as it is a UI class. Instead, manual / end-to-end testing was used.

### Running unit tests and creating reports

Tests can be run using 

```bash
poetry run invoke test
```

The html test coverage report is created using:

```bash
poetry run invoke coverage-report
```

The coverage report can be viewed from index.html in htmlcov.

### Current test coverage

As of submitting the project on 08.03.24, testing coverage is 99% and there are 64 tests. All tests pass in 2.86 seconds. 

![Test Coverage Report](https://github.com/lenbie/Connect4AI/blob/main/documentation/coverage-report.png)

## Performance Testing

Performance testing of the AI class - the minimax algorithm and different optimizations - was done in the ai_perf_test.py file found in the src directory. A copy of the AI class was created, and different versions of next_move and minimax, representing the different optimizations were added. Running the file prints out the speed of running next_move at each of these optimization levels, starting from the same game state and with the same depth. The depth can be manually set at the bottom of the file.

Performance tests can also be run using:

```bash
poetry run invoke performance-test
```

This found that simple minimax was by far the slowest, then minimax with alpha-beta pruning, but no alpha updates in next_move, and minimax and next_move with alpha-beta pruning was even faster. 

Upon implementing iterative deepening without caching, the algorithm was slightly slower than the alpha-beta pruning implementation. This makes sense, due to the added overhead of depth increases. However, upon adding caching, the algorithm got significantly faster. The latter difference is clearly visible from depths from 5 and up. Below that, the overhead of iterative deepening and caching in Python seems to be slightly greater than the efficiency improvement, so alpha-beta pruning is slightly faster. The time limits set in iterative deepening of course change what depths the algorithm is able to reach, but I have found that it could play at depths up to and including 9 without exceeding a time limit of 5 seconds.

## Manual / End-to-end Testing

Manual tests have been done through running classes indpendently with scenarios I created (e.g. making moves and testing the response at a certain point in the game). Also, debugging print statements were used a lot, especially to verify the minimax algorithm returns the correct evaluation scores, specifically in win/loss situations upon the next move. Moreover, I played the game a lot for end-to-end testing, acting as both players to test the AI's responses, and game play itself. Also, faulty user inputs were tested to see the game's response worked correctly.

I also tried playing the AI against itself, to see whether the first player would always win, as it should in optimal game play. Since my AI cannot reach very high depths, it probably does not play ideally, but the first player did always win in my trials. 


## Code Quality Checks
Pylint was used for checking and improving code quality. As of 08.03.24, the code is rated 9.69/10.

The pylint report can be gotten using:

```bash
poetry run invoke lint
```