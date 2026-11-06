import random
import pyperclip
import constants


def generate_integer_string():
    num_len = random.randint(1, constants.MAX_DIGIT_LENGTH)
    num_str = ""

    for _ in range(num_len):
        num_str += str(random.randint(0, 9))

    return num_str

def generate_random_number_string():
    num_str = generate_integer_string()

    # Insert decimal point
    if len(num_str) > 1 and random.randint(1, 100) <= constants.PERCENTAGE_DECIMAL_POINT:
        decimal_index = random.randint(0, len(num_str) - 2)

        beg_str = num_str[:decimal_index + 1]
        end_str = num_str[decimal_index + 1:]
        num_str = f"{beg_str}.{end_str}"

    # Format with commas
    if len(num_str) > 3 and random.randint(1, 100) <= constants.PERCENTAGE_COMMAS:
        parse_number = int
        decimal_index = num_str.find('.')

        if decimal_index > -1:
            parse_number = float

        num_str = f"{parse_number(num_str):,}"

    # Add negative sign
    if random.randint(1, 100) <= constants.PERCENTAGE_NEGATIVE:
        num_str = '-' + num_str

    return num_str

def main():
    consecutive_ops_count = 0
    output = ""

    for _ in range(constants.NUMBER_COUNT):
        num_str = generate_random_number_string()

        # Add parentheses
        if random.randint(1, 100) <= constants.PERCENTAGE_PARENTHESES:
            num_str = f"({num_str})"

        # Add math operators
        if consecutive_ops_count < constants.MAX_CONSECUTIVE_OPERATIONS and random.randint(1, 100) <= constants.PERCENTAGE_OPERATIONS:
            num_str += random.choice("-+/*^")
            consecutive_ops_count += 1

        else:
            num_str += ' '
            consecutive_ops_count = 0

        output += num_str

    output = output[:-1]
    print(output)
    pyperclip.copy(output)
    
if __name__ == "__main__":
    main()
