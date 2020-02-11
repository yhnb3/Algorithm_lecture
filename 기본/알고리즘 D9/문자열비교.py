import sys
sys.stdin = open('문자열비교.txt')

T = int(input())

for test_case in range(1, T + 1):
    s1 = list(input())
    s2 = list(input())

    count = 0
    for i in range(len(s2) - len(s1) + 1):
        for j in range(len(s1)):
            if s2[i + j] == s1[j]:
                pass
            else:
                break
        else:
            count += 1

    print('#{} {}'.format(test_case, count))