# import sys
# sys.stdin = open('broken_calc.txt')
# sys.setrecursionlimit(10 ** 6)


def nu(n, k, a, cnt, check):
    global ans
    if k > n * 10:
        return
    if a > n:
        return
    if a != 0 and n % a == 0 and a != 1 and check:
        if n // a == 1:
            ans = min(ans, cnt + 1)
            return
        else:
            nu(n // a, 1, 0, cnt + 1, 0)
    for i in range(len(usable_num)):
        if usable_num[i] == 0:
            nu(n, k * 10, a + k * usable_num[i], cnt + 1, 0)
        else:
            nu(n, k * 10, a + k * usable_num[i], cnt + 1, 1)


T = int(input())
for test_case in range(1, T + 1):
    usable_num = []
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i]:
            usable_num.append(i)
    N = int(input())
    ans = N
    nu(N, 1, 0, 0, 0)
    if ans == N and N > 10:
        print('#{} {}'.format(test_case, -1))
    elif N < 10 and N in usable_num:
        print('#{} {}'.format(test_case, 2))
    else:
        print('#{} {}'.format(test_case, ans))
