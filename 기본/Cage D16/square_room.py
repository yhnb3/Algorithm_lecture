def f(x, y, a):
    global ans
    ans = max(ans, a)
    if dp[sq[x][y]]:
        ans = a + dp[sq[x][y]] - 1
        return
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if sq[tx][ty] - sq[x][y] == 1:
                    f(tx, ty, a + 1)
                    return


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sq = [list(map(int, input().split())) for i in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dp = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            if dp[sq[i][j]] == 0:
                ans = 0
                f(i, j, 1)
                dp[sq[i][j]] = ans
    temp = max(dp)
    for i in range(1, N * N + 1):
        if temp == dp[i]:
            print('#{} {} {}'.format(test_case, i, temp))
            break


