def worm_next(x, y, num):
    for i in range(2):
        if x == worm_hole[num][i][0] and y == worm_hole[num][i][1]:
            pass
        else:
            return worm_hole[num][i][0], worm_hole[num][i][1]


def go_0(x, y, score, direction):  # 오른쪽 진행
    if y == N - 1:  # 재귀 들어오자 마자 벽과 직면 햇을때
        if 6 <= pin_map[x][y] <= 10:
            tx, ty = worm_next(x, y, pin_map[x][y])
            return tx, ty, score + 1, 1
        elif pin_map[x][y] == 2:
            return x, y, score + 2, 2
        elif pin_map[x][y] == 1:
            return x, y, score + 2, 3
    for k in range(1, N):
        if x == start_x and y + k == start_y:  # 제자리로 돌아 왔을때
            return x, y + k, score, -1
        elif pin_map[x][y + k] == -1:  # 블랙홀을 만났을때
            return x, y + k, score, -1
        elif 6 <= pin_map[x][y + k] <= 10:
            tx, ty = worm_next(x, y + k, pin_map[x][y + k])
            return tx, ty, score, direction
        elif 1 <= pin_map[x][y + k] <= 5:
            if pin_map[x][y + k] == 3:
                return x, y + k, score + 1, 2
            elif pin_map[x][y + k] == 4:
                return x, y + k, score + 1, 3
            else:
                return x, y + k, score + 1, 1
        elif y + k == N - 1:
            return x, y + k, score + 1, 1


def go_1(x, y, score, direction):  # 왼쪽 진행
    if y == 0:  # 재귀 들어오자 마자 벽과 직면 햇을때
        if 6 <= pin_map[x][y] <= 10:
            tx, ty = worm_next(x, y, pin_map[x][y])
            return tx, ty, score + 1, 0
        elif pin_map[x][y] == 3:
            return x, y, score + 2, 2
        elif pin_map[x][y] == 4:
            return x, y, score + 2, 3
    for k in range(1, N):
        if x == start_x and y - k == start_y:  # 제자리로 돌아 왔을때
            return x, y - k, score, -1
        elif pin_map[x][y - k] == -1:  # 블랙홀을 만났을때
            return x, y - k, score, -1
        elif 6 <= pin_map[x][y - k] <= 10:
            tx, ty = worm_next(x, y - k, pin_map[x][y - k])
            return tx, ty, score, direction
        elif 1 <= pin_map[x][y - k] <= 5:
            if pin_map[x][y - k] == 1:
                return x, y - k, score + 1, 3
            elif pin_map[x][y - k] == 2:
                return x, y - k, score + 1, 2
            else:
                return x, y - k, score + 1, 0
        elif y - k == N - 1:
            return x, y - k, score + 1, 0


def go_2(x, y, score, direction):  # 아래로 진행
    if x == N - 1:  # 재귀 들어오자 마자 벽과 직면 햇을때
        if 6 <= pin_map[x][y] <= 10:
            tx, ty = worm_next(x, y, pin_map[x][y])
            return tx, ty, score + 1, 3
        elif pin_map[x][y] == 2:
            return x, y, score + 2, 0
        elif pin_map[x][y] == 3:
            return x, y, score + 2, 1
    for k in range(1, N):
        if x + k == start_x and y == start_y:  # 제자리로 돌아 왔을때
            return x + k, y, score, -1
        elif pin_map[x + k][y] == -1:  # 블랙홀을 만났을때
            return x + k, y, score, -1
        elif 6 <= pin_map[x + k][y] <= 10:
            tx, ty = worm_next(x + k, y, pin_map[x + k][y])
            return tx, ty, score, direction
        elif 1 <= pin_map[x + k][y] <= 5:
            if pin_map[x + k][y] == 1:
                return x + k, y, score + 1, 0
            elif pin_map[x + k][y] == 4:
                return x + k, y, score + 1, 1
            else:
                return x + k, y, score + 1, 3
        elif x + k == N - 1:
            return x + k, y, score + 1, 3


def go_3(x, y, score, direction):  # 위로 진행
    if x == 0:  # 재귀 들어오자 마자 벽과 직면 햇을때
        if 6 <= pin_map[x][y] <= 10:
            tx, ty = worm_next(x, y, pin_map[x][y])
            return tx, ty, score + 1, 2
        elif pin_map[x][y] == 1:
            return x, y, score + 2, 0
        elif pin_map[x][y] == 4:
            return x, y, score + 2, 1
    for k in range(1, N):
        if x - k == start_x and y == start_y:  # 제자리로 돌아 왔을때
            return x - k, y, score, -1
        elif pin_map[x - k][y] == -1:  # 블랙홀을 만났을때
            return x - k, y, score, -1
        elif 6 <= pin_map[x - k][y] <= 10:
            tx, ty = worm_next(x - k, y, pin_map[x - k][y])
            return tx, ty, score, direction
        elif 1 <= pin_map[x - k][y] <= 5:
            if pin_map[x - k][y] == 2:
                return x - k, y, score + 1, 0
            elif pin_map[x - k][y] == 3:
                return x - k, y, score + 1, 1
            else:
                return x - k, y, score + 1, 2
        elif x - k == 0:
            return x - k, y, score + 1, 2


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
    i = 4
    j = 3
    h = 0
    start_x = i
    start_y = j
    direc = h
    xx = i
    yy = j
    while 1:
        if h == 0:
            if j + dy[h] == N:
                break
        if h == 1:
            if j + dy[h] < 0:
                break
        if h == 2:
            if i + dx[h] == N:
                break
        if h == 3:
            if i + dx[h] < 0:
                break
        if direc == 0:
            xx, yy, sc, direc = go_0(xx, yy, 0, direc)
            print(xx, yy, direc)
            if direc == -1:
                max_num = max(max_num, sc)
                break
        elif direc == 1:
            xx, yy, sc, direc = go_1(xx, yy, 0, direc)
            print(xx, yy, direc)
            if direc == -1:
                max_num = max(max_num, sc)
                break
        elif direc == 2:
            xx, yy, sc, direc = go_2(xx, yy, 0, direc)
            print(xx, yy, direc)
            if direc == -1:
                max_num = max(max_num, sc)
                break
        elif direc == 3:
            xx, yy, sc, direc = go_3(xx, yy, 0, direc)
            print(xx, yy, direc)
            if direc == -1:
                max_num = max(max_num, sc)
                break
    print()

    print(max_num)
