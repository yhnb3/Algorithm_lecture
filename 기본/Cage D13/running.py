import sys
sys.stdin = open('running.txt')


def f(n, visit):
    global ans
    if n == N:
        ans += 1
    for i in range(N):



T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for i in range(M)]
    ans = 0
