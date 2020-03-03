import sys
sys.stdin = open('perfect_square.txt')
sys.setrecursionlimit(10 ** 6)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for i in range(N)]
    dp = [[1] * N for i in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    idx = [0, 0]
    check = [0] * (N ** 2 + 1)
    max_num = 0
    for j in range(N):
        for k in range(N):
            for i in range(4):
                if 0 <= j + dx[i] < N and 0 <= k + dy[i] < N:
                    if S[j][k] - S[j + dx[i]][k + dy[i]] == -1:
                        check[S[j][k]] = 1
    count = 0
    num = 0
    for i in range(N ** 2, -1, -1):
        if check[i]:
            count += 1
        else:
            if max_num <= count:
                max_num = count
                num = i + 1
            count = 0

    print('#{} {} {}'.format(test_case, num, max_num + 1))