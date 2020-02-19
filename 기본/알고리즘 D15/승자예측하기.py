import sys
sys.stdin = open('승자예측하기.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    i = 0
    n = N
    x = 1
    while n != 1:
        n = n//2
        i += 1

    if i == 0:
        print('#{} Bob'.format(test_case))

    elif not i & 1:
        for j in range(0, i):
            if not j & 1:
                x = x * 2 + 1
            else:
                x = x * 2
        if N < x:
            print('#{} Alice'.format(test_case))
        else:
            print('#{} Bob'.format(test_case))

    else:
        for j in range(0, i):
            if not j & 1:
                x = x * 2
            else:
                x = x * 2 + 1
        if N >= x:
            print('#{} Alice'.format(test_case))

        else:
            print('#{} Bob'.format(test_case))
