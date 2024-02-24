# Connect4AI

*This project is part of the Algorithms and AI Lab course at the University of Helsinki*

## Documentation

[Project Specification](https://github.com/lenbie/Connect4AI/blob/main/documentation/ProjectSpecification.md)

### Weekly Reports

[Week 1 Report](https://github.com/lenbie/Connect4AI/blob/main/documentation/Week1Report.md)

[Week 2 Report](https://github.com/lenbie/Connect4AI/blob/main/documentation/Week2Report.md)

[Week 3 Report](https://github.com/lenbie/Connect4AI/blob/main/documentation/Week3Report.md)

[Week 4 Report](https://github.com/lenbie/Connect4AI/blob/main/documentation/Week4Report.md)

## Running the project

Note that Python version 3.10.12 was used for creating and testing this project.

## How to Play

The game is currently played via command line. Follow the steps below to install the project and start the game.
Then, enter inputs as prompted in the terminal. Columns are indexed from 0 (very left) to 6 (very right). Happy playing!

# Installation

1. Install dependencies through command line using:

```bash
poetry install
```

2. Start the game using: 

```bash
poetry run invoke start
```

## Command Line Functions

### Testing

Run tests using:

```bash
poetry run invoke test
```

### Test Coverage Report

Create the html test coverage report using:

```bash
poetry run invoke coverage-report
```

The coverage report can be viewed from index.html in htmlcov.

### Pylint tests

Create the pylint test report using:

```bash
poetry run invoke lint
```
