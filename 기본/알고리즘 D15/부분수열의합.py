import sys
sys.stdin = open('부분수열의합.txt')

T = int(input())


def per_sum(a, sum_num, check):
    if a == len(s):
        return
    if check:
        sum_num += s[a]
    if sum_num > K:
        return

    if sum_num == K:
        result[0] += 1
        return
    else:
        per_sum(a + 1, sum_num, 0)
        per_sum(a + 1, sum_num, 1)


for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    s = list(map(int, input().split()))
    result = [0]

    per_sum(0, 0, 0)
    per_sum(0, 0, 1)

    print('#{} {}'.format(test_case, result[0]))
