N = int(input())
S = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1
max_num = 1

for i in range(1, N):
    max_sub = 0
    max_idx = -1
    for j in range(i):
        if S[i] > S[j]:
            if max_sub < dp[j]:
                max_sub = dp[j]
                max_idx = j
    if max_idx != -1:
        dp[i] = max_sub + 1
    else:
        dp[i] = 1
    if max_num < dp[i]:
        max_num = dp[i]

print(max_num)




