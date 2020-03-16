import sys
sys.stdin = open('love_counselor.txt')


def f(cnt, n):
    global min_num
    if N - n - (N // 2) + cnt < 0:
        return
    if cnt == N // 2:
        ans_x = 0
        ans_y = 0
        for i in range(N):
            if visit[i]:
                ans_x -= ji_rung[i][0]
                ans_y -= ji_rung[i][1]
            else:
                ans_x += ji_rung[i][0]
                ans_y += ji_rung[i][1]
        min_num = min(min_num, ans_x ** 2 + ans_y ** 2)
        return
    for i in range(n, N):
        if visit[i] == 0:
            f(cnt, n + 1)
            visit[i] = 1
            f(cnt + 1, n + 1)
            visit[i] = 0
            return


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ji_rung = [list(map(int, input().split())) for i in range(N)]
    min_num = float('inf')
    visit = [0] * N
    ans = 0
    f(0, 0)
    print('#{} {}'.format(test_case, min_num))



