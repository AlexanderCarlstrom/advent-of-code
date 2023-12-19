import sys
import re
import operator


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


def solve_p2():
    workflows, _ = parse()
    variations = 0

    for workflow in workflows.items():
        for inst in workflow[1]:
            item = {'x': 4000, 'm': 4000, 'a': 4000, 's': 4000}
            print(inst)


solve_p1()
solve_p2()