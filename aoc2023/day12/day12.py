import utils
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
def gen_variants(dots, groups, i, gi, gl):



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


D = utils.parse_single_string('ex.txt')
p1 = 0
p2 = 0
for line in D:
    row, groups = line.split(' ')
    groups = [int(g) for g in groups.split(',')]

    variants = generate_variants(row)
    base_possible = len(list(filter(lambda v: count_groups(v) == groups, variants)))
    possible = 1

    if all(char in '#?' for char in row[len(row) - groups[-1]:]):
        possible = base_possible
    else:
        possible = len(list(filter(lambda v: count_groups(v) == groups, generate_variants('?' + row))))

    print(base_possible * pow(possible, 4))

    p1 += base_possible
    p2 += base_possible * pow(possible, 4)


print('Part 1:', p1)
print('Part 2:', p2)
