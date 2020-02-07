from collections import deque
# import sys
# sys.stdin = open('미로탐색.txt')


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


que = deque()
count = 0
a, b = map(int, input().split())
visit = [[0] * (b + 2) for i in range(a + 2)]
maze = [[0]*(b+2) for i in range(a + 2)]
for i in range(1, a + 1):
    s = input()
    for j in range(1, b + 1):
        maze[i][j] = int(s[j-1])

distance = [[0] * (b + 2) for i in range(a + 2)]
que.append([1, 1])
path = []
count = 0
while que:
    x, y = que.popleft()
    if x == a and y == b:
        break

    else:
        for i in range(4):
            if maze[x + dx[i]][y + dy[i]] == 1:
                if visit[x + dx[i]][y + dy[i]] == 0:
                    visit[x + dx[i]][y + dy[i]] = 1
                    distance[x + dx[i]][y + dy[i]] = distance[x][y] + 1
                    que.append([x + dx[i], y + dy[i]])

print(distance[a][b] + 1)








