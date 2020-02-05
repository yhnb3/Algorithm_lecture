import sys

sys.stdin = open('파스칼삼각형.txt')

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    s = [[0]*num for i in range(num)]
    s[0][0] = 1
    if num > 1:
        s[1][0], s[1][1] = 1, 1
        for i in range(2, num):
            s[i][0], s[i][i] = 1, 1
            for j in range(1, i):
                s[i][j] = s[i - 1][j - 1] + s[i - 1][j]

        print('#{}'.format(test_case))
        for i in range(num):
            for j in range(num):
                if s[i][j] != 0:
                    print(s[i][j], end=' ')
            print("")
    else:
        print('#{}'.format(test_case))
        print(1)

