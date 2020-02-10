import sys
sys.stdin = open('GNS.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, n = map(str, input().split())
    s = list(map(str, input().split()))
    count = [0]*10

    for i in s:
        if i == 'ZRO':
            count[0] += 1
        elif i == 'ONE':
            count[1] += 1
        elif i == 'TWO':
            count[2] += 1
        elif i == 'THR':
            count[3] += 1
        elif i == 'FOR':
            count[4] += 1
        elif i == 'FIV':
            count[5] += 1
        elif i == 'SIX':
            count[6] += 1
        elif i == 'SVN':
            count[7] += 1
        elif i == 'EGT':
            count[8] += 1
        elif i == 'NIN':
            count[9] += 1

    print(N)
    for i in range(10):
        for j in range(count[i]):
            if i == 0:
                print('ZRO ', end='')
            elif i == 1:
                print('ONE ', end='')
            elif i == 2:
                print('TWO ', end='')
            elif i == 3:
                print('THR ', end='')
            elif i == 4:
                print('FOR ', end='')
            elif i == 5:
                print('FIV ', end='')
            elif i == 6:
                print('SIX ', end='')
            elif i == 7:
                print('SVN ', end='')
            elif i == 8:
                print('EGT ', end='')
            elif i == 9:
                print('NIN ', end='')
    print()