import re
import utils

number_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def parse(puzzle_input):
    print(puzzle_input)
    return puzzle_input


# Part 1

def part1(lines):
    line_sum = 0

    for line in lines:
        numbers = re.findall(r'\d', line)
        line_sum += int(str(numbers[0]) + str(numbers[-1]))

    return line_sum


# Part 2
def part2(lines):
    pattern = r'(?=(\d|' + '|'.join(number_map.keys()) + '))'
    calibration_sum = 0

    for line in lines:
        numbers = re.findall(pattern, line)
        num = get_number_at_position(numbers, 0) + get_number_at_position(numbers, -1)
        calibration_sum += int(num)

    return calibration_sum


def get_number_at_position(arr, pos):
    item = arr[pos]

    if item.isdigit():
        return item
    else:
        for word, number in number_map.items():
            item = item.replace(word, number)
        return item


print(part1(utils.parse_single_string('input.txt')))
print(part2(utils.parse_single_string('input.txt')))
