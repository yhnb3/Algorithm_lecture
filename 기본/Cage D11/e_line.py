N = int(input())
line = [list(map(int, input().split())) for i in range(N)]
dp = [0] * N
dp[0] = 1
e_line = sorted(line)
max_num = 0
ans = 0

for i in range(0, N):
    max_num = 0
    for j in range(i):
        if e_line[i][1] > e_line[j][1]:
            if dp[j] > max_num:
                max_num = dp[j]
        dp[i] = max_num + 1
    if dp[i] > ans:
        ans = dp[i]
print(N - ans)



