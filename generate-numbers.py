import random
import pyperclip
import constants


def generate_integer_string():
    num_len = random.randint(1, constants.MAX_DIGIT_LENGTH)
    num_str = ""

    for _ in range(num_len):
        num_str += str(random.randint(0, 9))

    return num_str

def format_integer_string_with_commas(num_str):
    formatted_num = ""

    for i in range(len(num_str)):
        formatted_num += num_str[len(num_str) - i - 1]

        if i < len(num_str) - 1 and (i + 1) % 3 == 0:
            formatted_num += ','

    return formatted_num[:: -1]

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
        decimal_index = num_str.find('.')

        if decimal_index > -1:
            num_str = format_integer_string_with_commas(num_str[:decimal_index]) + num_str[decimal_index:]

        else:
            num_str = format_integer_string_with_commas(num_str)

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
            ops_list = "-+/*^"
            num_str += ops_list[random.randint(0, len(ops_list) - 1)]
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
