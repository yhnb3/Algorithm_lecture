import sys
sys.stdin = open('farm.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = [[int(x) for x in input()] for i in range(N)]
    sum_num = 0

    for i in range(N // 2):
        for j in range(i + 1):
            if j == 0:
                sum_num += S[i][N // 2]
                sum_num += S[N - 1 - i][N // 2]
            else:
                sum_num += S[i][N // 2 + j]
                sum_num += S[i][N // 2 - j]
                sum_num += S[N - 1 - i][N // 2 + j]
                sum_num += S[N - 1 - i][N // 2 - j]
    for i in range(N):
        sum_num += S[N // 2][i]

    print('#{} {}'.format(test_case, sum_num))
