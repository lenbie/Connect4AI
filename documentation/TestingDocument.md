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


## Manual Testing

Manual tests have been done through running classes indpendently with scenarios I created (e.g. making moves and testing the response at a certain point in the game). Also, debugging print statements were used a lot, especially to verify the minimax algorithm returns the correct evaluation scores, specifically in win/loss situations upon the next move. Moreover, I played the game a lot as both players to test the AI's responses, and game play itself.
