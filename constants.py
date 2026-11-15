import configparser

cfg = configparser.ConfigParser(allow_unnamed_section=True, interpolation=None)
cfg.read("settings.cfg")

def cfg_get_int(variable_name, default_value):
    return cfg.getint(configparser.UNNAMED_SECTION, variable_name, fallback=default_value)

def cfg_get_string(variable_name, default_name):
    return cfg.get(configparser.UNNAMED_SECTION, variable_name, fallback=default_name)

def to_int_list(comma_separated_string):
    string_list = comma_separated_string.split(",")
    return [int(string) for string in string_list]

WORD_COUNT = cfg_get_int("WORD_COUNT", 50)
MAX_DIGIT_COUNT = cfg_get_int("MAX_DIGIT_COUNT", 7)

PERCENTAGE_NEGATIVE_NUMBER = cfg_get_int("PERCENTAGE_NEGATIVE_NUMBER", 20)
PERCENTAGE_DECIMAL_POINT = cfg_get_int("PERCENTAGE_DECIMAL_POINT", 25)

PERCENTAGE_SINGLE_DELIMITER = cfg_get_int("PERCENTAGE_SINGLE_DELIMITER", 30)
PERCENTAGE_PAIRED_DELIMITER = cfg_get_int("PERCENTAGE_PAIRED_DELIMITER", 30)
PERCENTAGE_UNARY_OPERATOR = cfg_get_int("PERCENTAGE_UNARY_OPERATOR", 30)
PERCENTAGE_BINARY_OPERATOR = cfg_get_int("PERCENTAGE_BINARY_OPERATOR", 30)

DIGITS = cfg_get_string("DIGITS", "0123456789")
SINGLE_DELIMITERS = cfg_get_string("SINGLE_DELIMITERS", ",._:")
SINGLE_DELIMITERS_INTERVALS = to_int_list(cfg_get_string("SINGLE_DELIMITERS_INTERVALS", "2,3"))
PAIRED_DELIMITERS = cfg_get_string("PAIRED_DELIMITERS", "(),[],{},\\,//,``,__").split(",")
UNARY_OPERATORS = cfg_get_string("UNARY_OPERATORS", "@,#,$,++,--,!,~,&,*").split(",")
BINARY_OPERATORS = cfg_get_string("BINARY_OPERATORS", "+,-,*,/,%,&,|,^,<<,>>,&&,||,==,!=,>,<,>=,<=").split(",")
