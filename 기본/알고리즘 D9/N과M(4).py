N, M = map(int, input().split())

arr =[0]*M

def nnm4(n, m, k, q):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(q, N + 1):
        arr[k] = i
        nnm4(n, m, k + 1, i)

nnm4(N, M, 0, 1)


