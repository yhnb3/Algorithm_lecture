import sys
sys.stdin = open('숫자배열회전.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    s = [list(map(int, input().split())) for i in range(N)]

    s_90 = [[0] * N for i in range(N)]
    s_180 = [[0] * N for i in range(N)]
    s_270 = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N - 1, -1, -1):
            s_90[i][-j + (N - 1)] = s[j][i]

    for i in range(N):
        for j in range(N):
            s_180[i][j] = s[-i + (N - 1)][-j + (N - 1)]

    for i in range(N):
        for j in range(N):
            s_270[i][j] = s[j][-i + (N - 1)]

    print('#{}'.format(test_case))
    for j in range(N):
        for i in range(N):
            print(s_90[j][i], end='')
        print(' ', end='')
        for h in range(N):
            print(s_180[j][h], end='')
        print(' ', end='')
        for k in range(N):
            print(s_270[j][k], end='')
        print()