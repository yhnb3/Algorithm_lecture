import sys
sys.stdin = open('파리퇴치.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    fly_map = [list(map(int, input().split())) for i in range(N)]
    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_num = 0
            for k in range(M):
                for h in range(M):
                    sum_num += fly_map[i+k][j+h]
            if sum_num > max_num:
                max_num = sum_num

    print('#{} {}'.format(test_case, max_num))
