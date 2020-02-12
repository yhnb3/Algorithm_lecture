import sys
sys.stdin = open('농작물수확하기.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    s = [list(input()) for i in range(N)]
    sum_num = 0

    count = [0] * N
    num = 1
    temp = 2
    for i in range(N):
        if num == N:
            temp = temp*(-1)
        count[i] = num
        num = num + temp

    h = N // 2
    k = -1
    for i in range(N):
        if h == 0:
            k = k * -1
        for j in range(count[i]):
            sum_num += int(s[i][j + h])
        h += k

    print('#{} {}'.format(test_case, sum_num))