import sys
sys.stdin = open('Janghun.txt')


def height(n, sum_height):
    if H == sum_height:
        min_num[0] = sum_height
        return 1
    elif H < sum_height:
        if min_num[0] > sum_height:
            min_num[0] = sum_height
        return 0
    elif n == N:
        return 0
    else:
        if height(n + 1, sum_height + S[n]):
            return 1
        if height(n + 1, sum_height):
            return 1


T = int(input())
for test_case in range(1, T + 1):
    N, H = map(int, input().split())
    S = list(map(int, input().split()))
    min_num = [10001 * N]
    if height(1, S[0]):
        print('#{} {}'.format(test_case, min_num[0] - H))
    elif height(1, 0):
        print('#{} {}'.format(test_case, min_num[0] - H))
    else:
        print('#{} {}'.format(test_case, min_num[0] - H))

