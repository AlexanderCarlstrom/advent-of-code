def read_lines(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


# one int per line
def parse_single_int(path):
    data = read_lines(path)
    arr = [int(line) for line in data]
    return arr


# one string per line
def parse_single_string(path):
    data = read_lines(path)
    arr = [line.replace('\n', '') for line in data]
    return arr


# multiple ints per line
def parse_multiple_int(path, sep=' '):
    data = read_lines(path)
    if sep == '':
        arr = [[int(i) for i in list(line.replace('\n', ''))] for line in data]
    else:
        arr = [[int(i) for i in line.replace('\n', '').split(sep)] for line in data]
    return arr


# multiple strings per line
def parse_multiple_string(path, sep=' '):
    data = read_lines(path)
    if sep == '':
        arr = [list(line.replace('\n', '')) for line in data]
    else:
        arr = [line.replace('\n', '').split(sep) for line in data]
    return arr
