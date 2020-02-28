import sys
sys.stdin = open('find_matrix.txt')

T = int(input())


def fm():
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                return i, j
    return N, N


for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]
    result = []

    if N <= 10:
        reps = 5
    elif N <= 40:
        reps = 10
    elif N <= 80:
        reps = 15
    else:
        reps = 20

    for p in range(reps):
        global x, y
        i, j = fm()
        if i == N:
            break
        for h in range(i, N):
            if h == N - 1:
                x = h
                break
            if not matrix[h + 1][j]:
                x = h
                break
        for k in range(j, N):
            if k == N - 1:
                y = k
                break
            if not matrix[i][k + 1]:
                y = k
                break

        result.append([(x - i + 1) * (y - j + 1), x - i + 1, y - j + 1])
        for h in range(i, x + 1):
            for z in range(j, y + 1):
                matrix[h][z] = 0

    ans = sorted(result)

    print('#{} {}'.format(test_case, len(ans)), end='')
    for i in range(len(ans)):
        print(' {} {}'.format(ans[i][1], ans[i][2]), end='')
    print()


