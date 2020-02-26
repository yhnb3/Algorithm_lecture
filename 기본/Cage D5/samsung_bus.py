import sys
sys.stdin = open('samsung_bus.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    s = [list(map(int, input().split())) for i in range(N)]

    P = int(input())

    print('#{}'.format(test_case), end='')
    for j in range(P):
        count = 0
        a = int(input())
        for i in range(N):
            if s[i][0] <= a <= s[i][1]:
                count += 1
        print(' {}'.format(count), end='')
    print()