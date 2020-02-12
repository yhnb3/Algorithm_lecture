import sys
sys.stdin = open('삼성시의버스노선.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    s = [list(map(int, input().split())) for i in range(N)]
    P = int(input())
    count = [0] * P
    C = []

    for i in range(P):
        a = int(input())
        C.append(a)

    for i in range(P):
        for j in range(N):
            if s[j][0] <= C[i] <= s[j][1]:
                count[i] += 1

    print('#{}'.format(test_case), end='')
    for i in range(P):
        print(' {}'.format(count[i]), end='')
    print()