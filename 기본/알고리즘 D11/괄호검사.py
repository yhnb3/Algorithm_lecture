import sys
sys.stdin = open('괄호검사.txt')

T = int(input())

for test_case in range(1, T + 1):
    stackk = []
    S = input()
    flag = False
    gwal_ho = ['(', '{']

    for i in range(len(S)):
        if S[i] in gwal_ho:
            stackk.append(S[i])

        else:
            if S[i] == '}':
                if stackk:
                    if '{' == stackk[-1]:
                        stackk.pop()
                    else:
                        flag = True
                        break
            elif S[i] == ')':
                if stackk:
                    if '(' == stackk[-1]:
                        stackk.pop()
                    else:
                        flag = True
                        break

    if stackk:
        print('#{} 0'.format(test_case))
    else:
        if flag:
            print('#{} 0'.format(test_case))
        else:
            print('#{} 1'.format(test_case))

