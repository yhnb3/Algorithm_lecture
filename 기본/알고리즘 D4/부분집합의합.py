import sys
sys.stdin = open('부분집합의합.txt')

T = int(input())

for test_case in range(1, T + 1):
    num, sum_num = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ccount = 0
    for i in range(1 << 12):
        count = 0
        summ = 0
        for j in range(12):
            if (1 << j) & i:
                count += 1
                summ += A[j]
        if count == num:
            if summ == sum_num:
                ccount += 1
    print('#{} {}'.format(test_case, ccount))






