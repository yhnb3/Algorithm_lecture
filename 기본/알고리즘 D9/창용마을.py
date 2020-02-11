import sys
from typing import List, Any, Union

sys.stdin = open('창용마을.txt')

T = int(input())

def rel_ser(a, n, c):
    visit[a] = 1
    for i in range(1, n+1):
        if s[a][i] == 1 or s[i][a] == 1:
            if visit[i] == 0:
                rel_ser(i, n, c)

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    visit = [0] * (N + 1)
    s = [[0] * (N + 1) for i in range(N + 1)]
    count = 0

    for i in range(M):
        k, h = map(int, input().split())
        s[k][h] = 1

    for i in range(1, N + 1):
        if visit[i] == 0:
            rel_ser(i, N, count)
            count += 1

    print('#{} {}'.format(test_case, count))


