import utils


def solve_p1():
    inp = utils.parse_single_string('in.txt')
    data = []
    for line in inp:
        data.append(list(filter(None, line.split(' '))))

    times = [int(n) for n in data[0][1:]]
    distances = [int(n) for n in data[1][1:]]

    win_sum = 1
    for i in range(0, len(times)):
        time = times[i]
        distance = distances[i]

        ways_to_win = 0
        for t in range(1, time + 1):
            time_left = time - t
            dist = time_left * t
            if dist > distance:
                ways_to_win += 1

        if ways_to_win > 0:
            win_sum *= ways_to_win

    return win_sum


def solve_p2():
    inp = utils.parse_single_string('in.txt')
    data = []
    for line in inp:
        data.append(list(filter(None, line.split(' '))))

    time = int(''.join(data[0][1:]))
    distance = int(''.join(data[1][1:]))

    ways_to_win = 0
    for t in range(1, time + 1):
        time_left = time - t
        dist = time_left * t
        if dist > distance:
            ways_to_win += 1

    return ways_to_win


def parse_data(data):
    d = []
    for dd in data:
        d.append(list(filter(None, dd)))

    return d


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())
