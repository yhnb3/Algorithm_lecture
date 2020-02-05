import sys
sys.stdin = open('카카.txt')

T = int(input())

for test_case in range(1, T + 1):
    sam = input()
    s = [[0]*3 for i in range(len(sam)//3)]
    k = 0
    for i in range(len(sam)//3):
        for j in range(3):
            s[i][j] = sam[k]
            k += 1

    result = [13, 13, 13, 13]
    count = True
    for i in range(0, len(sam)//3):
        for j in range(i + 1, len(sam)//3):
            if s[i] == s[j]:
                print('#{} ERROR'.format(test_case))
                count = False
                break
    if count:
        for j in range(len(sam)//3):
            if s[j][0] == 'S':
                result[0] -= 1
            elif s[j][0] == 'D':
                result[1] -= 1
            elif s[j][0] == 'H':
                result[2] -= 1
            elif s[j][0] == 'C':
                result[3] -= 1
        print('#{} {} {} {} {}'.format(test_case, result[0], result[1], result[2], result[3]))



