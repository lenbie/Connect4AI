# Testing Document

## Unit Testing

Unit testing for this project is done using pytest. 

Tests can be run using 

```bash
poetry run invoke test
```

The html test coverage report is created using:

```bash
poetry run invoke coverage-report
```

The coverage report can be viewed from index.html in htmlcov.

*Upon recommendation of a peer reviwer, I am aiming to implement Codecov and add a badge displaying test coverage to the README of this repository* 

### Current test coverage

As of 24.02., there are 15 tests. More test for the AI class in particular, but also the Game class will be added ASAP. However, the Game class is partially a UI class, so unit testing is not always appropriate here. Instead, manual testing was used. All tests pass in 0.42 seconds. 

![Test Coverage Report](https://github.com/lenbie/Connect4AI/blob/main/documentation/CoverageReport.png)

## Performance Testing

Performance testing of the AI class - the minimax and different optimization - was done in the ai_perf_test.py file found in src. A copy of the AI class was created, and different versions of next_move and minimax, representing the different optimizations were added. Running the file prints out the speed of running next_move at each of these optimization levels, starting from the same game state and with the same depth. The depth can be manually set at the bottom of the file.

This found that simple minimax was by far the slowest, then minimax with alpha-beta pruning, but no alpha updates in next_move, and minimax and next_move with alpha-beta pruning was even faster. 

Upon implementing iterative deepening without caching, the algorithm was slightly slower than the alpha-beta pruning implementation. This makes sense, due to the added overhead of depth increases. However, upon adding caching, the algorithm got significantly faster. This applies to depths from 5 and up. Below that, the overhead of iterative deepening and caching in Python seems to be slightly greater than the efficiency improvement, so alpha-beta pruning is slightly faster.

## Manual Testing

Manual tests have been done through running classes indpendently with scenarios I created (e.g. making moves and testing the response at a certain point in the game). Also, debugging print statements were used a lot, especially to verify the minimax algorithm returns the correct evaluation scores, specifically in win/loss situations upon the next move. Moreover, I played the game a lot as both players to test the AI's responses, and game play itself.
