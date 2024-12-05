import sys
import re
import math


def solve_p1():
    D = open(sys.argv[1]).read().strip().split('\n\n')

    rules = dict()
    lines = D[0].split('\n')
    for line in lines:
        x, y = map(int, line.split('|'))

        if rules.get(y):
            rules[y].append(x)
        else:
            rules[y] = [x]

    sum = 0
    lines = D[1].split('\n')
    for line in lines:
        nums = list(map(int, line.split(',')))
        is_valid = True

        for i, num in enumerate(nums):
            before = nums[:i]
            after = nums[i+1:]
            if rules.get(num):
                if not set(before).issubset(rules[num]) or any([a in rules[num] for a in after]):
                    is_valid = False
                    break

        if is_valid:
            sum += nums[len(nums)//2]

    return sum


def solve_p2():
    D = open(sys.argv[1]).read().strip().split('\n\n')

    rules = [list(map(int, nums.split('|'))) for nums in D[0].split('\n')]
    updates = [list(map(int, line.split(','))) for line in D[1].split('\n')]

    sum = 0
    invalids = set()
    new_rules = set()
    for ir, rule in enumerate(rules):
        x, y = rule
        for i in range(len(updates)):
            if x in updates[i] and y in updates[i]:
                idx = updates[i].index(x)
                idy = updates[i].index(y)
                if idx > idy :
                    num = updates[i].pop(idx)
                    updates[i].insert(idy, num)
                    invalids.add(i)
                    new_rules.add(ir)

    for i in invalids:
        while True:
            changed = False
            for ir in new_rules:
                x, y = rules[ir]
                if x in updates[i] and y in updates[i]:
                    idx = updates[i].index(x)
                    idy = updates[i].index(y)
                    if idx > idy :
                        changed = True
                        num = updates[i].pop(idx)
                        updates[i].insert(idy, num)

            if not changed:
                break

        sum += updates[i][len(updates[i])//2]
    return sum


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())