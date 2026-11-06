# Generate Numbers

Generate number-oriented text (with math operators) for practice on typing sites like MonkeyType


## Usage

```
$ uv run generate-numbers.py
30676 7,558 2.2^943.853 -9759320 -679 14 5301436 7 3 (797105) -02342 -0231 27.867 002554 459,180*7+(4106321) 54 -54489^5906 691,136 7 1 6647349 54006 1648879-3 97.48630-2016 60.31 090+024.479/712.2478 -30+829523 -6,217 (-8.1538) (0,147) 8.04*(-1,793,306) 4474*564129 (78,303) (6)+(596) -0736 493849 -78 5.02906
```

The text of numbers is automatically copied to the user's clipboard


## Installation

This project uses `uv` for Python dependency management

```
uv sync
```


## Configuration

Customize number generation via config variables in a user-created `settings.cfg` file

```
NUMBER_COUNT = 50
MAX_DIGIT_LENGTH = 7
MAX_CONSECUTIVE_OPERATIONS = 2
PERCENTAGE_DECIMAL_POINT = 25
PERCENTAGE_COMMAS = 30
PERCENTAGE_NEGATIVE = 20
PERCENTAGE_PARENTHESES = 20
PERCENTAGE_OPERATIONS = 30
```