from collections import deque

N, M = map(int, input().split())

s = [[-1]*(M + 2) for i in range(N + 2)]
min_string = []

for i in range(1, N + 1):
    a = input()
    for j in range(1, M + 1):
        s[i][j] = int(a[j - 1])

distance = [[0]*(M + 2) for i in range(N + 2)]
bomb_distance = [[0]*(M + 2) for i in range(N + 2)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = deque()
que.append([1, 1, -1])
distance[1][1] = 1

while que:
    x, y, wall = que.popleft()
    if x == N and y == M:
        if wall == 1:
            min_string.append(bomb_distance[N][M])
        else:
            min_string.append(distance[N][M])
        break

    if wall == 1:
        for i in range(4):
            if s[x + dx[i]][y + dy[i]] == 0:
                if bomb_distance[x + dx[i]][y + dy[i]] == 0:
                    bomb_distance[x + dx[i]][y + dy[i]] = bomb_distance[x][y] + 1
                    que.append([x + dx[i], y + dy[i], 1])
    else:
        for i in range(4):
            if s[x + dx[i]][y + dy[i]] == 0:
                if distance[x + dx[i]][y + dy[i]] == 0:
                    distance[x + dx[i]][y + dy[i]] = distance[x][y] + 1
                    que.append([x + dx[i], y + dy[i], 0])
            elif s[x + dx[i]][y + dy[i]] == 1:
                if distance[x + dx[i]][y + dy[i]] == 0:
                    bomb_distance[x + dx[i]][y + dy[i]] = distance[x][y] + 1
                    que.append([x + dx[i], y + dy[i], 1])

if min_string:
    print(min(min_string))

else:
    print(-1)
