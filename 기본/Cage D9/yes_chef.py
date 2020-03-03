import sys
sys.stdin = open('yes_chef.txt')


def dfs(a, n, result1, result2):
    if n == N:
        return
    if a == 0 and n > N // 2:
        return
    if a == N // 2:
        for i in range(N):
            for j in range(N):
                if i not in check:
                    if j not in check:
                        result1 += S[i][j]
                else:
                    if j in check:
                        result2 += S[i][j]
        if ans[0] > abs(result1 - result2):
            ans[0] = abs(result1 - result2)
        return

    check.append(n)
    dfs(a + 1, n + 1, 0, 0)
    check.pop()
    dfs(a, n + 1, 0, 0)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for i in range(N)]
    check = []
    ans = [1000000000001]
    dfs(0, 0, 0, 0)
    print('#{} {}'.format(test_case, ans[0]))