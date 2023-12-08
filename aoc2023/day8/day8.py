import math
import sys
import re
from collections import defaultdict

import utils


def solve_p1():
    data = utils.parse_single_string("in.txt")
    instructions = list(data[0])
    nodes = []
    for n in data[2:]:
        groups = re.search(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', n).groups()
        nodes.append(Node1(groups[0], groups[1], groups[2]))

    current_node = find_node(nodes, 'AAA')
    found = False
    steps, i = [], 0

    while not found:
        steps.append(current_node.node)
        if instructions[i] == 'L':
            current_node = find_node(nodes, current_node.left)
        elif instructions[i] == 'R':
            current_node = find_node(nodes, current_node.right)

        if current_node.node == 'ZZZ':
            found = True

        i += 1
        if i == len(instructions):
            i = 0

    return len(steps)


def solve_p2():
    data = utils.parse_single_string('in.txt')
    instructions = list(data[0])

    nodes = defaultdict(tuple)
    current_nodes = []
    for n in data[2:]:
        groups = re.search(r'([A-Z\d]{3}) = \(([A-Z\d]{3}), ([A-Z\d]{3})\)', n).groups()
        nodes[groups[0]] = (groups[1], groups[2])

        if 'A' in groups[0]:
            current_nodes.append(groups[0])

    count, i = 0, 0
    steps = []

    while True:
        move = instructions[i]
        temp_nodes = []

        for node in current_nodes:
            if move == 'L':
                temp_nodes.append(nodes[node][0])
            elif move == 'R':
                temp_nodes.append(nodes[node][1])

            if node.endswith('Z'):
                steps.append(count)

        if len(steps) == len(current_nodes):
            return math.lcm(*steps)
        current_nodes = temp_nodes

        count += 1
        i += 1
        if i == len(instructions):
            i = 0


class Node1:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right


class Node:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

    def insert(self, node, position):
        if position == 'L':
            self.left = Node(node)
        elif position == 'R':
            self.right = Node(node)


def find_node(nodes, node):
    for n in nodes:
        if n.node == node:
            return n

    return


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())
