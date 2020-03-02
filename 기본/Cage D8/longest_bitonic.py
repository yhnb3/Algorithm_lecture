N = int(input())
S = list(map(int, input().split()))

dp = [[0] * 2 for i in range(N)]
dp[0][0], dp[0][1] = 1, 1

b = max(S)
max_num = 1
for i in range(1, N):
    max_up = -1
    max_down = -1
    for j in range(i):
        if S[j] < S[i]:
            if max_up < dp[j][0]:
                max_up = dp[j][0]
        elif S[j] > S[i]:
            if max_down < max(dp[j]):
                max_down = max(dp[j])

    if max_up != -1:
        dp[i][0] = max_up + 1
    else:
        dp[i][0] = 1

    if max_down != -1:
        dp[i][1] = max_down + 1
    else:
        dp[i][1] = 1

    if max_num < max(dp[i]):
        max_num = max(dp[i])

print(max_num)








