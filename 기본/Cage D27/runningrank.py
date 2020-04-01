def f(x):
    global res
    for i in range(M):
        if visit[s[i][0]] == 0:
            break
    else:
        a = 1
        for j in range(1, N - x + 2):
            a *= j
        res += a
        return
    if x == N:
        res += 1
        return
    for i in range(1, N + 1):
        if visit[i] == 0:
            flag = False
            for j in range(M):
                if i == s[j][1]:
                    if visit[s[j][0]] == 0:
                        flag = True
                        break
            if flag:
                continue
            else:
                visit[i] = 1
                f(x + 1)
                visit[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    s = [list(map(int, input().split())) for i in range(M)]
    visit = [0] * (N + 1)
    res = 0
    f(1)
    print('#{} {}'.format(tc, res))