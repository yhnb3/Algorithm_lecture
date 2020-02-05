# import sys
# sys.stdin = open('DFS&BFS.txt')

import sys
sys.setrecursionlimit(10**6)


N, T, start = map(int, input().split())
s = [[0] * (N + 1) for i in range(N + 1)]

for k in range(T):
    i, j = map(int, input().split())
    s[i][j] = 1

def dfs_move(a):
    print(a, end=' ')
    visited[a] = 1
    for i in range(1, N + 1):
        if s[a][i] == 1 or s[i][a] == 1:
            if visited[i] == 0:
                dfs_move(i)

def bfs_move(a):
    print(a, end=' ')
    visited[a] = 1
    for i in range(1, N+1):
        if s[a][i] == 1 or s[i][a] == 1:
            if visited[i] == 0:
                visited[i] = 1
                sss.append(i)
    if sss:
        bfs_move(sss.pop(0))


visited = [0]*(N+1)
dfs_move(start)
print("")
sss = []
visited = [0]*(N+1)
bfs_move(start)
