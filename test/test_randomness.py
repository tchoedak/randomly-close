from randomly_close.randomly_close import randomly_close


# NOTE: this test is very expensive to execute on a machine

def test_randomness_length_five():
    iterations = []

    sequence = randomly_close(5)

    for i in range(30):
        for j in range(1000000):
            if randomly_close(5) == sequence:
                iterations.append(j)
                break

    print('After testing 30 times, the iteration distribution is')
    print(iterations)

    avg = sum(iterations) / float(len(iterations))
    print(f'Average number of iterations is {avg}')

