import sys
sys.stdin = open('samsung_bus.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [list(map(int, input())) for _ in range(P)]
    cnt = [0] * 5002
    print(C)

    for i in range(N):
        for j in range(A[i][0], A[i][1] + 1):
            cnt[j] += 1

    print('#{}'.format(tc), end='')
    for a in range(P):
        print(' {}'.format(cnt[C[a][0]]), end='')
    print()
