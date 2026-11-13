import random
import pyperclip
import constants

# Return string of integers
def generate_integer_string():
    num_len = random.randint(1, constants.MAX_DIGIT_LENGTH)
    
    return "".join([str(random.randint(0, 9)) for _ in range(num_len)])

# Input number must be string of integers
def format_with_decimal_point(num_str):
    if len(num_str) < 2:
        return num_str
    
    decimal_index = random.randint(1, len(num_str) - 1)
    beg_str = num_str[:decimal_index]
    end_str = num_str[decimal_index:]

    return f"{beg_str}.{end_str}"

# Input number must be string of integers
def format_with_single_delimiter(num_str, single_delimiter):
    if len(num_str) < 4:
        return num_str
    
    tokens = []
    beg_index = len(num_str) % 3

    if beg_index > 0:
        tokens.append(num_str[:beg_index])

    while beg_index < len(num_str):
        tokens.append(num_str[beg_index : beg_index + 3])
        beg_index += 3

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
        decimal_index = num_str.find('.')
        beg_str = ""
        end_str = ""

        if decimal_index > -1:
            beg_str = num_str[:decimal_index]
            end_str = num_str[decimal_index:]

        else:
            beg_str = num_str

        num_str = format_with_single_delimiter(beg_str, random.choice(constants.SINGLE_DELIMITERS)) + end_str

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
