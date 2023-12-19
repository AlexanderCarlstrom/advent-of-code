import sys
from shapely import Polygon, area

G = open(sys.argv[1]).read().strip().split('\n')


def solve_p1():
    instructions = []
    for line in G:
        direction, length, _ = line.split(' ')
        instructions.append(tuple([direction, int(length)]))

    current = (0, 0)
    coords = [current]
    meters = 0
    for inst in instructions:
        direction, length = inst
        r, c = current
        if direction == 'U':
            r -= length
        elif direction == 'D':
            r += length
        elif direction == 'L':
            c -= length
        elif direction == 'R':
            c += length

        meters += length

        current = (r, c)
        coords.append((r, c))

    meters = meters // 2 + 1
    meters += area(Polygon(coords))
    print('Part 1:', meters)


def solve_p2():
    instructions = []
    directions = ['R', 'D', 'L', 'U']
    for line in G:
        parts = line.split(' ')
        instructions.append((directions[int(parts[2][-2])], int(parts[2][2:-2], 16)))

    current = (0, 0)
    coords = [current]
    trench_area = 0
    for inst in instructions:
        direction, length = inst
        r, c = current
        if direction == 'U':
            r -= length
        elif direction == 'D':
            r += length
        elif direction == 'L':
            c -= length
        elif direction == 'R':
            c += length

        trench_area += length

        current = (r, c)
        coords.append((r, c))

    trench_area = trench_area // 2 + 1
    trench_area += area(Polygon(coords))
    print('Part 2:', trench_area)


solve_p1()
solve_p2()
