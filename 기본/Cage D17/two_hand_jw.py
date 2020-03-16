import sys
sys.stdin = open('two_hand_jw.txt')


def f(n, a, b):
    global ans
    if K - (a + b) < (a - b):
        result = 1
        for i in range(1, N - n + 1):
            result *= i
        result = result * (2 ** (N - n))
        ans += result
        return
    if n == N:
        ans += 1
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            f(n + 1, a + kg[i], b)
            visit[i] = 0
            if b + kg[i] <= a:
                visit[i] = 1
                f(n + 1, a, b + kg[i])
                visit[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    visit = [0] * N
    kg = list(map(int, input().split()))
    ans = 0
    K = sum(kg)
    f(0, 0, 0)
    print('#{} {}'.format(test_case, ans))