# Generate Numbers

Generate number-oriented text (with unary and binary operators) for practice on typing sites like MonkeyType


## Usage

```
$ uv run generate-numbers.py
-13840 -7881627==\6.943\ 14.91573^988854 /@559/+19426 ~537|771 6814 &509 *8256*0.56 {982} /++-9424/ &3&&8 \55999\!=@-9.741 (-58.97066) &4 \68.784\ [8] 657.6 473245 _3634_ 325660!=5337135 @76751 $93.3503--5 @51721<<`&404` !21/852.706 [~66.28]%--3.626 --161 -39|/6.9/ _1_>>15731 \!6\ `9` *7.411 ++10.089 (@-3242984) 10|766 1_109 {-3.7} #7139870 \*766\ 424655 84.79 210.8&&~-402079 @767463.0 /43.16/ 5.422<</$10/ 59 (107447) /-5:953:215/ (543) /&40_003/ {63.907}
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
MAX_DIGIT_LENGTH=7

PERCENTAGE_NEGATIVE_NUMBER=20
PERCENTAGE_DECIMAL_POINT=25

PERCENTAGE_SINGLE_DELIMITER=30
PERCENTAGE_PAIRED_DELIMITER=30
PERCENTAGE_UNARY_OPERATOR=30
PERCENTAGE_BINARY_OPERATOR=30

SINGLE_DELIMITERS=,._:
PAIRED_DELIMITERS=(),[],{},\\,//,``,__
UNARY_OPERATORS=@,#,$,++,--,!,~,&,*
BINARY_OPERATORS=+,-,*,/,%,&,|,^,<<,>>,&&,||,==,!=,>,<,>=,<=
```