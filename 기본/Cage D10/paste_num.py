

def f(x, y, n, k, ans):
    ans += k * S[x][y]
    if n == 7:
        if ans not in result:
            result.append(ans)
            ans -= k * S[x][y]
        else:
            ans -= k * S[x][y]
        return

    for h in range(4):
        if 0 <= x + dx[h] < 4 and 0 <= y + dy[h] < 4:
            f(x + dx[h], y + dy[h], n + 1, k * 10, ans)
    ans -= k * S[x + dx[h]][y + dy[h]]


T = int(input())
for test_case in range(1, T + 1):
    S = [list(map(int, input().split())) for i in range(4)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = []
    for i in range(4):
        for j in range(4):
            f(i, j, 1, 1, 0)

    print('#{} {}'.format(test_case, len(result)))