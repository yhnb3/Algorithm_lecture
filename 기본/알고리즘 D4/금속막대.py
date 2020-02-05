import sys
sys.stdin = open('금속막대.txt')

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    count = num
    ss = [[0]*2 for a in range(num)]
    result = []
    a = list(map(int, input().split()))
    k = 0

    for i in range(num):
        for j in range(2):
            ss[i][j] = a[k]
            k += 1

    result.insert(0, ss[0])

    while count > 1:
        for i in range(1, len(ss)):
            if result[0][0] == ss[i][1]:
                result.insert(0, ss[i])
                count -= 1
                continue

            if result[-1][1] == ss[i][0]:
                result.insert(num+1, ss[i])
                count -= 1
                continue



    print('#{}'.format(test_case), end ='')
    for i in range(len(result)):
        for j in range(2):
            print(' {}'.format(result[i][j]), end='')
    print("")



