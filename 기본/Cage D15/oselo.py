def pick(x, y, dx, dy, a):
    tx = x + dx
    ty = y + dy
    if 0 <= tx < N and 0 <= ty < N:
        if abs(a - pan[tx][ty]) == 1:
            stack.append([tx, ty])
            if pick(tx, ty, dx, dy, a):
                return 1
            else:
                return 0
        elif abs(a - pan[tx][ty]) == 0:
            return 1
        else:
            return 0
    else:
        return 0


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for i in range(M)]
    pan = [[-1] * N for i in range(N)]
    pan[N // 2 - 1][N // 2 - 1] = 2
    pan[N // 2 - 1][N // 2] = 1
    pan[N // 2][N // 2 - 1] = 1
    pan[N // 2][N // 2] = 2
    dx = [0, 0, 1, -1, 1, -1, 1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]
    stack = []
    count = [0] * 3
    for i in range(M):
        y, x, c = S[i][0] - 1, S[i][1] - 1, S[i][2]
        pan[x][y] = c
        for j in range(8):
            stack.clear()
            tx = x + dx[j]
            ty = y + dy[j]
            if 0 <= tx < N and 0 <= ty < N:
                if abs(c - pan[tx][ty]) == 1:
                    stack.append([tx, ty])
                    if pick(tx, ty, dx[j], dy[j], c):
                        for k in range(len(stack)):
                            pan[stack[k][0]][stack[k][1]] = c

    for i in range(N):
        for j in range(N):
            if pan[i][j] != -1:
                count[pan[i][j]] += 1

    print('#{} {} {}'.format(test_case, count[1], count[2]))




