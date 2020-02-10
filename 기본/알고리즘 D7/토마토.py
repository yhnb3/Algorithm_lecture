from collections import deque

que = deque()
a, b = map(int, input().split())
s = [[-1]*(a+2) for i in range(b+2)]

for i in range(1, b + 1):
    d = list(map(int, input().split()))
    for j in range(1, a + 1):
        s[i][j] = d[j-1]


for i in range(1, b + 1):
    for j in range(1, a + 1):
        if s[i][j] == 1:
            que.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while que:
    s_test = que.popleft()
    x, y = s_test[0], s_test[1]
    for i in range(4):
        if s[x + dx[i]][y + dy[i]] == 0:
            s[x + dx[i]][y + dy[i]] = s[x][y] + 1
            que.append([x + dx[i], y + dy[i]])

count = 0

for i in range(1, b + 1):
    for j in range(1, a + 1):
        if s[i][j] == 0:
            count += 1

max_num = 0
for i in range(b+2):
    max_num = max(max_num, max(s[i]))


if count == 0:
    if max_num < 0:
        print(0)
    else:
        print(max_num - 1)
else:
    print(-1)






