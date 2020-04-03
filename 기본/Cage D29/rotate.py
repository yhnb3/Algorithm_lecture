T = int(input())
for tc in range(1, T + 1):
    N, M = map(int(input()))
    s = list(map(int, input().split()))
    print('#{} {}'.format(tc, s[M % N - 1]))