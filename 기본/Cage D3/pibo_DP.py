N = int(input())
S = [-1] * (N + 1)
S[0] = 0
S[1] = 1


def pibo(n):
    if S[n] != -1:
        return S[n]

    else:
        S[n] = pibo(n - 1) + pibo(n - 2)
        return S[n]


print(pibo(N))