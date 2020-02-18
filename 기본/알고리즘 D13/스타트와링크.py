import copy

N = int(input())

G = [[0]*(N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    G[i][1:] = list(map(int, input().split()))

s1 = [0] * (N // 2)
s2 = [i for i in range(1, N+1)]
s4 = []
s = []

min_num = 12412445346534


def combi_set(n, k):
    global min_num
    if k == 0:
        sum_1 = 0
        sum_2 = 0
        for i in range(N//2):
            for j in range(i + 1, N//2):
                sum_1 += G[s1[i]][s1[j]] + G[s1[j]][s1[i]]

        for i in range(1, N + 1):
            if i not in s1:
                for j in range(i + 1, N + 1):
                    if j not in s1:
                        sum_2 += G[i][j] + G[j][i]

        if abs(sum_1 - sum_2) == 0:
            min_num = 0

        if min_num > abs(sum_1 - sum_2):
            min_num = abs(sum_1 - sum_2)

    elif n < k:
        return
    else:
        s1[k - 1] = s2[n - 1]
        combi_set(n - 1, k - 1)
        combi_set(n - 1, k)


combi_set(N, N//2)


# for i in range(0, len(s)):
#     sum_1 = 0
#     sum_2 = 0
#     for j in range(N//2):
#         for k in range(j+1, N//2):
#             sum_1 += G[s[0 + i][j]][s[0 + i][k]] + G[s[0 + i][k]][s[0 + i][j]]
#             sum_2 += G[s[1 + i][j]][s[1 + i][k]] + G[s[1 + i][k]][s[1 + i][j]]
#
#     if abs(sum_1 - sum_2) == 0:
#         min_num = 0
#         break
#
#     if min_num > abs(sum_1 - sum_2):
#         min_num = abs(sum_1 - sum_2)

print(min_num)









