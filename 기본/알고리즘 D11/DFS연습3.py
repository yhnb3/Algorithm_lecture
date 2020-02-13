T = 7

s = list(map(int, input().split(',')))
graph = [[0] * T for i in range(T)]
visit = [0] * 7

for i in range(0, len(s), 2):
    graph[s[i] - 1][s[i + 1] - 1] = 1

def dfs(a):
    for i in range(T):
        if not visit[i] and (graph[a][i] or graph[i][a]):
            visit[i] = 1
            print('-{}'.format(i+1), end='')
            dfs(i)


print('-1', end='')
visit[0] = 1
dfs(0)






