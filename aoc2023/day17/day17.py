import sys
from heapq import heappush, heappop


def reverse_direction(direction):
    return tuple([-direction[0], -direction[1]])


G = open(sys.argv[1]).read().strip().split('\n')
G = [[int(n) for n in row] for row in G]
R = len(G)
C = len(G[0])


def solve_p1():
    visited = set()
    # heat, node/position, direction, number of times in direction
    q = [(0, (0, 0), (0, 0), 0)]

    while q:
        heat, current, direction, n = heappop(q)
        r, c = current
        dr, dc = direction

        if current == (R - 1, C - 1):
            print('Part 1:', heat)
            break

        if (current, direction, n) in visited:
            continue

        visited.add((current, direction, n))

        for new_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ndr, ndc = new_direction
            if new_direction != reverse_direction(direction):
                nn = 1
                if new_direction == direction:
                    if n < 3:
                        nn = n + 1
                    else:
                        continue

                next_pos = (r + ndr, c + ndc)
                if 0 <= next_pos[0] < R and 0 <= next_pos[1] < C:
                    heappush(q, (heat + G[next_pos[0]][next_pos[1]], next_pos, new_direction, nn))


def solve_p2():
    visited = set()
    # heat, node/position, direction, number of times in direction
    q = [(0, (0, 0), (0, 0), 0)]

    while q:
        heat, current, direction, n = heappop(q)
        r, c = current
        dr, dc = direction

        if current == (R - 1, C - 1) and n >= 4:
            print('Part 2:', heat)
            break

        if (current, direction, n) in visited:
            continue

        visited.add((current, direction, n))

        for new_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ndr, ndc = new_direction
            if new_direction != reverse_direction(direction):
                next_pos = (r + ndr, c + ndc)
                if 0 <= next_pos[0] < R and 0 <= next_pos[1] < C:
                    if new_direction == direction:
                        if n < 10:
                            heappush(q, (heat + G[next_pos[0]][next_pos[1]], next_pos, new_direction, n + 1))
                        else:
                            continue
                    elif n >= 4 or direction == (0, 0):
                        heappush(q, (heat + G[next_pos[0]][next_pos[1]], next_pos, new_direction, 1))


solve_p1()
solve_p2()
