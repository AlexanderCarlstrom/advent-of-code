import utils


def generate_variants(group):
    if '?' not in group:
        return [group]

    template_index = group.index('?')
    variants = []
    for ch in '.#':
        variant = group.replace('?', ch, 1)
        variants.extend(generate_variants(variant))

    return variants


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
possibles = []
for line in D[0:1]:
    row, groups = line.split(' ')
    groups = [int(g) for g in groups.split(',')]

    possible = 0
    for v in generate_variants(row):
        group_count = count_groups(v)
        print(v)
        if group_count == groups:
            possible += 1

    possibles.append(possible)

print('Part 1:', sum(possibles))

print(len(generate_variants('.??..??...?##')))