import sys
from collections import deque, defaultdict


def parse():
    D = open(sys.argv[1]).read().strip().split('\n')
    grid = [[ch for ch in row] for row in D]

    return grid


def solve_p1():
    grid = parse()
    R = len(grid)
    C = len(grid[0])

    q = deque([(0, 1, [])])
    longest = 0
    while q:
        r, c, path = q.popleft()

        if (r, c) in path:
            continue

        if r < 0 or r >= R or c < 0 or c >= C:
            continue

        if grid[r][c] == '#':
            continue

        if (r, c) == (R - 1, C - 2):
            longest = max(longest, len(path))

        for ch, nr, nc in [('v', r + 1, c), ('>', r, c + 1), ('^', r - 1, c), ('<', r, c - 1)]:
            if grid[r][c] in ['v', '>', '^', '<'] and grid[r][c] != ch:
                continue

            q.append((nr, nc, path + [(r, c)]))

    print('Part 1:', longest)


# Very brute force, took several hours to get the longest path
def solve_p2():
    grid = parse()
    R = len(grid)
    C = len(grid[0])

    q = deque([(0, 1, [])])
    longest = 0
    s_longest = set()
    while q:
        r, c, path = q.pop()

        if (r, c) in path:
            continue

        if (r, c) == (R - 1, C - 2):
            longest = max(longest, len(path))
            if longest not in s_longest:
                print(longest)
                s_longest.add(longest)
            continue

        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] != '#':
                    q.append((nr, nc, path + [(r, c)]))

    print('Part 2:', longest)


solve_p1()
solve_p2()
