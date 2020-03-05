import sys
sys.stdin = open('mountain_road.txt')
import copy


def dfs(x, y, a, k, arr):
    visit[x][y] = 1
    if result[0] < a:
        result[0] = a
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            if visit[x + dx[i]][y + dy[i]] == 0:
                if arr[x][y] > arr[x + dx[i]][y + dy[i]]:
                    dfs(x + dx[i], y + dy[i], a + 1, k, arr)
                    visit[x + dx[i]][y + dy[i]] = 0
                else:
                    if k == 0:
                        for u in range(1, K + 1):
                            if arr[x][y] > arr[x + dx[i]][y + dy[i]] - u:
                                r_arr = copy.deepcopy(arr)
                                r_arr[x + dx[i]][y + dy[i]] = r_arr[x + dx[i]][y + dy[i]] - u
                                dfs(x + dx[i], y + dy[i], a + 1, 1, r_arr)
                                visit[x + dx[i]][y + dy[i]] = 0


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mou = [list(map(int, input().split())) for i in range(N)]
    idx = []
    max_num = 0
    for i in range(N):
        for j in range(N):
            if max_num < mou[i][j]:
                max_num = mou[i][j]
                idx.clear()
                idx.append([i, j])
            elif max_num == mou[i][j]:
                idx.append([i, j])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = [0]

    for i in range(len(idx)):
        visit = [[0] * N for j in range(N)]
        dfs(idx[i][0], idx[i][1], 1, 0, mou)

    print('#{} {}'.format(test_case, result[0]))