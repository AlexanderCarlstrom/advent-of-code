import sys
import re
import math
from functools import cache


def solve_p1():
    D = open(sys.argv[1]).read().strip()
    nums = [int(n) for n in D.split(' ')]

    runs = 25
    for x in range(runs):
        new_nums = [[num] for num in nums]
        for idx, num in enumerate(nums):
            if num == 0:
                new_nums[idx] = [1]
                continue
            if len(str(num)) % 2 == 0:
                stone_one = str(num)[:len(str(num))//2]
                stone_two = str(num)[len(str(num))//2:]
                new_nums[idx] = [int(stone_one), int(stone_two)]
                continue
            else:
                new_nums[idx] = [num*2024]
        nums = sum(new_nums, [])

    return len(nums)

@cache
def count_stones(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count_stones(1, steps - 1)
    s = str(stone)
    l = len(s)
    if (l % 2 == 0):
        return count_stones(int(s[l//2:]), steps - 1) + count_stones(int(s[:l//2]), steps - 1)
    return count_stones(stone * 2024, steps - 1)


def solve_p2():
    D = open(sys.argv[1]).read().strip()
    nums = [int(num) for num in D.split(' ')]
    return sum([count_stones(num, 75) for num in nums])



print('Part 1:', solve_p1())
print('Part 2:', solve_p2())