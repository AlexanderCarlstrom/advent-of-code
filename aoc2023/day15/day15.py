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
        boxes.append(defaultdict(list))
    for ins in instructions:
        chars, sep, v = re.search(r'([a-z]+)([=\-])(\d*)', ins).groups()
        box = 0
        print(chars, sep, v)

        for ch in chars:
            box += ord(ch)
            box *= 17
            box = box % 256

        if sep == '-':
            print('del', box)
            if boxes[box][chars]:
                del boxes[box][chars]
        elif sep == '=':
            print('add', box)
            if boxes[box][chars]:
                boxes[box][chars][0] = int(v)
            else:
                boxes[box][chars] = [int(v), len(boxes[box])]

    power = 0
    for i, box in enumerate(boxes):
        if len(box) > 0:
            items = sorted(box.items(), key=lambda item: item[1])
            print(items)
            for j, lens in enumerate(items):
                power += (i + 1) * (j + 1) * lens[1][0]

    print('Part 2:', power)


solve_p2()