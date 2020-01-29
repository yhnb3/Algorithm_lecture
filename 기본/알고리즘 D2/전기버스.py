import sys
sys.stdin = open("전기버스.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K, N, M = map(int, input().split(" "))
    charge = list(map(int, input().split(" ")))

    i = 0
    count = 0
    while i + K < N:
        count1 = count
        for j in range(K, 0, -1):
            if i + j in charge:
                i += j
                count += 1
                break

        if count1 == count:
            print('#{} 0'.format(test_case))
            break
    else:
        print('#{} {}'.format(test_case, count))