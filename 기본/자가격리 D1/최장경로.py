import sys
sys.stdin = open('최장경로.txt')


T = int(input())


def long_long(x, c):
    global max_distance
    if x == c:
        if max_distance < distance[c]:
            max_distance = distance[c]
        return

    for k in range(1, N + 1):
        if (s[x][k] or s[k][x]) and distance[k] == 0:
            distance[k] = distance[x] + 1
            long_long(k, c)
            distance[k] = 0


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    s = [[0] * (N + 1) for j in range(N + 1)]
    if M == 0:
        print('#{} 1'.format(test_case))
        continue

    for i in range(M):
        a, b = map(int, input().split())
        s[a][b] = 1

    max_distance = 1
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            distance = [0] * (N + 1)
            distance[i] = 1
            long_long(i, j)

    print('#{} {}'.format(test_case, max_distance))