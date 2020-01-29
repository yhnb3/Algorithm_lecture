import sys
sys.stdin = open("숫자카드.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K = int(input())
    S = input()
    k = [0]*10
    max_num = 0
    for i in S:
        for j in range(0, 10):
            if i == str(j):
                k[j] += 1

    for i in k:
        if i > max_num:
            max_num = i

    for i in range(9, -1, -1):
        if max_num == k[i]:
            print('#{} {} {}'.format(test_case, i, max_num))
            break