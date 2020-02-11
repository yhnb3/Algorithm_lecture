import sys
sys.stdin = open('글자수.txt')

T = int(input())

for test_case in range(1, T + 1):
    s1 = list(input())
    s2 = list(input())

    max_num = 0
    for i in range(len(s1)):
        count = 0
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count += 1
        if max_num < count:
            max_num = count

    print('#{} {}'.format(test_case, max_num))
