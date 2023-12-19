import sys
import re
import operator
import functools


def parse():
    D = open(sys.argv[1]).read().strip().split('\n\n')
    workflow = {}
    items = []

    for line in D[0].split('\n'):
        parts = line.split('{')

        instructions = parts[1][:-1].split(',')
        workflow[parts[0]] = []
        for inst in instructions:
            m = re.match(r'^([A-Za-z]+)([<>])(\d+):([A-Za-z]+)$', inst)
            if m:
                v, op, n, w = m.groups()
                workflow[parts[0]].append((v, op, int(n), w))
            else:
                workflow[parts[0]].append(inst)

    for line in D[1].split('\n'):
        parts = line[1:-1].split(',')
        item = {}
        for p in parts:
            v, n = p.split('=')
            item[v] = int(n)

        items.append(item)

    return workflow, items


def solve_p1():
    operators = {
        '<': operator.lt,
        '>': operator.gt
    }

    workflows, items = parse()

    accepted = 0
    for item in items:
        current = 'in'
        run = True
        while run:
            for inst in workflows[current]:
                if isinstance(inst, str):
                    if inst == 'A':
                        accepted += sum(item.values())
                        run = False
                    elif inst == 'R':
                        run = False
                    else:
                        current = inst
                    break
                else:
                    v, op, n, w = inst
                    if operators[op](item[v], n):
                        if w == 'A':
                            accepted += sum(item.values())
                            run = False
                        elif w == 'R':
                            run = False
                        else:
                            current = w
                        break

    print('Part 1:', accepted)


def count_variations(workflows, item, name):
    if name == 'R':
        return 0
    if name == 'A':
        return functools.reduce(lambda a, b: a*b, [rg[1] - rg[0] + 1 for rg in item.values()])

    variations = 0

    for inst in workflows[name]:
        if isinstance(inst, str):
            variations += count_variations(workflows, item, inst)
        else:
            v, op, n, w = inst
            inside, outside = (0, 0), (0, 0)
            if op == '<':
                inside = (item[v][0], n - 1)
                outside = (n, item[v][1])
            elif op == '>':
                inside = (n + 1, item[v][1])
                outside = (item[v][0], n)

            if inside[0] <= inside[1]:
                new_item = dict(item)
                new_item[v] = inside
                variations += count_variations(workflows, new_item, w)

            if outside[0] <= outside[1]:
                item[v] = outside
            else:
                break

    return variations


def solve_p2():
    workflows, _ = parse()

    item = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }

    variations = count_variations(workflows, item, 'in')
    print('Part 2:', variations)


solve_p1()
solve_p2()
