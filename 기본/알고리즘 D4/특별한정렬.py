import sys
sys.stdin = open('특별한정렬.txt')

T = int(input())

for test_case in range(1, T + 1):
    Alen = int(input())
    A = list(map(int, input().split()))
    for i in range(Alen-1):
        if i & 1:
            min_num = 101
            min_idx = i
            for j in range(i, Alen):
                if A[j] < min_num:
                    min_num = A[j]
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]
        else:
            max_num = 0
            max_idx = i
            for j in range(i, Alen):
                if A[j] > max_num:
                    max_num = A[j]
                    max_idx = j
            A[i], A[max_idx] = A[max_idx], A[i]

    print('#{}'.format(test_case), end='')
    for i in range(10):
        print(' {}'.format(A[i]), end='')
    print("")



