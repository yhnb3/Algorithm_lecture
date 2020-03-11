import sys
sys.stdin = open('pw_attack.txt')


def dfs(n, k, num, check):
    global ans
    if N - n < M - check:
        return
    if check == M:
        if n == N:
            ans += 1
        else:
            ans += (M ** (N - n))
        return
    elif n == N:
        return
    for i in range(M):
        if visit[i] == 0:
            visit[i] += 1
            dfs(n + 1, k * 10, num + k * i, check + 1)
            visit[i] -= 1
        else:
            visit[i] += 1
            dfs(n + 1, k * 10, num + k * i, check)
            visit[i] -= 1


T = int(input())
for test_case in range(1, T + 1):
    M, N = map(int, input().split())
    visit = [0] * M
    dp = [0] * N
    ans = 0
    dfs(0, 1, 0, 0)
    print('#{} {}'.format(test_case, ans % 1000000007))