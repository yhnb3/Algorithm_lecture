import collections

N, M = map(int, input().split())
miro = [[int(x) for x in input()] for i in range(N)]
que = collections.deque()
que.append([0, 0])
distance = [[0] * M for i in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
distance[0][0] = 1
while que:
    x, y = que.popleft()
    if x == N - 1 and y == M - 1:
        break
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M and distance[x + dx[i]][y + dy[i]] == 0 and miro[x + dx[i]][y + dy[i]] == 1:
            que.append([x + dx[i], y + dy[i]])
            distance[x + dx[i]][y + dy[i]] = distance[x][y] + 1

print(distance[N - 1][M - 1])