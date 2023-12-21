import sys
from collections import deque


def parse():
    D = open(sys.argv[1]).read().strip().split('\n')
    return [[ch for ch in row] for row in D]


def solve_p1():
    grid = parse()
    start = (0, 0)
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'S':
                start = (r, c)
                grid[r][c] = '.'

    steps = {start}
    for i in range(0, 64):
        new_steps = set()
        for r, c in steps:
            for rr, cc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = r + rr
                nc = c + cc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == '.':
                        new_steps.add((nr, nc))

        steps = new_steps

    print('Part 1:', len(steps))


def solve_p2():
    grid = parse()
    R = len(grid)
    C = len(grid[0])
    start = (0, 0)
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'S':
                start = (r, c)
                grid[r][c] = '.'

    print(start)
    steps = {start}
    count = 0
    for i in range(0, 26501365):
        count = 0
        new_steps = set()
        for r, c in steps:
            for rr, cc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = r + rr
                nc = c + cc
                if grid[nr % R][nc % C] == '.':
                    new_steps.add((nr, nc))

        steps = new_steps

    # print(steps)
    print('Part 2:', len(steps))


# solve_p1()
solve_p2()
