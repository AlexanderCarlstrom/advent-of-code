import sys
import re
from collections import deque
import utils
import math

NORTH = ('S|JL', '|7F')
SOUTH = ('S|F7', '|LJ')
WEST = ('S-J7', '-LF')
EAST = ('S-LF', '-J7')


# Part 1
data = utils.parse_single_string('in.txt')
S = (0, 0)
for r, row in enumerate(data):
    c = row.find('S')
    if c != -1:
        S = (r, c)
        break

q = deque([S])
seen = {S}
possible_s = {'|', '-', 'L', 'J', '7', 'F'}

while q:
    row, col = q.popleft()
    ch = data[row][col]

    if row > 0 and ch in NORTH[0] and data[row - 1][col] in NORTH[1] and (row - 1, col) not in seen:
        q.append((row - 1, col))
        seen.add((row - 1, col))

        if ch == 'S':
            possible_s &= set(NORTH[0])
    if row < len(data) - 1 and ch in SOUTH[0] and data[row + 1][col] in SOUTH[1] and (row + 1, col) not in seen:
        q.append((row + 1, col))
        seen.add((row + 1, col))

        if ch == 'S':
            possible_s &= set(SOUTH[0])
    if col > 0 and ch in WEST[0] and data[row][col - 1] in WEST[1] and (row, col - 1) not in seen:
        q.append((row, col - 1))
        seen.add((row, col - 1))

        if ch == 'S':
            possible_s &= set(WEST[0])
    if col < len(data[0]) - 1 and ch in EAST[0] and data[row][col + 1] in EAST[1] and (row, col + 1) not in seen:
        q.append((row, col + 1))
        seen.add((row, col + 1))

        if ch == 'S':
            possible_s &= set(EAST[0])

print('Part 1:', len(seen) // 2)

# Part 2
(new_s,) = possible_s
data = [row.replace('S', new_s) for row in data]

dots = 0
for r, row in enumerate(data):
    count = 0
    up = False
    for c, ch in enumerate(row):
        if (r, c) not in seen:
            if count % 2 != 0:
                dots += 1
            continue

        if ch == '|':
            count += 1
        elif ch == 'L':
            up = True
        elif ch == 'F':
            up = False
        elif ch == '7':
            if up:
                count += 1
            else:
                count += 2
            up = None
        elif ch == 'J':
            if up:
                count += 2
            else:
                count += 1
            up = None

print('Part 2:', dots)


