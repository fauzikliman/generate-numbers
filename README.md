# Generate Numbers

Generate number-oriented text (with unary and binary operators) for practice on typing sites like MonkeyType


## Usage

```
$ uv run generate-numbers.py
/@5374/ 242.0/4981 9326 [7.2]%878154 @-01_491 -36>>_1_892_ \194337\ 31 \@5629\ 01||{6040.587} {!-9:297:285} 00.440 916:300.1 ---04.33.25 4128&199 [36418] [77:05:19] 00.882.3 [--2401644] 111.914|`-160219.5` &8:141 -895566 3_63+65 $222563+(793136) 3538950<=2714358 [96109] 4.4 2.905 367010 0482>>{1527} -35.94%[77105] _030195_ /38/ -40765 6408 (614) {@2468} 10371 _65.0_ 020 *0693 (339:341) /++1.5/-_-225686_ 1,77,36,16 ~44.47980 227768 8800 6335 -3879 (9.4)
```

The command output is automatically copied to the user's clipboard


## Installation

This project uses `uv` for Python dependency management

```
uv sync
```


## Configuration

Customize text generation via config variables in a user-created `settings.cfg` file

```
WORD_COUNT=50
MIN_DIGIT_COUNT=2
MAX_DIGIT_COUNT=7

PERCENTAGE_NEGATIVE_NUMBER=20
PERCENTAGE_DECIMAL_POINT=25

PERCENTAGE_SINGLE_DELIMITER=30
PERCENTAGE_PAIRED_DELIMITER=30
PERCENTAGE_UNARY_OPERATOR=30
PERCENTAGE_BINARY_OPERATOR=30

DIGITS=0123456789
SINGLE_DELIMITERS=,._:
SINGLE_DELIMITERS_INTERVALS=2,3
PAIRED_DELIMITERS=(),[],{},\\,//,``,__
UNARY_OPERATORS=@,#,$,++,--,!,~,&,*
BINARY_OPERATORS=+,-,*,/,%,&,|,^,<<,>>,&&,||,==,!=,>,<,>=,<=
```