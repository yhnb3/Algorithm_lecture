import sys
sys.stdin = open('통역사성경이.txt')

T = int(input())


for test_case in range(1, T + 1):
    test_s ='.?!'
    ss = []
    p = int(input())
    s = list(input().split())
    a = 0
    count = 0
    for i in s:
        if i.isalpha():
            if i[0] == i[0].upper() and i[1:] == i[1:].lower():
                count += 1
        else:
            if i[-1] in test_s:
                if i[:-1].isalpha():
                    if i[0] == i[0].upper() and i[1:] == i[1:].lower():
                        count += 1
        for j in i:
            if j in test_s:
                ss.append(count)
                count = 0
                break

    print('#{}'.format(test_case), end="")
    for i in range(p):
        print(' {}'.format(ss[i]),end="")
    print("")






