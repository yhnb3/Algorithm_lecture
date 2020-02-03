import sys
sys.stdin = open('이상한나라의엘리스.txt')

T = int(input())

for test_case in range(1, T + 1):
    s = int(input())
    count = 0
    while s > 9:
        if s//10%10 + s%10 > 9:
            s = s//100*100 + s//10%10 + s%10
        else:
            s = s//100*10 + s//10%10 + s%10
        count += 1
    if count & 1:
        print('#{} A'.format(test_case))
    else:
        print('#{} B'.format(test_case))
