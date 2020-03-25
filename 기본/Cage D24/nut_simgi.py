T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(M):
            if (i // 2 + j // 2) % 2 == 0:
                ans += 1

    print('#{} {}'.format(tc, ans))


