import sys
import re
import math


def solve_p1():
    D = open(sys.argv[1]).read().strip().split('\n')
    reports = [[int(level) for level in report.split(' ')] for report in D]

    safe_count = 0
    for report in reports:
        asc = all(report[i] < report[i+1] and abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))
        desc = all(report[i] > report[i+1] and abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))

        if asc or desc:
            safe_count = safe_count + 1
    return safe_count


def solve_p2():
    D = open(sys.argv[1]).read().strip().split('\n')
    reports = [[int(level) for level in report.split(' ')] for report in D]

    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count = safe_count + 1
        else:
            for i in range(len(report)):
                for j in range(len(report)):
                    if is_safe(report[:i] + report[i+1:]):
                        safe_count = safe_count + 1
                        break
                else:
                    continue
                break
    return safe_count


def is_safe(report):
    asc = all(report[i] < report[i+1] and abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))
    desc = all(report[i] > report[i+1] and abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))

    return asc or desc


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())
