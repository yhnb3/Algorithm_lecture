import collections, sys
sys.stdin = open('miro_guri.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    miro = [[0] * N for i in range(N)]
    visit = [[0] * N for i in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    start = [0, 0]
    end = [0, 0]
    for i in range(N):
        a = input()
        for j in range(N):
            miro[i][j] = int(a[j])
            if int(a[j]) == 2:
                start = [i, j]
            if int(a[j]) == 3:
                end = [i, j]
    que = collections.deque()
    que.append(start)
    visit[start[0]][start[1]] = 1
    while que:
        x, y = que.popleft()
        if [x, y] == end:
            break
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and visit[x + dx[i]][y + dy[i]] == 0 and miro[x + dx[i]][y + dy[i]] != 1:
                visit[x + dx[i]][y + dy[i]] = visit[x][y] + 1
                que.append([x + dx[i], y + dy[i]])
    if visit[end[0]][end[1]]:
        print('#{} {}'.format(tc, visit[end[0]][end[1]] - 2))
    else:
        print('#{} {}'.format(tc, visit[end[0]][end[1]]))


