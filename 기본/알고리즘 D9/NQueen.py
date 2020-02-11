N = int(input())

s = [[-1] * (N + 2) for i in range(N + 2)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        s[i][j] = 0
result = [0]

dx = [-1, -1, -1]
dy = [0, -1, 1]


def ymq(x, n, c):
    # test_sum = 0
    # # for i in range(1, N + 1):
    # #     for j in range(1, N + 1):
    # #         print(s[i][j], end=' ')
    # #     print()
    # # print()
    # for i in range(1, N + 1):
    #     for j in range(1, N + 1):
    #         test_sum += s[i][j]
    #
    # if test_sum == N:
    #     result[0] += 1
    #     return
    if c == n:
        result[0] += 1
        return
    # for i in range(1, N + 1):
    for j in range(1, n + 1):
        flag = True
        for k in range(n):
            for h in range(3):
                if 1 <= x + k * dx[h] <= n and 1 <= j + k * dy[h] <= n:
                    if s[x + k * dx[h]][j + k * dy[h]] == 1:
                        flag = False
                        break
            if not flag:
                break

        if flag == True:
            if s[x][j] == 0:
                s[x][j] = 1
                ymq(x + 1, N, c + 1)
                s[x][j] = 0


ymq(1, N, 0)

print(result[0])




