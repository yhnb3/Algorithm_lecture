import sys, copy
sys.stdin = open('break_block.txt')
import copy


def bomb(yy, r_B, visit):
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


def dfs(n, arr, cnt):
    if n == N or cnt == 0:
        if min_num[0] > cnt:
            min_num[0] = cnt
        return

    r_b = copy.deepcopy(arr)
    for i in range(W):
        visit = [[0] * W for i in range(H)]
        cnt = bomb(i, arr, visit)
        rr_b = sl(arr)
        dfs(n + 1, rr_b, cnt)
        arr = copy.deepcopy(r_b)


T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(H)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    check = []
    min_num = [181]
    dfs(0, B, 181)
    print('#{} {}'.format(test_case, min_num[0]))

