T = int(input())
for test_case in range(1, T + 1):
    s = input()
    stack = []
    gwal_l = ['(', '{']
    gwal_r = [')', '}']
    ans = 0
    flag = True
    for i in s:
        if i in gwal_l:
            stack.append(i)
        elif i in gwal_r:
            if stack:
                if i == '}':
                    if stack[-1] == '{':
                        stack.pop()
                elif i == ')':
                    if stack[-1] == '(':
                        stack.pop()
            else:
                flag = False
                break
    if not flag or stack:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, 1))


