from randomly_close.randomly_close import random_first, mobile, desktop, find_key


def test_random_first():
    assert random_first(mobile) in range(10)

    assert 4 <= sum(random_first(mobile) for i in range(1000)) / 1000 < 7


def test_find_key():
    layout = [
        [0 , 1, 2, 12],
        [3, 4, 5, 9],
        [6, 7, 8, 10],
        [11, 15, 14, 17]
    ]

    line = [[0, 1, 2, 3, 4, 5]]

    assert find_key(layout, 2) == (0, 2)
    assert find_key(layout, 5) == (1, 2)
    assert find_key(layout, 6) == (2, 0)

    assert find_key(line, 2) == (0, 2)
    assert find_key(line, 5) == (0, 5)


def test_generate_mobile_zone():
    layout = [
        [0 , 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [11, 15, 14]
    ]

    start = 4

    available_zones = [
        [
            [0, 1],
            [3, 4],
            [6, 7],
            [11, 15], # zone left
        ],
        [
            [6, 7, 8],
            [11, 15, 14], # zone down
        ],
        [
            [0, 1, 2],
            [3, 4, 5], # zone up
        ],
        [
            [1, 2],
            [4, 5],
            [7, 8],
            [15, 14] # zone right
        ]
    ]

    zones = generate_zones(start, layout)
    assert all([zone in zones for zone in available_zones])


def test_generate_desktop_zone():
    start = 5
    layout = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ]

    available_zones = [
        [
            [1, 2, 3, 4, 5],
        ],
        [
            [5, 6, 7, 8, 9],
        ]
    ]
    zones = generate_zones(start, layout)
    assert all([zone in zones for zone in available_zones])

    start = 3
    layout = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ]

    available_zones = [
        [
            [1, 2, 3, 4, 5],
        ],
        [
            [3, 4, 5, 6, 7]
        ]
    ]

    zones = generate_zones(start, layout)
    assert all([zone in zones for zone in available_zones])




