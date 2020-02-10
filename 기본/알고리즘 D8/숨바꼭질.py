from collections import deque

que = deque()
N, K = map(int, input().split())
s = [0]*100000
visit = [0]*100001

que.append([N, 0])
temp = [-1, 1]

while que:
    x, count = que.popleft()
    if x == K:
        break

    for i in range(2):
        if 0 <= x + temp[i] <= 100000:
            if visit[x + temp[i]] == 0:
                visit[x + temp[i]] = 1
                que.append([x + temp[i], count + 1])
    if x * 2 <= 100000:
        if visit[x*2] == 0:
            visit[x * 2] = 1
            que.append([x*2, count + 1])

print(count)


