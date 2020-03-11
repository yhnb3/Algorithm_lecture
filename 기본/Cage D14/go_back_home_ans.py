import sys
sys.stdin = open('go_back_room.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for i in range(N)]
    count = [0] * 201
    for i in range(N):
        a = (S[i][1] + 1) // 2
        b = (S[i][0] + 1) // 2
        if a > b:
            a, b = b, a
        for j in range(a, b + 1):
            count[j] += 1

    print('#{} {}'.format(test_case, max(count)))