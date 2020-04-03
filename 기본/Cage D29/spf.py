import collections

T = int(input())
for tc in range(1, T + 1):
    N, M, start, end = map(int, input().split())
    start = start - 1
    end = end - 1
    ch = [[] for i in range(N)]
    distance = [float('INF')] * N
    distance[start] = 0
    for i in range(M):
        x, y, c = map(int, input().split())
        ch[x - 1].append([y - 1, c])
        ch[y - 1].append([x - 1, c])
    que = collections.deque()
    que.append(start)
    while que:
        x = que.popleft()
        for i in ch[x]:
            if distance[i[0]] > distance[x] + i[1]:
                que.append(i[0])
                distance[i[0]] = distance[x] + i[1]
    print('#{} {}'.format(tc, distance[end]))
