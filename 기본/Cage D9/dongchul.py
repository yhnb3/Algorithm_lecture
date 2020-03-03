import sys
sys.stdin = open('dongchul.txt')


def tsp(n, a, visit):
    if visit == (1 << N) - 1:
        return P[n][a] / 100
    if cache[a][visit]:
        return cache[a][visit]
    temp = 0
    for i in range(N):
        if visit & (1 << i) == 0:
            temp = max(temp, tsp(n + 1, i, visit | (1 << i)) * P[n][a] / 100)
    cache[a][visit] = temp
    return temp


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for i in range(N)]
    cache = [[None] * (1 << N) for i in range(N)]
    max_num = 0
    for i in range(N):
        if max_num < tsp(0, i, 1 << i):
            max_num = tsp(0, i, 1 << i)

    print('#{} {:.6f}'.format(test_case, max_num * 100))

