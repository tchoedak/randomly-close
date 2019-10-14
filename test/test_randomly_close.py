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
