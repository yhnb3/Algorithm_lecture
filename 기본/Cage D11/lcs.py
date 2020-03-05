import sys
sys.setrecursionlimit(10 ** 6)


s1 = input()
s2 = input()
dp = [0] * len(s1)


def dfs(n, yy):
    if n == len(s1):
        return 0
    if dp[n] != 0:
        return dp[n]
    ret = 0
    for i in range(yy, len(s2)):
        if s1[n] == s2[i]:
            ret = dfs(n + 1, i + 1) + 1
            dp[n] = ret
            break
    else:
        ret = dfs(n + 1, yy)
    return ret


for i in range(len(s1)):
    dfs(i, 0)
    print(dp)

print(max(dp))
