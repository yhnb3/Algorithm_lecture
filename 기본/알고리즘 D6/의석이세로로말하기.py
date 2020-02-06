import sys
sys.stdin = open('의석이세로로말하기.txt')

T = int(input())

for test_case in range(1, T + 1):
    s = [[0]*15 for i in range(5)]
    for i in range(5):
        a = input()
        for j in range(len(a)):
            s[i][j] = a[j]

    print('#{} '.format(test_case), end = "")
    for i in range(15):
        for j in range(5):
            if s[j][i] == 0:
                pass
            else:
                print(s[j][i], end='')
    print("")