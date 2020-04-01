import collections

T = int(input())
for tc in range(1, T + 1):
    M, N = map(int, input().split())
    s = list(map(int, input().split()))
    check = [0] * M
    que = collections.deque()
    for i in range(M):
        que.append(s[i])
        check[i] = i
    x = M
    n = N
    flag = False
    while 1:
        for i in range(M):
            if que[i] == 0:
                continue
            que[i] = que[i] // 2
            if que[i] == 0:
                if x < N:
                    que[i] = s[x]
                    check[i] = x
                    x += 1
                    n -= 1
                else:
                    n -= 1
            if n == 1:
                flag = True
                break
        if flag:
            break
    for i in range(M):
        if que[i] != 0:
            print('#{} {}'.format(tc, check[i] + 1))
            break