import sys
sys.stdin = open('두개의숫자열.txt')

T = int(input())

for test_case in range(1, T + 1):
    a_len, b_len = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_flag = False
    max_num = 0

    if a_len > b_len:
        max_len = a_len
        a_flag = True
    else:
        max_len = b_len

    if a_flag:
        for i in range(a_len - b_len + 1):
            test_num = 0
            for j in range(b_len):
                test_num += a[j+i] * b[j]

            if max_num < test_num:
                max_num = test_num
    else:
        for i in range(b_len - a_len + 1):
            test_num = 0
            for j in range(a_len):
                test_num += b[j+i] * a[j]

            if max_num < test_num:
                max_num = test_num

    print('#{} {}'.format(test_case, max_num))




