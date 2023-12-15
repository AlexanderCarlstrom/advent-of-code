import sys
import re
from collections import defaultdict

# MAIN STUFF

D = open(sys.argv[1]).read().strip()


def solve_p1():
    instructions = D.split(',')

    sum_ascii = 0
    for ins in instructions:
        current = 0
        for ch in ins:
            value = ord(ch)
            current += value
            current *= 17
            current = current % 256

        sum_ascii += current

    print('Part 1:', sum_ascii)


def solve_p2():
    instructions = D.split(',')

    boxes = []
    for i in range(0, 256):
        boxes.append(defaultdict(int))
    for ins in instructions:
        chars, sep, v = re.search(r'([a-z]+)([=\-])(\d*)', ins).groups()
        box = 0

        for ch in chars:
            box += ord(ch)
            box *= 17
            box = box % 256

        if sep == '-':
            if chars in boxes[box]:
                del boxes[box][chars]
        elif sep == '=':
            if boxes[box][chars]:
                boxes[box][chars] = int(v)
            else:
                boxes[box][chars] = int(v)

    power = 0
    for i, box in enumerate(boxes):
        if len(box) > 0:
            for j, lens in enumerate(box.items()):
                power += (i + 1) * (j + 1) * lens[1]

    print('Part 2:', power)


solve_p1()
solve_p2()