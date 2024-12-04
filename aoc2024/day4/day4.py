import sys
import re
import math


def is_inside(y, x, grid):
    if (y < 0 or y >= len(grid)):
        return False
    if (x < 0 or x >= len(grid[0])):
        return False
    return True


def get_dir_pos(y, x, direction):
    if direction == 'N':
        return (y - 1, x)
    if direction == 'NE':
        return (y - 1, x + 1)
    if direction == 'E':
        return (y, x + 1)
    if direction == 'SE':
        return (y + 1, x + 1)
    if direction == 'S':
        return (y + 1, x)
    if direction == 'SW':
        return (y + 1, x - 1)
    if direction == 'W':
        return (y, x - 1)
    if direction == 'NW':
        return (y - 1, x - 1)


def get_character(y, x, grid):
    return


def solve_p1():
    G = open(sys.argv[1]).read().strip().split('\n')

    # find all x
    word = 'XMAS'
    x_positions = []
    word_count = 0
    for y in range(len(G)):
        for x in range(len(G[y])):
            if G[y][x] == 'X':
                x_positions.append((y, x))

    for pos in x_positions:
        y, x = pos
        directions = [(y, x, 'N', 1), (y, x, 'NE', 1), (y, x, 'E', 1), (y, x, 'SE', 1), (y, x, 'S', 1), (y, x, 'SW', 1), (y, x, 'W', 1), (y, x, 'NW', 1)]

        while len(directions) > 0:
            y, x, dir, count = directions.pop(0)
            y2, x2 = get_dir_pos(y, x, dir)
            if not is_inside(y2, x2, G):
                continue

            if G[y2][x2] == word[count]:
                if count == 3:
                    word_count = word_count + 1
                else:
                    directions.append((y2, x2, dir, count + 1))

    print(len(x_positions))
    return word_count


def solve_p2():
    G = open(sys.argv[1]).read().strip().split('\n')

    # find all x
    word = 'MAS'
    a_positions = []
    word_count = 0
    for y in range(len(G)):
        for x in range(len(G[y])):
            if G[y][x] == 'A':
                a_positions.append((y, x))

    for pos in a_positions:
        y, x = pos
        new_positions = [(y - 1, x - 1), (y + 1, x + 1), (y + 1, x - 1), (y - 1, x + 1)]
        if not all([is_inside(new_pos[0], new_pos[1], G) for new_pos in new_positions]):
            continue

        chars1 = [G[p[0]][p[1]] for p in new_positions[:2]]
        chars2 = [G[p[0]][p[1]] for p in new_positions[2:]]
        if chars1.count('S') == 1 and chars1.count('M') == 1 and chars2.count('S') == 1 and chars2.count('M') == 1:
            word_count = word_count + 1
        # diagonal1 = [G[y - 1][x - 1], G[y + 1][x + 1]].sort()
        # diagonal2 = [G[y + 1][x - 1], G[y - 1][x + 1]].sort()

        # if diagonal1 == diagonal2:
        #     x_mas.add((y, x))

    # for pos in a_positions:
    #     y, x = pos
    #     directions = [(y, x, 'N', 1), (y, x, 'NE', 1), (y, x, 'E', 1), (y, x, 'SE', 1), (y, x, 'S', 1), (y, x, 'SW', 1), (y, x, 'W', 1), (y, x, 'NW', 1)]

    #     while len(directions) > 0:
    #         y2, x2, dir, count = directions.pop(0)
    #         y3, x3 = get_dir_pos(y2, x2, dir)
    #         if not is_inside(y3, x3, G):
    #             continue

    #         if G[y3][x3] == word[count]:
    #             if count == 3:
    #                 word_count = word_count + 1
    #             else:
    #                 directions.append((y3, x3, dir, count + 1))

    return word_count


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())
