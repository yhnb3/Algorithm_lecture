s1 = input()
s2 = input()
dp = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]

idx = []
for i in range(len(s1) - 1, -1, -1):
    for j in range(len(s2) - 1, -1, -1):
        if s1[i] == s2[j]:
            max_num = max(dp[len(s1)][j + 1:])
            dp[i][j] = max_num + 1
            idx.append(j)
    while idx:
        a = idx.pop()
        dp[len(s1)][a] = max(dp[len(s1)][a], dp[i][a])


print(max(dp[len(s1)]))