N = int(input())
s = [list(map(int, input().split())) for i in range(N)]
sum_num = [[0] * N for i in range(N)]

for i in range(N):
    if i == 0:
        sum_num[i][0] = s[i][0]
    else:
        for j in range(i + 1):
            if j != 0:
                sum_num[i][j] = s[i][j] + max(sum_num[i - 1][j - 1], sum_num[i - 1][j])
            else:
                sum_num[i][j] = s[i][j] + sum_num[i - 1][j]

print(max(sum_num[N - 1]))


