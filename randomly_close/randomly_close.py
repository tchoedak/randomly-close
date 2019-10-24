import random


directions = ['up', 'down', 'left', 'right']

minimum_random_keys_count = 5

mobile = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None]
]

desktop = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]


def random_first(layout):
    '''
    Select a random key within the layout
    '''
    keys = []
    for line in layout:
        for key in line:
            if key is not None:
                keys.append(key)

    return random.choice(keys)


def find_key(layout, search_key):
    '''
    Find a key within a layout and return the index of that key
    '''
    for i, line in enumerate(layout):
        for j, key in enumerate(line):
            if key == search_key:
                return j, i


def randomly_close(n, layout=mobile):
    '''
    Generate a sequence of numbers that are near each other, randomly.

    :param n: length of the desired sequence
    :param layout: layout of the possible keypad
    '''
    start = random_first(layout)
    print('We are starting with a layout of:\n')
    for line in layout:
        print(line)

    print(f'\nRandom key selected {start} \n')

    if len(layout) == 1:
        range_limiter = 5 # increase the range limiter when working with a horizontal keypad
    else:
        range_limiter = 2

    x, y = find_key(layout, start)

    direction = random.choice(available_directions(x, y, layout))
    print(f'Direction is... {direction}. Searching\n')

    sublayout = available_sublayout(x, y, direction, layout, range_limiter)

    print(f'The sublayout selected after searching {direction} is:\n')

    for line in sublayout:
        print(line)


    sequence = random_sequence(sublayout, n)
    print(f'\nFrom this sublayout we have generated a sequence of {sequence}')
    return sequence

def available_directions(x, y, layout):
    '''
    Calculate the available directions of a key in index [y][x] within the layout.
    Directions are available if it is possible to move an index by at least 1
    in that direction
    '''
    directions = []
    try:
        if x-1 >= 0:
            key = layout[y][x-1]
            if key is not None:
                directions.append('left')
    except IndexError:
        pass

    try:
        key = layout[y][x+1]
        if key is not None:
            directions.append('right')
    except IndexError:
        pass

    try:
        if y-1 >= 0:
            key = layout[y-1][x]
            if key is not None:
                directions.append('up')
    except IndexError:
        pass

    try:
        key = layout[y+1][x]
        if key is not None:
            directions.append('down')
    except IndexError:
        pass

    print(f'available directions are: {directions}\n')
    return directions


def check_depth(x, y, direction, layout):
    '''
    Check how deep the layout is relative to the index x,y in a specific direction
    '''
    increment = 0
    depth = 0

    if direction == 'up':
        depth = y

    if direction == 'left':
        depth = x

    if direction == 'down':
        for i in range(5):
            try:
                increment += 1
                layout[y + increment][x]
            except IndexError:
                increment -= 1
                depth = increment

    if direction == 'right':
        for i in range(5):
            try:
                increment += 1
                layout[y][x+increment]
            except IndexError:
                increment -= 1
                depth = increment

    print(f'Depth discovered in direction {direction} is {depth}\n')
    return depth


def available_sublayout(x, y, direction, layout, range_limiter=2):
    '''
    Given a direction to search, calculate the sublayout that is available
    start from the index x,y in the layout
    '''
    depth = check_depth(x, y, direction, layout)
    search_depth = min(range_limiter, depth)

    if direction in ('up', 'down'):
        left_depth = check_depth(x, y, 'left', layout)
        right_depth = check_depth(x, y, 'right', layout)

        if left_depth == 0:
            x_start = x
        else:
            x_start = x - left_depth
        if right_depth == 0:
            x_end = x
        else:
            x_end = x + right_depth

        x_range = (x_start, x_end)

        if direction == 'up':
            if search_depth >= 2:
                y_start = y - search_depth
                y_end = y-1
            else:
                y_start = y - search_depth
                y_end = y

        if direction == 'down':
            if search_depth >= 2:
                y_start = y + 1
                y_end = y + search_depth
            else:
                y_start = y
                y_end = y + search_depth

        y_range = (y_start, y_end)


    elif direction in ('left', 'right'):
        up_depth = check_depth(x, y, 'up', layout)
        down_depth = check_depth(x, y, 'down', layout)

        if up_depth == 0:
            y_start = y
        else:
            y_start = y - min(up_depth, range_limiter)

        if down_depth == 0:
            y_end = y
        else:
            y_end = y + min(down_depth, range_limiter)

        y_range = (y_start, y_end)

        if direction == 'left':
            if search_depth >= 2:
                x_start = x - search_depth
                x_end = x - 1
            else:
                x_start = x - search_depth
                x_end = x

        if direction == 'right':
            if search_depth >= 2:
                x_start = x + 1
                x_end = x + search_depth
            else:
                x_start = x
                x_end = x + search_depth

        x_range = (x_start, x_end)

    return sublayout_from_range(x_range, y_range, layout)



def sublayout_from_range(x_range, y_range, layout):
    '''
    Generate the sublayout from possible x and y ranges in indices
    '''
    sublayout = []
    y_start, y_end = y_range
    x_start, x_end = x_range
    for y in range(y_start, y_end + 1):
        subsublayout = []
        for x in range(x_start, x_end + 1):
            subsublayout.append(layout[y][x])

        sublayout.append(subsublayout)
    return sublayout


def random_sequence(layout, n):
    '''
    Generate a random sequence from a layout
    '''
    sequence = []

    flattened = [
        key for line in layout for key in line if key is not None
    ]

    print(f'Possible Sequence is.. {flattened}')
    for i in range(n):
        sequence.append(random.choice(flattened))

    return sequence



