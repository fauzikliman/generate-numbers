import configparser

cfg = configparser.ConfigParser(allow_unnamed_section=True)
cfg.read("settings.cfg")

def cfg_get_int(variable_name, default_value):
    return cfg.getint(configparser.UNNAMED_SECTION, variable_name, fallback=default_value)

NUMBER_COUNT = cfg_get_int("NUMBER_COUNT", 50)
MAX_DIGIT_LENGTH = cfg_get_int("MAX_DIGIT_LENGTH", 7)
MAX_CONSECUTIVE_OPERATIONS = cfg_get_int("MAX_CONSECUTIVE_OPERATIONS", 2)
PERCENTAGE_DECIMAL_POINT = cfg_get_int("PERCENTAGE_DECIMAL_POINT", 25)
PERCENTAGE_COMMAS = cfg_get_int("PERCENTAGE_COMMAS", 30)
PERCENTAGE_NEGATIVE = cfg_get_int("PERCENTAGE_NEGATIVE", 20)
PERCENTAGE_PARENTHESES = cfg_get_int("PERCENTAGE_PARENTHESES", 20)
PERCENTAGE_OPERATIONS = cfg_get_int("PERCENTAGE_OPERATIONS", 30)
