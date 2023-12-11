import copy

import utils
import re
from collections import defaultdict


def solve_p1():
    # PART 1
    graph = utils.parse_single_string('ex.txt')

    graph = add_rows(graph)
    graph = add_columns(graph)
    nodes = get_nodes(graph)

    pairs = []
    for i in range(0, len(nodes) - 1):
        node1 = nodes[i]
        for j in range(i + 1, len(nodes)):
            node2 = nodes[j]
            pairs.append(tuple([node1, node2]))

    sum_paths = 0
    for pair in pairs:
        path = shortest_path(graph, pair[0], pair[1])
        sum_paths += path

    print('Part 1:', sum_paths)


def solve_p2():
    # PART 2
    graph = utils.parse_single_string('in.txt')
    c_row = len(graph)
    c_col = len(graph[0])

    nodes = get_nodes(graph)
    t_nodes = copy.deepcopy(nodes)
    for row in range(0, c_row):
        row_nodes = list(filter(lambda node: node[0] == row, nodes))
        if len(row_nodes) == 0:
            for i in range(0, len(nodes)):
                if nodes[i][0] > row:
                    t_nodes[i][0] += 999999

    for col in range(0, c_col):
        col_nodes = list(filter(lambda node: node[1] == col, nodes))
        if len(col_nodes) == 0:
            for i in range(0, len(nodes)):
                if nodes[i][1] > col:
                    t_nodes[i][1] += 999999

    nodes = t_nodes
    for node in nodes:
        print(node)

    pairs = []
    for i in range(0, len(nodes) - 1):
        node1 = nodes[i]
        for j in range(i + 1, len(nodes)):
            node2 = nodes[j]
            pairs.append(tuple([node1, node2]))

    sum_paths = 0
    for pair in pairs:
        path = shortest_path(graph, pair[0], pair[1])
        sum_paths += path

    print('Part 2:', sum_paths)


def shortest_path(graph, node1, node2):
    horizontal_diff = abs(node1[0] - node2[0])
    vertical_diff = abs(node1[1] - node2[1])
    return horizontal_diff + vertical_diff


def add_rows(graph, part=1):
    t_graph = []
    for row in graph:
        if all([ch == '.' for ch in row]):
            if part == 2:
                t_graph.extend([row] * 1000000)
            else:
                t_graph.extend([row] * 2)
        else:
            t_graph.append(row)

    return t_graph


def add_columns(graph, part=1):
    columns = [True] * len(graph[0])
    t_graph = [''] * len(graph)
    for r, row in enumerate(graph):
        for c, ch in enumerate(row):
            if ch == '#':
                columns[c] = False

    for c, col in enumerate(columns):
        for i in range(0, len(t_graph)):
            if col:
                if part == 2:
                    t_graph[i] += '.' * 1000000
                else:
                    t_graph[i] += '.' * 2
            else:
                t_graph[i] += graph[i][c]

    return t_graph


def get_nodes(graph):
    galaxies = []
    for r, row in enumerate(graph):
        for c, ch in enumerate(row):
            if ch == '#':
                galaxies.append([r, c])

    return galaxies


solve_p1()
solve_p2()