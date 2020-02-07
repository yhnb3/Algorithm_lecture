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
    x, y = que.popleft()
    for i in range(4):
        if s[x + dx[i]][y + dy[i]] == 0:
            s[x + dx[i]][y + dy[i]] = s[x][y] + 1
            que.append([x + dx[i], y + dy[i]])

count = 0
for i in range(1, b + 1):
    for j in range(1, a + 1):
        if s[i][j] == 0:
            count += 1

if count == 0:
    if max(max(s)) < 0:
        print(0)
    else:
        print(max(max(s)) - 1)
else:
    print(-1)






