N = int(input())
S = list(map(int, input().split()))
dp = [0] * N
dp[N - 1] = S[N - 1]
for i in range(N - 2, -1, -1):
    dp[i] = max(dp[i + 1] + S[i], S[i])

print(max(dp))