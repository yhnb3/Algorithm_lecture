T = list(input().split())

def perm(n, k):
    if n == k:
        print(T)
        return
    for i in range(k, n):
        T[k], T[i] = T[i], T[k]
        perm(n, k + 1)
        T[k], T[i] = T[i], T[k]


perm(len(T), 0)

