import sys
sys.stdin = open('treasure_pw.txt')


def make_num(s):
    if s.isdigit():
        return int(s)
    elif s == 'A':
        return 10
    elif s == 'B':
        return 11
    elif s == 'C':
        return 12
    elif s == 'D':
        return 13
    elif s == 'E':
        return 14
    elif s == 'F':
        return 15


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    S = input()
    count = []
    for i in range(N - 1, N - 1 - (3 * (N // 4)) - 1, - (N // 4)):
        for j in range(N // 4):
            result = 0
            for k in range(N // 4):
                result += (16 ** k) * make_num(S[i - j - k])
            if result not in count:
                count.append(result)

    ans = sorted(count, reverse=True)
    print('#{} {}'.format(test_case, ans[K - 1]))



