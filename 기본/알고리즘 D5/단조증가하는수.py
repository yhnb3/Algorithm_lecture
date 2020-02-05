import sys

sys.stdin = open('단조증가하는수.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    s = list(map(int, input().split()))

    max_num = -1
    num = 0
    for i in range(N - 1):
        for j in range(i + 1, N - 1):
            count = 0
            num = s[i] * s[j]
            while num > 9:
                if (num % 100) // 10 > num % 10:
                    count += 1
                    break
                else:
                    num = num // 10
            if count == 0:
                if max_num < s[i] * s[j]:
                    max_num = s[i] * s[j]

    if max_num > 0:
        print('#{} {}'.format(test_case, max_num))
    else:
        print('#{} {}'.format(test_case, -1))
