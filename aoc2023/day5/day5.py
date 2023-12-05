from collections import defaultdict
import re
import utils


def solve_p1():
    D = utils.parse_single_string('in.txt')
    seeds = [int(num) for num in D[0].split(':')[1].split()]
    maps = parse_maps(D)

    lowest_location = -1
    for s in seeds:
        source = s
        for m in maps:
            for m_item in m:
                if m_item[1] <= source < m_item[1] + m_item[2]:
                    source = m_item[0] + (source - m_item[1])
                    break

        if lowest_location == -1 or source < lowest_location:
            lowest_location = source

    return lowest_location


def solve_p2():
    D = utils.parse_single_string('in.txt')
    seeds_input = [int(num) for num in D[0].split(':')[1].split()]
    seeds = []

    for i, s in enumerate(seeds_input):
        if i % 2 == 0:
            seeds.append([s, s + seeds_input[i + 1] - 1])

    maps = parse_maps(D)

    seed_location = defaultdict(int)
    for m in maps:
        found_seeds = []
        for i, r in enumerate(m):
            start_range, end_range = [r[1], r[1] + r[2] - 1]
            temp_seeds = []
            for j, seed in enumerate(seeds):
                start_seed, end_seed = seed
                start, end = 0, 0
                # outside
                if end_range < start_seed or end_seed < start_range:
                    temp_seeds.append(seed)
                    continue

                if start_seed < start_range:
                    start = start_range
                    temp_seeds.append([start_seed, start - 1])
                elif start_seed >= start_range:
                    start = start_seed

                if end_seed <= end_range:
                    end = end_seed
                elif end_seed > end_range:
                    end = end_range
                    temp_seeds.append([end + 1, end_seed])
                found_seeds.append([r[0] + (start - r[1]), r[0] + (end - r[1])])

            seeds = temp_seeds
        seeds.extend(found_seeds)

    return min([s[0] for s in seeds])


def parse_maps(data):
    maps = []
    current_map = []
    new_category = False
    for i, line in enumerate(data[2:]):
        if i == 0 or new_category:
            new_category = False
        elif line == '':
            new_category = True
            maps.append(current_map)
            current_category = ''
            current_map = []
        else:
            nums = [int(n) for n in line.split()]
            current_map.append(nums)

    if len(current_map) > 0:
        maps.append(current_map)

    return maps


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())

