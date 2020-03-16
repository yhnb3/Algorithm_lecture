T = int(input())
for test_case in range(1, T + 1):
    s = input()
    l = len(s)
    for i in range(l // 2):
        if s[i] == s[l - i - 1] or s[i] == '?' or s[l - i - 1] == '?':
            pass
        else:
            print('#{} Not exist'.format(test_case))
            break
    else:
        print('#{} Exist'.format(test_case))

