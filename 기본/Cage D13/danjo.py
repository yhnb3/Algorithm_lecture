import sys
sys.stdin = open('danjo.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = list(map(int, input().split()))
    max_num = -1
    for i in range(N):
        for j in range(i + 1, N):
            num = S[i] * S[j]
            a = num
            while a > 9:
                if a % 10 >= a % 100 // 10:
                    a = a // 10
                    pass
                else:
                    break
            else:
                max_num = max(max_num, num)

    print('#{} {}'.format(test_case, max_num))