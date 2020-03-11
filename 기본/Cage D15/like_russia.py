def f(x, y):
    u = 0
    for i in range(x + 1):
        for j in range(M):
            if russia[i][j] != 'W':
                u += 1
    for i in range(x + 1, x + y + 1):
        for j in range(M):
            if russia[i][j] != 'B':
                u += 1
    for i in range(x + y + 1, N):
        for j in range(M):
            if russia[i][j] != 'R':
                u += 1
    return u


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    russia = [list(input()) for i in range(N)]

    ans = N * M
    for i in range(N - 2):
        for j in range(1, N - 1 - i):
            ans = min(f(i, j), ans)

    print('#{} {}'.format(test_case, ans))