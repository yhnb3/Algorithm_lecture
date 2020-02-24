import sys
sys.stdin = open('파핑파핑지뢰찾기.txt')

T = int(input())


def is_zero(x, y, c=0):
    for i in range(8):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            if mine[x + dx[i]][y + dy[i]] == '*':
                c += 1
    return c


def mine_detector(x, y):
    mine[x][y] = 0
    for i in range(8):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            if mine[x + dx[i]][y + dy[i]] not in ['*', 0, 1, 2, 3, 4, 5, 6, 7, 8]:
                temp = is_zero(x + dx[i], y + dy[i])
                if temp == 0:
                    mine_detector(x + dx[i], y + dy[i])
                else:
                    mine[x + dx[i]][y + dy[i]] = temp


for test_case in range(1, T + 1):
    N = int(input())
    mine = [[x for x in input()] for i in range(N)]
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    count = 0
    for i in range(N):
        for j in range(N):
            if mine[i][j] not in ['*', 0, 1, 2, 3, 4, 5, 6, 7, 8]:
                if is_zero(i, j) == 0:
                    mine_detector(i, j)
                    count += 1

    for i in range(N):
        for j in range(N):
            if mine[i][j] == '.':
                count += 1

    print('#{} {}'.format(test_case, count))






