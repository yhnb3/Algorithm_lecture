import sys
sys.stdin = open('olympic.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = [0] * N
    for j in range(M):
        max_idx = -1
        for i in range(N):
            if B[j] >= A[i]:
                max_idx = i
                break
        count[max_idx] += 1

    temp = max(count)
    for i in range(N):
        if temp == count[i]:
            print('#{} {}'.format(test_case, i + 1))
            break



