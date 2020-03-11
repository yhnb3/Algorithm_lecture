T = int(input())
for test_case in range(1, T + 1):
    s = input()
    c = [0] * 5
    cc = [0] * 5
    min_num = 0
    for i in s:
        if i == 'c':
            min_num = max(min_num, c[0] - c[4] + 1)
            c[0] += 1
            cc[0] += 1
        elif i == 'r':
            if c[0] > c[1]:
                c[1] += 1
            cc[1] += 1
        elif i == 'o':
            if c[1] > c[2]:
                c[2] += 1
            cc[2] += 1
        elif i == 'a':
            if c[2] > c[3]:
                c[3] += 1
            cc[3] += 1
        elif i == 'k':
            if c[3] > c[4]:
                c[4] += 1
            cc[4] += 1
    if min(c) != max(c) or max(cc) != min(cc):
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, min_num))