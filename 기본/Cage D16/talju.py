import sys
sys.stdin = open('talju.txt')
import collections

T = int(input())
for test_case in range(1, T + 1):
    N, M, a, b, time = map(int, input().split())
    hole = [list(map(int, input().split())) for i in range(N)]
    delta = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    pipes = [[], [0, 1, 2, 3], [0, 3], [1, 2], [0, 1], [1, 3], [2, 3], [0, 2]]
    visit = [[0] * M for i in range(N)]
    que = collections.deque()
    que.append([a, b, 1])
    visit[a][b] = 1
    ans = 1
    while que:
        x, y, c = que.popleft()
        if c == time:
            continue
        a = hole[x][y]
        for i in pipes[a]:
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if 0 <= dx < N and 0 <= dy < M and (3 - i in pipes[hole[dx][dy]]) and visit[dx][dy] == 0:
                visit[dx][dy] = 1
                que.append([dx, dy, c + 1])
                ans += 1

    print('#{} {}'.format(test_case, ans))




