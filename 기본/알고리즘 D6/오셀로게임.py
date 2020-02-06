import sys

sys.stdin = open('오셀로게임.txt')

T = int(input())


def black(a, b, c, count):
    if pan[a + dx[c] * count][b + dy[c] * count] == 2:
        if black(a, b, c, count + 1):
            return 1

        else:
            pan[a + dx[c] * count][b + dy[c] * count] = 1
            return 0

    elif pan[a + dx[c] * count][b + dy[c] * count] == 1:
        return 0
    else:
        return 1


def white(a, b, c, count):
    if pan[a + dx[c] * count][b + dy[c] * count] == 1:
        if white(a, b, c, count + 1):
            return 1
        else:
            pan[a + dx[c] * count][b + dy[c] * count] = 2
            return 0

    elif pan[a + dx[c] * count][b + dy[c] * count] == 2:
        return 0

    else:
        return 1


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pan = [[0] * (N + 2) for i in range(N + 2)]
    pan[1 + (N - 2) // 2][1 + (N - 2) // 2] = 2
    pan[N - (N - 2) // 2][N - (N - 2) // 2] = 2
    pan[1 + (N - 2) // 2][N - (N - 2) // 2] = 1
    pan[N - (N - 2) // 2][1 + (N - 2) // 2] = 1
    s = [list(map(int, input().split())) for i in range(M)]
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    num_1 = 0
    num_2 = 0

    for i in range(M):
        j = 0
        if s[i][2] == 1:
            pan[s[i][0]][s[i][1]] = 1
            while j < 8:
                black(s[i][0], s[i][1], j, 1)
                j += 1
        elif s[i][2] == 2:
            pan[s[i][0]][s[i][1]] = 2
            while j < 8:
                white(s[i][0], s[i][1], j, 1)
                j += 1
    for i in range(N + 2):
        for j in range(N + 2):
            if pan[i][j] == 1:
                num_1 += 1
            elif pan[i][j] == 2:
                num_2 += 1

    print('#{} {} {}'.format(test_case, num_1, num_2))
