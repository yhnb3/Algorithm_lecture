import sys
sys.stdin = open('썸.txt')

T = 10
s = [[0 for i in range(100)] for j in range(100)]

for test_case in range(1, T + 1):
    p = int(input())
    maxn = 0
    for i in range(100):
        k = 0
        a = list(map(int, input().split()))
        for j in range(100):
            s[i][j] = a[k]
            k += 1


    for i in range(100):
        sumn = 0
        for j in range(100):
            sumn += s[i][j]
        if maxn < sumn:
            maxn = sumn

    for j in range(100):
        sumn = 0
        for i in range(100):
            sumn += s[i][j]
        if maxn < sumn:
            maxn = sumn

    for i in range(100):
        sumn = 0
        for j in range(100):
            if i == j:
                sumn += s[i][j]
        if maxn < sumn:
            maxn = sumn

    for i in range(100):
        sumn = 0
        for j in range(100):
            if i + j == 99:
                sumn += s[i][j]
        if maxn < sumn:
            maxn = sumn

    print('#{} {}'.format(test_case, maxn))






