# import sys
# sys.stdin = open('종이붙이기.txt')

T = int(input())


for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    for i in range(1, N//20 + 1):
        combi_num = 1
        for j in range(1, i + 1):
            combi_num *= (N//10 - i * 2) + i - j + 1
            combi_num //= j
        result += combi_num * (2 ** i)
    result += 1

    print('#{} {}'.format(test_case, result))






