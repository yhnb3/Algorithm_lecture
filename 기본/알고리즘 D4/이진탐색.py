import sys
sys.stdin = open('이진탐색.txt')

T = int(input())

for test_case in range(1, T + 1):
    total, a, b = map(int, input().split())
    start = 1
    end = total
    acount = 0
    res = 0
    while res != a:
        res = int((start+end)/2)
        if res < a:
            start = res
        else:
            end = res
        acount += 1
    start = 1
    end = total
    bcount = 0
    res = 0
    while res != b:
        res = int((start+end)/2)
        if res < b:
            start = res
        else:
            end = res
        bcount += 1

    if acount > bcount:
        print('#{} B'.format(test_case))
    elif acount < bcount:
        print('#{} A'.format(test_case))
    else:
        print('#{} 0'.format(test_case))
