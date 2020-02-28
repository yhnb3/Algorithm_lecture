N = int(input())
S = [0] + [int(input()) for i in range(N)]
result = [[-1] * 3 for i in range(N + 1)]

result[1][1] = S[1]
if N > 1:
    result[2][1] = S[2]
    result[2][2] = S[2] + S[1]
    max_num = result[2][2]
else:
    max_num = S[1]
# dp = [0] * (N + 1)
# dp[1] = S[1]
# if N > 1:
#     dp[2] = S[1] + S[2]

for i in range(3, N + 1):
    result[i][1] = max(max(result[i - 3]), max(result[i - 2])) + S[i]
    result[i][2] = max(result[i - 1][1] + S[i], max(result[i - 3]) + S[i - 1])
    if max(result[i]) > max_num:
        max_num = max(result[i])

# for i in range(3, N + 1):
#     dp[i] = max(dp[i - 1], max(dp[i - 2] + S[i], dp[i - 3] + S[i - 1] + S[i]))
#
#
# print(dp[N])
print(max_num)
