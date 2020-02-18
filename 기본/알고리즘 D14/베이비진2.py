idx = [i for i in range(6)]
T = [int(x) for x in input()]


def baby(n, k):
    if n == k:
        if is_baby(0):
            return 1

    for i in range(k, n):
        idx[k], idx[i] = idx[i], idx[k]
        if baby(n, k + 1):
            return 1
        idx[k], idx[i] = idx[i], idx[k]


def is_baby(a):
    for i in range(0, 6, 3):
        if (T[idx[i]] == T[idx[i + 1]] and T[idx[i + 1]] == T[idx[i + 2]]) or (T[idx[i]] + 1 == T[idx[i + 1]] and T[idx[i + 1]] + 1 == T[idx[i + 2]]):
            a += 1
    if a == 2:
        return 1


if baby(6, 0):
    print('베이비진 ! :', end='')
    for i in range(6):
        print(' {}'.format(T[idx[i]]), end='')
    print()
else:
    print('Nooooooooo!')