import copy, collections

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    s = [[int(x) for x in input()] for i in range(N)]
    s_dis = copy.deepcopy(s)
    visit = [[0] * N for i in range(N)]
    que = collections.deque()
    que.append([0, 0])
    visit[0][0] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while que:
        x, y = que.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and visit[x + dx[i]][y + dy[i]] == 0:
                visit[x + dx[i]][y + dy[i]] = 1
                s_dis[x + dx[i]][y + dy[i]] = s_dis[x][y] + s[x + dx[i]][y + dy[i]]
                que.append([x + dx[i], y + dy[i]])
            elif 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and visit[x + dx[i]][y + dy[i]] != 0:
                if s_dis[x + dx[i]][y + dy[i]] > s_dis[x][y] + s[x + dx[i]][y + dy[i]]:
                    s_dis[x + dx[i]][y + dy[i]] = s_dis[x][y] + s[x + dx[i]][y + dy[i]]
                    que.append([x + dx[i], y + dy[i]])

    print('#{} {}'.format(test_case, s_dis[N - 1][N - 1]))

