N, M = map(int, input().split())
arr = [0]*M

def combi(n, m, k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return 0

    for j in range(1, N + 1):
        arr[k] = j
        combi(n, m, k + 1)

combi(N, M, 0)