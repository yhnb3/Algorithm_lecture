import sys
sys.stdin = open('make_number.txt')


def party(n, ans):
    if n == N - 1:
        if ans < result[0]:
            result[0] = ans
        if ans > result[1]:
            result[1] = ans
        return
    for i in range(4):
        if yeon_san[i] > 0:
            c = ans
            if i == 0:
                ans = ans + numbers[n + 1]
            elif i == 1:
                ans = ans - numbers[n + 1]
            elif i == 2:
                ans = ans * numbers[n + 1]
            elif i == 3:
                ans = int(ans / numbers[n + 1])
            yeon_san[i] -= 1
            party(n + 1, ans)
            yeon_san[i] += 1
            ans = c


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    yeon_san = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = [100000001, -100000001]
    party(0, numbers[0])
    print('#{} {}'.format(test_case, abs(result[0] - result[1])))