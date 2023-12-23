import sys
from collections import defaultdict


def parse():
    D = open(sys.argv[1]).read().strip().split('\n')
    bricks = []
    for line in D:
        parts = line.split('~')
        start = tuple(map(int, parts[0].split(',')))
        end = tuple(map(int, parts[1].split(',')))
        bricks.append((start, end))

    bricks.sort(key=lambda b: b[0][2])

    for i, b in enumerate(bricks):
        (x1, y1, z1), (x2, y2, z2) = b
        z = 1

        for bb in bricks[:i]:
            if overlaps(b, bb):
                z = max(z, bb[1][2] + 1)

        z2 -= z1 - z
        z1 = z

        bricks[i] = ((x1, y1, z1), (x2, y2, z2))
    return bricks


def overlaps(rect1, rect2):
    (x1, y1, _), (x2, y2, _) = rect1
    (x3, y3, _), (x4, y4, _) = rect2

    if x2 < x3 or x4 < x1:
        return False

    if y2 < y3 or y4 < y1:
        return False

    return True


def solve_p1():
    bricks = parse()

    supports = {i: set() for i in range(len(bricks))}
    supported = {i: set() for i in range(len(bricks))}

    for i, b in enumerate(bricks):
        for j, bb in enumerate(bricks[:i]):
            if overlaps(b, bb) and b[0][2] == bb[1][2] + 1:
                supports[j].add(i)
                supported[i].add(j)

    count = 0
    for i in range(len(bricks)):
        if all(len(supported[j]) >= 2 for j in supports[i]):
            count += 1

    print('Part 1:', count)


def solve_p2():
    bricks = parse()
    supports = {i: set() for i in range(len(bricks))}
    supported = {i: set() for i in range(len(bricks))}

    for i, b in enumerate(bricks):
        for j, bb in enumerate(bricks[:i]):
            if overlaps(b, bb) and b[0][2] == bb[1][2] + 1:
                supports[j].add(i)
                supported[i].add(j)

    # print('supports', supports)
    # print('supported', supported)

    sum_bricks = 0
    for i in range(len(bricks)):
        current = {i}
        destroyed_bricks = {i}
        count = -1
        while True:
            count += len(current)
            sb = {index for c in current for index in supports[c]}

            if len(sb) == 0:
                break

            nb = set()
            for si in sb:
                if supported[si] == current or supported[si].issubset(current.union(destroyed_bricks)):
                    nb.add(si)

            current = nb
            destroyed_bricks.update(nb)

        sum_bricks += count

    print('Part 2:', sum_bricks)


solve_p1()
solve_p2()
