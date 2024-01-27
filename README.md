# Connect4AI

*This project is part of the Algorithms and AI Lab course at the University of Helsinki*

## Documentation

[Project Specification](https://github.com/lenbie/Connect4AI/blob/main/documentation/ProjectSpecification.md)

### Weekly Reports

[Week 1 Report](https://github.com/lenbie/Connect4AI/blob/main/documentation/Week1Report.md)


## Running the project

Note that Python version 3.10.12 was used for creating and testing this project.


## Installation

1. Install dependencies through command line using:

```bash
poetry install
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

### Pylint tests

Create the pylint test report using:

```bash
poetry run invoke lint
```