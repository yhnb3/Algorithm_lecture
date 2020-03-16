T = int(input())
for test_case in range(1, T + 1):
    s = list(input())
    while 1:
        s = list(s)
        flag = False
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                flag = True
                break
        if not flag:
            break

    print('#{} {}'.format(test_case, len(s)))



