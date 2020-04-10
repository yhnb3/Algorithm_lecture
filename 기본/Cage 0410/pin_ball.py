def worm_next(x, y, num):
    for i in range(2):
        if x == worm_hole[num][i][0] and y == worm_hole[num][i][1]:
            pass
        else:
            return worm_hole[num][i][0], worm_hole[num][i][1]


def dfs(x, y, score, start_x, start_y, direction):  # 좌표와 시작한 자리 그리고 방향이 함수에 필요하다.
    global max_num
    if direction == 0:  # 오른쪽으로 진행
        if y == N - 1:  # 재귀 들어오자 마자 벽과 직면 햇을때
            if 6 <= pin_map[x][y] <= 10:
                dx, dy = worm_next(x, y, pin_map[x][y])
                dfs(dx, dy, score + 1, start_x, start_y, 1)
                return
            elif pin_map[x][y] == 1:
                dfs(x, y, score + 2, start_x, start_y, 3)
                return
            elif pin_map[x][y] == 2:
                dfs(x, y, score + 2, start_x, start_y, 2)
                return
        for k in range(1, N):
            if x == start_x and y + k == start_y:  # 제자리로 돌아 왔을때
                max_num = max(max_num, score)  # 가장 높은 점수로 계속 해서 저장
                return
            elif pin_map[x][y + k] == -1:  # 블랙홀을 만났을때
                max_num = max(max_num, score)  # 가장 높은 점수로 계속 해서 저장
                return
            elif 6 <= pin_map[x][y + k] <= 10:
                dx, dy = worm_next(x, y + k, pin_map[x][y + k])
                dfs(dx, dy, score, start_x, start_y, direction)
                return
            elif 1 <= pin_map[x][y + k] <= 5:
                if pin_map[x][y + k] == 3:
                    dfs(x, y + k, score + 1, start_x, start_y, 2)
                    return
                elif pin_map[x][y + k] == 4:
                    dfs(x, y + k, score + 1, start_x, start_y, 3)
                    return
                else:
                    dfs(x, y + k, score + 1, start_x, start_y, 1)
                    return
            elif y + k == N - 1:
                dfs(x, y + k, score + 1, start_x, start_y, 1)  # 벽에 부딪혔을때는 점수+1 방향 반대
                return  # 재귀에서 한번 나오면 다시 들어 갈 필요 없음
    elif direction == 1:  # 왼쪽으로 진행
        if y == 0:
            if 6 <= pin_map[x][y] <= 10:
                dx, dy = worm_next(x, y, pin_map[x][y])
                dfs(dx, dy, score + 1, start_x, start_y, 0)
                return
            elif pin_map[x][y] == 3:
                dfs(x, y, score + 2, start_x, start_y, 2)
                return
            elif pin_map[x][y] == 4:
                dfs(x, y, score + 2, start_x, start_y, 3)
                return
        for k in range(1, N):
            if x == start_x and y - k == start_y:  # 제자리로 돌아 왔을때
                max_num = max(max_num, score)  # 가장 높은 점수로 계속 해서 저장
                return
            elif pin_map[x][y - k] == -1:  # 블랙홀을 만났을때
                max_num = max(max_num, score)  # 가장 높은 점수로 계속 해서 저장
                return
            elif 6 <= pin_map[x][y - k] <= 10:
                dx, dy = worm_next(x, y - k, pin_map[x][y - k])
                dfs(dx, dy, score, start_x, start_y, direction)
                return
            elif 1 <= pin_map[x][y - k] <= 5:
                if pin_map[x][y - k] == 1:
                    dfs(x, y - k, score + 1, start_x, start_y, 3)
                    return
                elif pin_map[x][y - k] == 2:
                    dfs(x, y - k, score + 1, start_x, start_y, 2)
                    return
                else:
                    dfs(x, y - k, score + 1, start_x, start_y, 0)
                    return
            elif y - k == 0:
                dfs(x, y - k, score + 1, start_x, start_y, 0)  # 벽에 부딪혔을때는 점수+1 방향 반대
                return  # 재귀에서 한번 나오면 다시 들어 갈 필요 없음
    elif direction == 2:  # 아래로 진행
        if x == N - 1:
            if 6 <= pin_map[x][y] <= 10:
                dx, dy = worm_next(x, y, pin_map[x][y])
                dfs(dx, dy, score + 1, start_x, start_y, 3)
                return
            elif pin_map[x][y] == 2:
                dfs(x, y, score + 2, start_x, start_y, 0)
                return
            elif pin_map[x][y] == 3:
                dfs(x, y, score + 2, start_x, start_y, 1)
                return
        for k in range(1, N):
            if x + k == start_x and y == start_y:  # 제자리로 돌아 왔을때
                max_num = max(max_num, score)  # 가장 높은 점수로 계속 해서 저장
                return
            elif pin_map[x + k][y] == -1:  # 블랙홀을 만났을때
                max_num = max(max_num, score)  # 가장 높은 점수로 계속 해서 저장
                return
            elif 6 <= pin_map[x + k][y] <= 10:
                dx, dy = worm_next(x + k, y, pin_map[x + k][y])
                dfs(dx, dy, score, start_x, start_y, direction)
                return
            elif 1 <= pin_map[x + k][y] <= 5:
                if pin_map[x + k][y] == 1:
                    dfs(x + k, y, score + 1, start_x, start_y, 0)
                    return
                elif pin_map[x + k][y] == 4:
                    dfs(x + k, y, score + 1, start_x, start_y, 1)
                    return
                else:
                    dfs(x + k, y, score + 1, start_x, start_y, 3)
                    return
            elif x + k == N - 1:
                dfs(x + k, y, score + 1, start_x, start_y, 3)  # 벽에 부딪혔을때는 점수+1 방향 반대
                return  # 재귀에서 한번 나오면 다시 들어 갈 필요 없음
    elif direction == 3:  # 위로 진행
        if x == 0:
            if 6 <= pin_map[x][y] <= 10:
                dx, dy = worm_next(x, y, pin_map[x][y])
                dfs(dx, dy, score + 1, start_x, start_y, 2)
                return
            elif pin_map[x][y] == 1:
                dfs(x, y, score + 2, start_x, start_y, 0)
                return
            elif pin_map[x][y] == 4:
                dfs(x, y, score + 2, start_x, start_y, 1)
                return
        for k in range(1, N):
            if x - k == start_x and y == start_y:  # 제자리로 돌아 왔을때
                max_num = max(max_num, score)  # 가장 높은 점수로 계속 해서 저장
                return
            elif pin_map[x - k][y] == -1:  # 블랙홀을 만났을때
                max_num = max(max_num, score)  # 가장 높은 점수로 계속 해서 저장
                return
            elif 6 <= pin_map[x - k][y] <= 10:
                dx, dy = worm_next(x - k, y, pin_map[x - k][y])
                dfs(dx, dy, score, start_x, start_y, direction)
                return
            elif 1 <= pin_map[x - k][y] <= 5:
                if pin_map[x - k][y] == 2:
                    dfs(x - k, y, score + 1, start_x, start_y, 0)
                    return
                elif pin_map[x - k][y] == 3:
                    dfs(x - k, y, score + 1, start_x, start_y, 1)
                    return
                else:
                    dfs(x - k, y, score + 1, start_x, start_y, 2)
                    return
            elif x - k == 0:
                dfs(x - k, y, score + 1, start_x, start_y, 2)  # 벽에 부딪혔을때는 점수+1 방향 반대
                return  # 재귀에서 한번 나오면 다시 들어 갈 필요 없음


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pin_map = [list(map(int, input().split())) for i in range(N)]
    worm_hole = [[] for i in range(11)]
    for i in range(N):
        for j in range(N):
            if 6 <= pin_map[i][j] <= 10:
                worm_hole[pin_map[i][j]].append([i, j])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    max_num = 0
    for i in range(N):
        for j in range(N):
            if pin_map[i][j] == 0:
                for h in range(4):
                    if 0 <= i + dx[h] < N and 0 <= j + dy[h] < N:
                        dfs(i, j, 0, i, j, h)
    print('#{} {}'.format(tc, max_num))
