N = int(input())
s = [list(map(int, input().split())) for i in range(N)]
sum_num = [[0] * 3 for i in range(N)]
# def painting(n, a, sum_num):
#     sum_num += s[n][a]
#     if sum_num > min_num[0]:
#         return
#
#     if n == N - 1:
#         min_num[0] = sum_num
#         return
#
#     for i in range(3):
#         if i != a:
#             painting(n + 1, i, sum_num)


# for i in range(3):
#     painting(0, i, 0)
for i in range(N):
    if i == 0:
        for j in range(3):
            sum_num[0][j] = s[0][j]
    else:
        for j in range(3):
            if j == 0:
                sum_num[i][j] = s[i][j] + min(sum_num[i - 1][1], sum_num[i - 1][2])
            elif j == 1:
                sum_num[i][j] = s[i][j] + min(sum_num[i - 1][0], sum_num[i - 1][2])
            elif j == 2:
                sum_num[i][j] = s[i][j] + min(sum_num[i - 1][1], sum_num[i - 1][0])

print(min(sum_num[N - 1]))

