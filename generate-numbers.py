import random
import pyperclip
import constants

# Return string of integers
def generate_integer_string():
    digit_count = random.randint(constants.MIN_DIGIT_COUNT, constants.MAX_DIGIT_COUNT)
    return "".join(random.choices(constants.DIGITS, k=digit_count))

# Input number must be string of integers
def format_with_decimal_point(num_str):
    if len(num_str) < 2:
        return num_str
    
    decimal_index = random.randint(1, len(num_str) - 1)
    integer_part = num_str[:decimal_index]
    fractional_part = num_str[decimal_index:]

    return f"{integer_part}.{fractional_part}"

# Input number must be string of integers
def format_with_single_delimiter(num_str, single_delimiter, interval):
    if len(num_str) < interval + 1:
        return num_str
    
    tokens = []
    beg_index = len(num_str) % interval

    if beg_index > 0:
        tokens.append(num_str[:beg_index])

    while beg_index < len(num_str):
        tokens.append(num_str[beg_index : beg_index + interval])
        beg_index += interval

    return single_delimiter.join(tokens)

def format_with_paired_delimiter(num_str, paired_delimiter):
    return paired_delimiter[0] + num_str + paired_delimiter[1]

def generate_random_number_string():
    num_str = generate_integer_string()

    # Format with decimal point
    if random.randint(1, 100) <= constants.PERCENTAGE_DECIMAL_POINT:
        num_str = format_with_decimal_point(num_str)

    # Format with single delimiter
    if random.randint(1, 100) <= constants.PERCENTAGE_SINGLE_DELIMITER:
        integer_part = num_str
        fractional_part = ""
        decimal_index = num_str.find('.')

        if decimal_index > -1:
            integer_part = num_str[:decimal_index]
            fractional_part = num_str[decimal_index:]

        single_delimiter = random.choice(constants.SINGLE_DELIMITERS)
        interval = random.choice(constants.SINGLE_DELIMITERS_INTERVALS)
        num_str = format_with_single_delimiter(integer_part, single_delimiter, interval) + fractional_part

    # Prefix with negative sign
    if random.randint(1, 100) <= constants.PERCENTAGE_NEGATIVE_NUMBER:
        num_str = '-' + num_str

    # Prefix with unary operator
    if random.randint(1, 100) <= constants.PERCENTAGE_UNARY_OPERATOR:
        num_str = random.choice(constants.UNARY_OPERATORS) + num_str

    # Format with paired delimiter
    if random.randint(1, 100) <= constants.PERCENTAGE_PAIRED_DELIMITER:
        num_str = format_with_paired_delimiter(num_str, random.choice(constants.PAIRED_DELIMITERS))

    return num_str

def main():
    output_tokens = []

    for _ in range(constants.WORD_COUNT):
        token = generate_random_number_string()

        # Add binary operator
        if random.randint(1, 100) <= constants.PERCENTAGE_BINARY_OPERATOR:
            token += random.choice(constants.BINARY_OPERATORS) + generate_random_number_string()

        output_tokens.append(token)

    output = " ".join(output_tokens)
    print(output)
    pyperclip.copy(output)
    
if __name__ == "__main__":
    main()
