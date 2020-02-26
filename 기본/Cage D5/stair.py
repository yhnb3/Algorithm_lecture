N = int(input())
S = [0] + [int(input()) for i in range(N)]
max_num = [0]
s = [[-1] * 3 for i in range(N + 1)]


def stair(n, a):
    if n > N:
        return -10000001
    if s[n][a] != -1:
        return s[n][a]
    if n == N:
        return S[n]
    if a == 2:
        s[n][a] = stair(n + 2, 1) + S[n]
    else:
        s[n][a] = stair(n + 2, 1) + S[n]
        s[n][a] = max(stair(n + 1, a + 1) + S[n], s[n][a])
    return s[n][a]


print(stair(0, 0))