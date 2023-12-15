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


def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print('')
    print('--------------------------')
    print('')


def flatten_grid(grid):
    return '\n'.join([''.join(row) for row in grid])


def solve_p2():
    grid = open('in.txt').read().strip().split('\n')
    grid = [[ch for ch in row] for row in grid]
    R = len(grid)
    C = len(grid[0])

    flat = flatten_grid(grid)
    seen = {flat}
    array = [flat]
    while True:
        move_north(grid)
        move_west(grid)
        move_south(grid)
        move_east(grid)

        flat = flatten_grid(grid)
        if flat in seen:
            break

        seen.add(flat)
        array.append(flat)

    start = array.index(flat)
    end = len(seen)

    grid = array[(1000000000 - start) % (end - start) + start].split('\n')

    points = 0
    for r, line in enumerate(grid):
        counter = Counter(line)['O']
        points += counter * (R - r)

    print('Part 1:', points)


solve_p1()
solve_p2()
