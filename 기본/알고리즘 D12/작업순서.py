import sys
sys.stdin = open('작업순서.txt')

T = 10

def dfs_rank(a):
    for j in range(1, V + 1):
        count = 0
        for z in range(len(s[j])):
            if visit[s[j][z]] != 1:
                count += 1

        if not count and (a in s[j]):
            if visit[j] == 0:
                visit[j] = 1
                result.append(j)
                dfs_rank(j)


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    result = []
    s = [[] for i in range(V + 1)]
    visit = [0] * (V + 1)
    a = list(map(int, input().split()))

    for i in range(0, E*2, 2):
        s[a[i + 1]].append(a[i])

    for k in range(1, V + 1):
        if not s[k]:
            visit[k] = 1
            result.append(k)
            dfs_rank(k)

    print('#{}'.format(test_case), end='')
    for i in range(len(result)):
        print(' {}'.format(result[i]), end='')
    print()
