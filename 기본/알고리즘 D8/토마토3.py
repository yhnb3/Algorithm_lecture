from collections import deque

que = deque()
N, M, H = map(int, input().split())

s = [[[-1]*(N + 2) for i in range(M + 2)] for j in range(H + 2)]


for i in range(1, H + 1):
    for j in range(1, M + 1):
        a = list(map(int, input().split()))
        for k in range(1, N + 1):
            s[i][j][k] = a[k-1]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(1, H + 1):
    for j in range(1, M + 1):
        for k in range(1, N + 1):
            if s[i][j][k] == 1:
                que.append([i, j, k])

while que:
    x, y, z = que.popleft()
    for i in range(6):
        if s[x + dx[i]][y + dy[i]][z + dz[i]] == 0:
            s[x + dx[i]][y + dy[i]][z + dz[i]] = s[x][y][z] + 1
            que.append([x + dx[i], y + dy[i], z + dz[i]])

count = 0
for i in range(1, H + 1):
    for j in range(1, M + 1):
        for k in range(1, N + 1):
            if s[i][j][k] == 0:
                count += 1

max_num = 0
for i in range(1, H + 1):
    for j in range(1, M + 1):
        for k in range(1, N + 1):
            if s[i][j][k] > max_num:
                max_num = s[i][j][k]

if count > 0:
    print(-1)
else:
    if max_num < 0:
        print(0)
    else:
        print(max_num - 1)
