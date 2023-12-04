import sys
import re
from collections import defaultdict

import utils
valves = {}
tunnels = {}

pattern = re.compile(r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
for line in utils.parse_single_string('example.txt'):
    rx = pattern.search(line)
    groups = rx.groups()

    valve = groups[0]
    flow = groups[1]
    edges = [e.strip() for e in groups[2].split(',')]

    valves[valve] = flow
    tunnels[valve] = edges

dists = {}

