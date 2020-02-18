import sys
sys.stdin = open('계산기3.txt')
yeon_san = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    S = input()
    sam_stackk = []
    jung_hu = []
    cal_cul = []

    for i in range(len(S)):
        if S[i] not in yeon_san.keys():
            if S[i] == ')':
                while sam_stackk[-1] != '(':
                    b = sam_stackk.pop()
                    jung_hu.append(b)
                sam_stackk.pop()
            else:
                jung_hu.append(int(S[i]))
        else:
            if not sam_stackk:
                sam_stackk.append(S[i])
            else:
                if S[i] == '(':
                    sam_stackk.append(S[i])

                elif yeon_san[sam_stackk[-1]] < yeon_san[S[i]]:
                    sam_stackk.append(S[i])
                else:
                    while sam_stackk:
                        if yeon_san[S[i]] <= yeon_san[sam_stackk[-1]]:
                            a = sam_stackk.pop()
                            jung_hu.append(a)
                            continue
                        else:
                            sam_stackk.append(S[i])
                            break
                    else:
                        sam_stackk.append(S[i])

    while sam_stackk:
        a = sam_stackk.pop()
        jung_hu.append(a)


    for i in range(len(jung_hu)):
        if jung_hu[i] not in yeon_san.keys():
            cal_cul.append(jung_hu[i])
        else:
            a = cal_cul.pop()
            b = cal_cul.pop()
            if jung_hu[i] == '+':
                cal_cul.append(b+a)
            elif jung_hu[i] == '-':
                cal_cul.append(b-a)
            elif jung_hu[i] == '*':
                cal_cul.append(b*a)
            elif jung_hu[i] == '/':
                cal_cul.append(b/a)

    print('#{} {}'.format(test_case, cal_cul[0]))






