import sys
# sys.stdin = open('배추지렁이.txt')
sys.setrecursionlimit(10**6)

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def kimchi(a, b):
    ss[a][b] = 0
    for i in range(4):
        if ss[a + dx[i]][b + dy[i]] == 1:
            kimchi(a + dx[i], b + dy[i])



for test_case in range(1, T + 1):

    M, N, K = map(int, input().split())
    ss = [[0]*(M+2) for i in range(N+2)]

    for i in range(K):
        a, b = map(int, input().split())
        ss[b+1][a+1] = 1

    count = 0
    for i in range(1, 1 + N):
        for j in range(1, M + 1):
            if ss[i][j] == 1:
                kimchi(i, j)
                count += 1

    print(count)
