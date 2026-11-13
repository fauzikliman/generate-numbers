import configparser

cfg = configparser.ConfigParser(allow_unnamed_section=True, interpolation=None)
cfg.read("settings.cfg")

def cfg_get_int(variable_name, default_value):
    return cfg.getint(configparser.UNNAMED_SECTION, variable_name, fallback=default_value)

def cfg_get_string(variable_name, default_name):
    return cfg.get(configparser.UNNAMED_SECTION, variable_name, fallback=default_name)

WORD_COUNT = cfg_get_int("WORD_COUNT", 50)
MAX_DIGIT_LENGTH = cfg_get_int("MAX_DIGIT_LENGTH", 7)

PERCENTAGE_NEGATIVE_NUMBER = cfg_get_int("PERCENTAGE_NEGATIVE_NUMBER", 20)
PERCENTAGE_DECIMAL_POINT = cfg_get_int("PERCENTAGE_DECIMAL_POINT", 25)

PERCENTAGE_SINGLE_DELIMITER = cfg_get_int("PERCENTAGE_SINGLE_DELIMITER", 30)
PERCENTAGE_PAIRED_DELIMITER = cfg_get_int("PERCENTAGE_PAIRED_DELIMITER", 30)
PERCENTAGE_UNARY_OPERATOR = cfg_get_int("PERCENTAGE_UNARY_OPERATOR", 30)
PERCENTAGE_BINARY_OPERATOR = cfg_get_int("PERCENTAGE_BINARY_OPERATOR", 30)

SINGLE_DELIMITERS = cfg_get_string("SINGLE_DELIMITERS", ",._:")
PAIRED_DELIMITERS = cfg_get_string("PAIRED_DELIMITERS", "(),[],{},\\,//,``,__").split(",")
UNARY_OPERATORS = cfg_get_string("UNARY_OPERATORS", "@,#,$,++,--,!,~,&,*").split(",")
BINARY_OPERATORS = cfg_get_string("BINARY_OPERATORS", "+,-,*,/,%,&,|,^,<<,>>,&&,||,==,!=,>,<,>=,<=").split(",")
