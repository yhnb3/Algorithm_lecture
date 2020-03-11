T = int(input())
dp = [0] * 1000001
for i in range(1, 1000001):
    for j in range(i, 1000001):
        if i * j > 1000000:
            break
        if i == j:
            if i & 1:
                dp[i * j] += i
            continue
        if i & 1:
            dp[i * j] += i
        if j & 1:
            dp[i * j] += j
for i in range(1, 1000000):
    dp[i + 1] += dp[i]

for test_case in range(1, T + 1):
    start, end = map(int, input().split())
    result = 0
    print('#{} {}'.format(test_case, dp[end] - dp[start - 1]))


