import sys

sys.stdin = open('구간합.txt', 'r')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    a, b = map(int, input().split())
    c = input().split()
    d = list()
    max_num = 0
    min_num = 7891548779

    for i in range(0, a - b + 1):
        e = 0
        for j in range(b):
            e += int(c[j + i])
        if e > max_num:
            max_num = e

    for i in range(0, a - b + 1):
        e = 0
        for j in range(b):
            e += int(c[j + i])
        if e < min_num:
            min_num = e

    print('#{} {}'.format(test_case, max_num - min_num))
