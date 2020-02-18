import sys
sys.stdin = open('배열최소합.txt')


def min_func(x, sum_num):
    global min_num
    if sum_num > min_num:
        return

    if x == N:
        if min_num > sum_num:
            min_num = sum_num
        return

    for i in range(N):
        if count[i] == 0:
            sum_num += s[x][i]
            count[i] += 1
            min_func(x + 1, sum_num)
            sum_num -= s[x][i]
            count[i] -= 1


for test_case in range(1, int(input()) + 1):
    N = int(input())
    s = [list(map(int, input().split())) for i in range(N)]
    min_num = 1232354346456345235
    count = [0] * N
    min_func(0, 0)

    print('#{} {}'.format(test_case, min_num))