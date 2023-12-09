import utils


def solve_p1():
    data = utils.parse_multiple_int('in.txt')
    lines = create_history(data)

    for values in lines:
        values[-1].append(0)
        for i in range(len(values) - 2, -1, -1):
            next_value = values[i][-1] + values[i + 1][-1]
            values[i].append(next_value)

    return sum(line[0][-1] for line in lines)


def solve_p2():
    data = utils.parse_multiple_int('in.txt')
    lines = create_history(data)

    for values in lines:
        values[-1].insert(0, 0)
        for i in range(len(values) - 2, -1, -1):
            next_value = values[i][0] - values[i + 1][0]
            values[i].insert(0, next_value)

    return sum(line[0][0] for line in lines)


def create_history(data):
    lines = []
    for i, line in enumerate(data):
        values = [line]
        current = values[0]
        while not all(c == 0 for c in current):
            hist = []
            for j in range(0, len(current) - 1):
                hist.append(current[j + 1] - current[j])
            values.append(hist)
            current = hist
        lines.append(values)

    return lines


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())
