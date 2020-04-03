import sys
sys.stdin = open('node_guri.txt')
import collections

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    s = [[] for i in range(V + 1)]
    visit = [0] * (V + 1)
    for i in range(E):
        x, y = map(int, input().split())
        s[x].append(y)
        s[y].append(x)
    start, end = map(int, input().split())
    que = collections.deque()
    que.append(start)
    visit[start] = 1
    while que:
        x = que.popleft()
        if x == end:
            break
        for i in s[x]:
            if visit[i] == 0:
                que.append(i)
                visit[i] = visit[x] + 1
    if visit[end]:
        print('#{} {}'.format(tc, visit[end] - 1))
    else:
        print('#{} {}'.format(tc, visit[end]))