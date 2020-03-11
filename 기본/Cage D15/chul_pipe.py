T = int(input())
for test_case in range(1, T + 1):
    s = input()
    stackk = []
    result = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            if s[i + 1] == ')':
                result += len(stackk)
                i += 2
            else:
                stackk.append('(')
                i += 1
        else:
            result += 1
            stackk.pop()
            i += 1

    print('#{} {}'.format(test_case, result))
