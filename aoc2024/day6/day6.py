import sys
import re
import math

def get_next(pos):
    x, y, dir = pos
    if dir == 'N':
        return (x - 1, y, dir)
    if dir == 'E':
        return (x, y + 1, dir)
    if dir == 'S':
        return (x + 1, y, dir)
    if dir == 'W':
        return (x, y - 1, dir)


def turn_right(pos):
    x, y, dir = pos
    if dir == 'N':
        return (x + 1, y + 1, 'E')
    if dir == 'E':
        return (x + 1, y - 1, 'S')
    if dir == 'S':
        return (x - 1, y - 1, 'W')
    if dir == 'W':
        return (x - 1, y + 1, 'N')


def solve_p1():
    D = open(sys.argv[1]).read().strip().split('\n')
    guard = (0, 0, 'N')
    trail = set()

    for x, line in enumerate(D):
        if '^' in line:
            y = line.index('^')
            guard = (x, y, 'N')

    while True:
        x, y, dir = guard
        trail.add((x, y))

        guard = get_next(guard)

        if guard[0] < 0 or guard[0] >= len(D) or guard[1] < 0 or guard[1] >= len(D[0]):
            break

        if D[guard[0]][guard[1]] == '#':
            guard = turn_right(guard)

    return len(trail)

def is_loop(x, y, dir, obstacles):
    if dir == 'N':
        return ((x, y), next((pos for pos in obstacles if pos[0] > x and pos[1] == y - 1), None), next((pos for pos in obstacles if pos[0] == x + 1 and pos[1] > y), None))
    if dir == 'E':
        return ((x, y), next((pos for pos in obstacles if pos[0] == x - 1 and pos[1] < y), None), next((pos for pos in obstacles if pos[0] > x and pos[1] == y - 1), None))
    if dir == 'S':
        return ((x, y), next((pos for pos in obstacles if pos[0] < x and pos[1] == y + 1), None), next((pos for pos in obstacles if pos[0] == x - 1 and pos[1] < y), None))
    if dir == 'W':
        return ((x, y), next((pos for pos in obstacles if pos[0] == x + 1 and pos[1] > y), None), next((pos for pos in obstacles if pos[0] < x and pos[1] == y + 1), None))


def calc_vertex(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    x4 = x1 + x2 + x3 - (2 * (x1 + x2 + x3) / 3)
    y4 = y1 + y2 + y3 - (2 * (y1 + y2 + y3) / 3)

    return (x4, y4)
    # 0 + 1 + 7 - (2 * (0 + 1 + 7) / 3)
    # 4 + 9 + 8 - (2 * (4 + 9 + 8) / 3)


def loops(grid, r, c):
    seen = set()
    dr = -1
    dc = 0
    while True:
        seen.add((r, c, dr, dc))
        rr = r + dr
        cc = c + dc
        if rr < 0 or rr >= len(grid) or cc < 0 or cc >= len(grid[0]):
            return False

        if grid[rr][cc] == '#':
            dc, dr = -dr, dc
        else:
            r = rr
            c = cc

        if (r, c, dr, dc) in seen:
            return True


def solve_p2():
    D = open(sys.argv[1]).read().strip().split('\n')
    grid = [list(row) for row in D]
    rows = len(grid)
    cols = len(grid[0])

    for sr in range(rows):
        for sc in range(cols):
            if grid[sr][sc] == '^':
                break
        else:
            continue
        break

    loop_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                continue

            grid[r][c] = '#'
            if loops(grid, sr, sc):
                loop_count += 1
            grid[r][c] = '.'


    return loop_count

print('Part 1:', solve_p1())
print('Part 2:', solve_p2())
