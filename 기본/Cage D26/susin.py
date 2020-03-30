T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = int(input())
    s = set(list(map(int, input().split())))
    re_s = sorted(list(s), reverse=False)
    diff = []
    if M >= len(re_s):
        print('#{} {}'.format(tc, 0))
    else:
        for i in range(1, len(re_s)):
            diff.append(re_s[i] - re_s[i - 1])
        diff.sort(reverse=True)
        print('#{} {}'.format(tc, sum(diff[M - 1:])))
