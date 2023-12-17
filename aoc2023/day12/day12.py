import sys
import re


def generate_variants(input_line):
    if '?' not in input_line:
        return [input_line]

    template_index = input_line.index('?')
    line_variants = []
    for ch in '.#':
        variant = input_line.replace('?', ch, 1)
        line_variants.extend(generate_variants(variant))

    return line_variants


keys = {}





def count_groups(input_row):
    spring_groups = []
    current_group = ''
    for i, ch in enumerate(input_row):
        if ch == '#':
            current_group += '#'

            if i == len(input_row) - 1:
                spring_groups.append(len(current_group))
        elif len(current_group) > 0:
            spring_groups.append(len(current_group))
            current_group = ''

    return spring_groups


# MAIN PARTS

D = open(sys.argv[1]).read().strip().split('\n')


def solve_p1():
    count = 0
    for line in D:
        dots, groups = line.split(' ')
        groups = [int(g) for g in groups.split(',')]
        variants = generate_variants(dots)
        count += len(list(filter(lambda v: count_groups(v) == groups, variants)))

    print('Part 1:', count)


def solve_p2():
    count = 0
    for line in D:
        dots, groups = line.split(' ')
        groups = [int(g) for g in groups.split(',')]*5
        dots = '?'.join([dots]*5)
        print('dots', dots)
        print('groups', groups)
        # variants = generate_variants(dots)
        # count += len(list(filter(lambda v: count_groups(v) == groups, variants)))

    print('Part 2:', count)


solve_p2()
