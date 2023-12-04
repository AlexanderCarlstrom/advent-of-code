import re

import utils


def part1(data):
    numbers = []
    for row, line in enumerate(data):
        indices = re.finditer(r'\d+', line)
        for m in indices:
            if is_part_number(row, m.start(), m.end(), data):
                numbers.append(int(m.group()))

    return sum(numbers)


def is_part_number(row, s, e, data):
    start = max(s - 1, 0)
    end = min(e + 1, len(data[0]) - 1)
    pattern = re.compile(r'[^\d.]')
    for line_index in range(max(row - 1, 0), min(row + 1, len(data) - 1) + 1):
        if pattern.search(data[line_index][start:end]):
            return True

    return False


def part2(data):
    numbers = []
    gears = []
    for row, line in enumerate(data):
        line_nums = re.finditer(r'\d+', line)
        for m in line_nums:
            numbers.append(Num(m.group(), m.start(), m.end() - 1, row))

        line_gears = re.finditer(r'\*', line)
        for m in line_gears:
            gears.append(Gear(m.start(), row))

    gear_sum = 0
    for gear in gears:
        gear_nums = get_gear_parts(gear, data, numbers)
        if len(gear_nums) == 2:
            gear_sum += gear_nums[0] * gear_nums[1]

    return gear_sum


def get_gear_parts(gear, data, numbers):
    row_range = [max(gear.row - 1, 0), min(gear.row + 1, len(data) - 1)]
    index_range = [max(gear.index - 1, 0), min(gear.index + 1, len(data[0]) - 1)]

    nums = list(filter(lambda num: row_range[0] <= num.row <= row_range[1], numbers))
    nums = list(filter(lambda num: num.start <= index_range[1] and num.end >= index_range[0], nums))
    return [int(num.number) for num in nums]


class Num:
    def __init__(self, number, start, end, row):
        self.number = number
        self.start = start
        self.end = end
        self.row = row


class Gear:
    def __init__(self, index, row):
        self.index = index
        self.row = row


print('Part 1: ' + str(part1(utils.parse_single_string('input.txt'))))
# print(part1(['467..114..', '...*......']))
print('Part 2: ' + str(part2(utils.parse_single_string('input.txt'))))
