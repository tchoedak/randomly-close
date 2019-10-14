import random


mobile = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None]
]

desktop = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
]


def random_first(layout):
    # layout = mobile or desktop
    keys = []
    for line in layout:
        for key in line:
            if key is not None:
                keys.append(key)

    return random.choice(keys)


def find_key(layout, search_key):
    for i, line in enumerate(layout):
        for j, key in enumerate(line):
            if key == search_key:
                return i, j

def neighbours(layout, key):
    pass

def randomly_close(n, layout=mobile):

    # n = length of password
    start = random_first(layout)

