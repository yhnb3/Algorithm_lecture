import sys, collections, copy
sys.stdin = open('go_min.txt')

T = int(input())
for test_case in range(1, T + 1):
    W, H, N = map(int, input().split())
    S = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for i in range(N - 1):
        if S[i][0] < S[i + 1][0] and S[i][1] > S[i + 1][1]:
            result += abs(S[i + 1][0] - S[i][0] + S[i][1] - S[i + 1][1])
        elif S[i][0] > S[i + 1][0] and S[i][1] < S[i + 1][1]:
            result += abs(S[i + 1][0] - S[i][0] + S[i][1] - S[i + 1][1])
        elif S[i][0] == S[i + 1][0] or S[i][1] == S[i + 1][1]:
            result += abs(S[i + 1][0] - S[i][0] + S[i][1] - S[i + 1][1])
        else:
            result += max(abs(S[i][0] - S[i + 1][0]), abs(S[i][1] - S[i + 1][1]))

    print('#{} {}'.format(test_case, result))



