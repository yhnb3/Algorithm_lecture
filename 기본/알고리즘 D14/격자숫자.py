import sys
sys.stdin = open('격자숫자.txt')

T = int(input())


def number_paste(x, y, k, c, result):
    result += s[x][y] * k

    if c == 6:
        if result not in result_list:
            result_list.append(result)
            result -= s[x][y] * k
            return
        else:
            result -= s[x][y] * k
            return

    for i in range(4):
        if 0 <= s[x + dx[i]][y + dy[i]] <= 9:
            number_paste(x + dx[i], y + dy[i], k * 10, c + 1, result)



for test_case in range(1, T + 1):
    s = [[-1] * 6 for i in range(6)]
    for i in range(1, 5):
        a = list(map(int, input().split()))
        for j in range(1, 5):
            s[i][j] = a[j - 1]
    result_list = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(1, 5):
        for j in range(1, 5):
            number_paste(i, j, 1, 0, 0)

    print('#{} {}'.format(test_case, len(result_list)))

