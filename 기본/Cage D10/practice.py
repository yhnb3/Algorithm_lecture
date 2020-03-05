def bomb(yy, r_B):
    for j in range(H):
        if r_B[j][yy]:
            if r_B[j][yy] > 1:
                check.append([j, yy, r_B[j][yy]])
            else:
                r_B[j][yy] = 0
            break
    while check:
        x, y, z = check.pop()
        r_B[x][y] = 0
        for i in range(4):
            for k in range(1, z):
                if 0 <= x + k * dx[i] < H and 0 <= y + k * dy[i] < W:
                    if r_B[x + k * dx[i]][y + k * dy[i]] > 1 and visit[x + k * dx[i]][y + k * dy[i]] == 0:
                        visit[x + k * dx[i]][y + k * dy[i]] = 1
                        check.append([x + k * dx[i], y + k * dy[i], r_B[x + k * dx[i]][y + k * dy[i]]])
                    else:
                        r_B[x + k * dx[i]][y + k * dy[i]] = 0
    cnt = 0
    for i in range(H):
        for j in range(W):
            if r_B[i][j]:
                cnt += 1
    return cnt


def sl(arr):
    for i in range(W):
        temp = -1
        j = H - 1
        while j >= 0:
            if not arr[j][i]:
                if temp == -1:
                    temp = j
            else:
                if temp != -1:
                    arr[j][i], arr[temp][i] = arr[temp][i], arr[j][i]
                    j = temp
                    temp = -1
            j -= 1
    return arr


T = int(input())
N, W, H = map(int, input().split())
B = [list(map(int, input().split())) for i in range(H)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
check = []
visit = [[0] * W for i in range(H)]
min_num = [181]
bomb(2, B)
sl(B)
bomb(2, B)
sl(B)
for j in range(H):
    for k in range(W):
        print(B[j][k], end=' ')
    print()
print()
bomb(6, B)
sl(B)
for j in range(H):
    for k in range(W):
        print(B[j][k], end=' ')
    print()
print()
