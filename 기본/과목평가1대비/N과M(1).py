N, M = map(int, input().split())
s = [0]*M
visit = [0]*(N+1)
array = [0]*(N+1)

for i in range(1, N + 1):
    array[i] = i

def combi(arr, n, m, k):
    if k == m:
        for i in range(len(arr)):
            print(arr[i],end=' ')
        print()
        return

    for i in range(1, n + 1):
        if visit[i] == 0:
            arr[k] = i
            visit[i] = 1
            combi(arr, n, m, k+1)
            visit[i] = 0

combi(s, N, M, 0)

















