N = int(input())
S = [[-1] * 10 for i in range(N + 1)]
for i in range(0, 10):
    S[1][i] = 1


def stair(n, a):
    if S[n][a] != -1:
        return S[n][a]
    else:
        if a == 0:
            S[n][a] = (stair(n - 1, a + 1)) % 1000000000
            return S[n][a]
        elif a == 9:
            S[n][a] = stair(n - 1, a - 1) % 1000000000
            return S[n][a]
        else:
            S[n][a] = (stair(n - 1, a - 1) + stair(n - 1, a + 1)) % 1000000000
            return S[n][a]


for i in range(1, 10):
    stair(N, i)
print(sum(S[N][1:10]) % 1000000000)