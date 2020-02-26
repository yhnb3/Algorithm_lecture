import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
S = [-1] * 1000001
S[1] = 1
S[2] = 2


# def make_binary(n):
#     if S[n] != -1:
#         if n > 3:
#             S[n - 1] = 0
#         return S[n]
#
#     else:
#         n1 = make_binary(n - 2)
#         n2 = make_binary(n - 1)
#         S[n] = (n1 + n2) % 15746
#         return S[n]

for i in range(3, N + 1):
    S[i] = (S[i - 1] + S[i - 2]) % 15746

print(S[N])
