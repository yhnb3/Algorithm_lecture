import collections
for tc in range(1, 11):
    N, start = map(int, input().split())
    s = [[] for i in range(101)]
    l = list(map(int, input().split()))
    for i in range(0, N, 2):
        if l[i + 1] not in s[l[i]]:
            s[l[i]].append(l[i + 1])
    visit = [0] * 101
    que = collections.deque()
    dis = [0] * 101
    que.append([start, dis[start]])
    visit[start] = 1
    max_d = 0
    while que:
        x, d = que.popleft()
        dis[x] = d
        max_d = max(d, max_d)
        for i in s[x]:
            if visit[i] == 0:
                visit[i] = 1
                que.append([i, d + 1])

    for i in range(100, 0, -1):
        if dis[i] == max_d:
            print('#{} {}'.format(tc, i))
            break

