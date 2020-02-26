import sys
sys.stdin = open('padovan.txt')

T = int(input())
S = [0] * 101
S[0] = 1
S[1] = 1
S[2] = 1
S[3] = 1
S[4] = 2
S[5] = 2


for _ in range(T):
    N = int(input())
    if N < 6:
        print(S[N])
    else:
        for i in range(6, N + 1):
            S[i] = S[i - 5] + S[i - 1]
        print(S[N])

