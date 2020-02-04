import sys
sys.stdin = open('색칠하기.txt')

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    s = [[0]*5 for i in range(num)]
    for i in range(num):
        s[i] = list(map(int, input().split()))

    p = [[0]*10 for i in range(10)]
    for i in range(num):
        if s[i][-1] == 1:
            for j in range(s[i][0], s[i][2]+1):
                for h in range(s[i][1], s[i][3]+1):
                    p[h][j] += 1
        else:
            for j in range(s[i][0], s[i][2]+1):
                for h in range(s[i][1], s[i][3]+1):
                    p[h][j] += 1

    count = 0
    for i in range(10):
        for j in range(10):
            if p[i][j] == 2:
                count += 1

    print('#{} {}'.format(test_case, count))



