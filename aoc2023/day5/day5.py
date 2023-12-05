from collections import defaultdict
import re

import utils

D = utils.parse_single_string('ex.txt')
seeds = [int(num) for num in D[0].split(':')[1].split()]

maps = defaultdict(list)
current_map = []
current_category = ''
new_category = False
for i, line in enumerate(D[2:]):
    if i == 0 or new_category:
        groups = re.search(r'([a-z]+)-to-([a-z]+) map:', line).groups()
        current_category = '-'.join(groups)
        new_category = False
    elif line == '':
        new_category = True
        maps[current_category] = current_map
        current_category = ''
        current_map = []
    else:
        nums = [int(n) for n in line.split()]
        # destination = nums[0]
        # source = nums[1]
        # for n in range(0, nums[2]):
        #     current_map[source + n] = destination + n
        current_map.append(nums)

if len(current_map) > 0:
    maps[current_category] = current_map

print(maps['fertilizer-water'])

lowest_location = -1
for s in seeds:
    source = s
    for m in maps:
        for nums in maps[m]:
            if nums[1] <= source <= (nums[1] + nums[2] - 1):
                source = nums[0] + (source - nums[1])

    #     print(source)
    #
    # print('---')
    if lowest_location == -1 or source < lowest_location:
        lowest_location = source

print(lowest_location)

