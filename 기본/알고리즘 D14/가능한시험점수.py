import sys
sys.stdin = open('가능한시험점수.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = [0]
    score = list(map(int, input().split()))
    count = [0] * 100001
    check = 0
    sum_num = 0
    for i in range(N):
        j = 0
        a = len(result)
        while j < a:
            if count[result[j] + score[i]] == 0:
                count[result[j] + score[i]] += 1
                result.append(result[j] + score[i])
                check += 1
            j += 1
    print('#{} {}'.format(test_case, check + 1))

