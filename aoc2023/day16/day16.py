import sys
import re


operators = {
    '/': {
        'N': (0, 1, 'E'),
        'S': (0, -1, 'W'),
        'W': (1, 0, 'S'),
        'E': (-1, 0, 'N')
    },
    '\\': {
        'N': (0, -1, 'W'),
        'S': (0, 1, 'E'),
        'W': (-1, 0, 'N'),
        'E': (1, 0, 'S')
    }
}


def is_outside(pos, R, C):
    r, c = pos[0:2]
    return r < 0 or r >= R or c < 0 or c >= C


def sim_beams(beam):
    beams = [beam]
    touched = set()

    while len(beams) > 0:
        t_beams = []
        beams_length = len(beams)
        for i in range(beams_length):
            r, c, d = beams[i]
            if is_outside(beams[i], R, C) or (r, c, d) in touched:
                continue

            positions = []

            ch = G[r][c]
            if ch in '/\\':
                op = operators[ch][d]
                positions.append((r + op[0], c + op[1], op[2]))

            elif ch == '-' and d in 'NS':
                if (r, c, 'N') in touched or (r, c, 'S') in touched:
                    continue
                positions.append((r, c - 1, 'W'))
                positions.append((r, c + 1, 'E'))

            elif ch == '|' and d in 'WE':
                if (r, c, 'W') in touched or (r, c, 'E') in touched:
                    continue
                positions.append((r - 1, c, 'N'))
                positions.append((r + 1, c, 'S'))

            else:
                if d == 'N':
                    positions.append((r - 1, c, d))
                elif d == 'S':
                    positions.append((r + 1, c, d))
                elif d == 'W':
                    positions.append((r, c - 1, d))
                elif d == 'E':
                    positions.append((r, c + 1, d))

            touched.add(beams[i])
            t_beams.extend(positions)

        beams = t_beams

    touched = set([(pos[0], pos[1]) for pos in touched])
    return len(touched)


G = open(sys.argv[1]).read().strip().split('\n')
G = [[ch for ch in row] for row in G]
R = len(G)
C = len(G[0])


def solve_p1():
    touched = sim_beams((0, 0, 'E'))

    print('Part 1:', touched)


def solve_p2():
    starting_beams = []
    max_touched = 0

    for c in range(C):
        starting_beams.append((R - 1, c, 'N'))
        starting_beams.append((0, c, 'S'))
    for r in range(1, R - 1):
        starting_beams.append((r, C - 1, 'W'))
        starting_beams.append((r, 0, 'E'))

    for beam in starting_beams:
        touched = sim_beams(beam)
        if touched > max_touched:
            max_touched = touched

    print('Part 2:', max_touched)


solve_p1()
solve_p2()


