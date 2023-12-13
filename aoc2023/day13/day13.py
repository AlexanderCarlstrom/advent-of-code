import utils
from numpy import array


def solve_p1():
    D = utils.parse_single_string('ex.txt')

    patterns = [[]]
    for line in D:
        if line == '':
            patterns.append([])
        else:
            patterns[-1].append(list(line))

    v_cols = 0
    h_cols = 0
    c_patterns = []

    for p in patterns:
        arr = array(p)
        for i in range(0, len(p) - 1):
            if p[i] == p[i + 1]:
                c1, c2 = i, i + 1

    print('v_cols', v_cols)



solve_p1()