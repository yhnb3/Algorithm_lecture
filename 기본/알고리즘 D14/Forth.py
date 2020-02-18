import sys
sys.stdin = open('Forth.txt')

T = int(input())

for test_case in range(1, T + 1):
    pp = list(input().split())
    stackk = []
    yeon_san = ['*', '/', '-', '+', '.']
    flag = True

    print('#{} '.format(test_case), end='')
    for i in pp:
        if i not in yeon_san:
            stackk.append(i)

        else:
            if i == '+':
                if len(stackk) >= 2:
                    a = int(stackk.pop())
                    b = int(stackk.pop())
                    stackk.append(b + a)
                else:
                    print('error')
                    break
            elif i == '-':
                if len(stackk) >= 2:
                    a = int(stackk.pop())
                    b = int(stackk.pop())
                    stackk.append(b - a)
                else:
                    print('error')
                    break
            elif i == '*':
                if len(stackk) >= 2:
                    a = int(stackk.pop())
                    b = int(stackk.pop())
                    stackk.append(b * a)
                else:
                    print('error')
                    break
            elif i == '/':
                if len(stackk) >= 2:
                    a = int(stackk.pop())
                    b = int(stackk.pop())
                    stackk.append(int(b / a))
                else:
                    print('error')
                    break
            elif i == '.':
                if len(stackk) == 1:
                    print(stackk.pop())
                else:
                    print('error')
