import sys
import re
import math


def solve_p1():
    D = open(sys.argv[1]).read().strip()
    results = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', D)

    return sum([math.prod([int(num) for num in nums]) for nums in results])


def solve_p2():
    D = open(sys.argv[1]).read().strip()
    results = re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)', D)
    results = [list(filter(None, result)) for result in results]

    enabled = True
    sum = 0
    for result in results:
        if len(result) == 1:
            if result[0] == 'do()':
                enabled = True
            elif result[0] == 'don\'t()':
                enabled = False
        elif enabled == True:
            sum += math.prod(list(map(int, result)))

    return sum


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())
