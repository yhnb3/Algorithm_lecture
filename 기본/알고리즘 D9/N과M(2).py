from collections import deque

N, M = map(int, input().split())

que = deque()
arr = [0] * (M + 1)
q_visit = [0] * (N + 1)
visit = [0] * (N + 1)

def combi(n, m, k, q):
    if k == m:
        for i in range(0, m):
            if i != m - 1:
                print('{}'.format(arr[i]), end=' ')
            else:
                print('{}'.format(arr[i]))
        return 0

    for j in range(q, n + 1):
        if visit[j] == 0:
            visit[j] = 1
            arr[k] = j
            combi(n, m, k + 1, j + 1)
            visit[j] = 0

# que.append(1)
# while que:
#     visit = [0] * (N + 1)
#     x = que.popleft()
#     for i in range(2, N + 1):
#         if q_visit[i] == 0:
#             q_visit[i] = 1
#             que.append(i)

combi(N, M, 0, 1)
