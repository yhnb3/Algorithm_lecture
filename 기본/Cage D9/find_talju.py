# import sys
# sys.stdin = open('find_talju.txt')


def find_talju(x, y, a):
    result.append([x, y])
    count[x][y] = 1
    if a == L:
        return
    if hole[x][y] == 1:
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if i == 2:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 2 or hole[x + dx[i]][y + dy[i]] == 4 or hole[x + dx[i]][y + dy[i]] == 7:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 3:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 5 or hole[x + dx[i]][y + dy[i]] == 6 or hole[x + dx[i]][y + dy[i]] == 2:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 0:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 6 or hole[x + dx[i]][y + dy[i]] == 7 or hole[x + dx[i]][y + dy[i]] == 3:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 1:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 4 or hole[x + dx[i]][y + dy[i]] == 5 or hole[x + dx[i]][y + dy[i]] == 3:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
    elif hole[x][y] == 2:
        for i in [2, 3]:
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if i == 2:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 2 or hole[x + dx[i]][y + dy[i]] == 4 or hole[x + dx[i]][y + dy[i]] == 7:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 3:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 5 or hole[x + dx[i]][y + dy[i]] == 6 or hole[x + dx[i]][y + dy[i]] == 2:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
    elif hole[x][y] == 3:
        for i in [0, 1]:
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if i == 0:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 6 or hole[x + dx[i]][y + dy[i]] == 7 or hole[x + dx[i]][y + dy[i]] == 3:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 1:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 4 or hole[x + dx[i]][y + dy[i]] == 5 or hole[x + dx[i]][y + dy[i]] == 3:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
    elif hole[x][y] == 4:
        for i in [0, 3]:
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if i == 0:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 6 or hole[x + dx[i]][y + dy[i]] == 7 or hole[x + dx[i]][y + dy[i]] == 3:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 3:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 5 or hole[x + dx[i]][y + dy[i]] == 6 or hole[x + dx[i]][y + dy[i]] == 2:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
    elif hole[x][y] == 5:
        for i in [0, 2]:
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if i == 0:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 6 or hole[x + dx[i]][y + dy[i]] == 7 or hole[x + dx[i]][y + dy[i]] == 3:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 2:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 2 or hole[x + dx[i]][y + dy[i]] == 4 or hole[x + dx[i]][y + dy[i]] == 7:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
    elif hole[x][y] == 6:
        for i in [1, 2]:
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if i == 2:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 2 or hole[x + dx[i]][y + dy[i]] == 4 or hole[x + dx[i]][y + dy[i]] == 7:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 1:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 4 or hole[x + dx[i]][y + dy[i]] == 5 or hole[x + dx[i]][y + dy[i]] == 3:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)

    elif hole[x][y] == 7:
        for i in [1, 3]:
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if i == 1:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 4 or hole[x + dx[i]][y + dy[i]] == 5 or hole[x + dx[i]][y + dy[i]] == 3:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)
                elif i == 3:
                    if hole[x + dx[i]][y + dy[i]] == 1 or hole[x + dx[i]][y + dy[i]] == 5 or hole[x + dx[i]][y + dy[i]] == 6 or hole[x + dx[i]][y + dy[i]] == 2:
                        if not count[x + dx[i]][y + dy[i]]:
                            find_talju(x + dx[i], y + dy[i], a + 1)


T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    hole = [list(map(int, input().split())) for i in range(N)]
    count = [[0] * M for i in range(N)]
    result = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    find_talju(R, C, 1)
    print('#{} {}'.format(test_case, len(result)))

    for i in range(N):
        for j in range(M):
            print(count[i][j], end=' ')
        print()