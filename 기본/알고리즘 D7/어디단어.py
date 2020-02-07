import sys

sys.stdin = open('어디단어.txt')

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())

    s = [[0]*(a+2) for i in range(a+2)]

    for i in range(a):
        u = list(map(int, input().split()))
        for j in range(a):
            s[i+1][j+1] = u[j]


    count = 0
    for i in range(1, a + 1):
        for j in range(1, a - b + 2):
            flag_1 = 0
            flag_2 = 0
            for h in range(b):
                if s[i][j + h] == 1:
                    flag_1 += 1

                if s[j + h][i] == 1:
                    flag_2 += 1

            if flag_1 == b:
                if s[i][j + b] == 0 and s[i][j - 1] == 0:
                    count += 1

            if flag_2 == b:
                if s[j + b][i] == 0 and s[j - 1][i] == 0:
                    count += 1

    print('#{} {}'.format(test_case, count))
