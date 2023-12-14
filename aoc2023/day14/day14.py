from collections import Counter


def move_north(grid):
    changed = True
    while changed:
        changed = False
        for r in range(1, len(grid)):
            for c, ch in enumerate(grid[r]):
                if ch == 'O' and grid[r - 1][c] not in '#O':
                    grid[r - 1][c] = 'O'
                    grid[r][c] = '.'
                    changed += True


def move_west(grid):
    changed = True
    while changed:
        changed = False
        for r in range(0, len(grid)):
            for c in range(1, len(grid[r])):
                if grid[r][c] == 'O' and grid[r][c - 1] not in '#O':
                    grid[r][c - 1] = 'O'
                    grid[r][c] = '.'
                    changed += True


def move_south(grid):
    changed = True
    while changed:
        changed = False
        for r in range(len(grid) - 2, -1, -1):
            for c, ch in enumerate(grid[r]):
                if ch == 'O' and grid[r + 1][c] not in '#O':
                    grid[r + 1][c] = 'O'
                    grid[r][c] = '.'
                    changed += True


def move_east(grid):
    changed = True
    while changed:
        changed = False
        for r in range(0, len(grid)):
            for c in range(len(grid[r]) - 2, -1, -1):
                if grid[r][c] == 'O' and grid[r][c + 1] not in '#O':
                    grid[r][c + 1] = 'O'
                    grid[r][c] = '.'
                    changed += True


def solve_p1():
    D = open('in.txt').read().strip().split('\n')
    grid = [[ch for ch in row] for row in D]
    L = len(grid)
    move_north(grid)

    points = 0
    for r, line in enumerate(grid):
        counter = Counter(line)['O']
        points += counter * (L - r)

    print('Part 1:', points)


def get_next(r, c, direction):
    if direction == 'N':
        return tuple([r - 1, c])
    if direction == 'W':
        return tuple([r, c - 1])
    if direction == 'S':
        return tuple([r + 1, c])
    if direction == 'E':
        return tuple([r, c + 1])


def solve_p2():
    D = open('ex.txt').read().strip().split('\n')
    grid = [[ch for ch in row] for row in D]
    R = len(grid)
    C = len(grid[0])
    stones = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'O':
                grid[r][c] = '.'
                stones.append((r, c))

    print(1)

    for cycle in range(1):
        for d in ['N', 'W', 'S', 'E']:
            for s in range(len(stones)):
                (r, c) = stones[s]

                can_move = True
                while can_move:
                    (r, c) = get_next(r, c, d)
                    print('first', r, c)
                    print('next', d, r, c)
                    if 0 <= r < R and 0 <= c < C:
                        if grid[r][c] not in '#O':
                            stones[s] = (r, c)
                        else:
                            can_move = False

    print(2)

    for s in range(len(stones)):
        (r, c) = stones[s]
        grid[r][c] = 'O'

    for line in grid:
        print(''.join(line))

    points = 0
    for r, line in enumerate(grid):
        counter = Counter(line)['O']
        points += counter * (R - r)

    print('Part 2:', points)


solve_p1()
solve_p2()
