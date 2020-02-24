import sys

sys.stdin = open('merge_sort.txt')

T = int(input())


def sorting(start, end):
    if start == end:
        return
    else:
        sorting(start, start + (end - start + 1) // 2 - 1)
        sorting(start + (end - start + 1) // 2, end)
        s1 = start
        s2 = start + (end - start + 1) // 2
        if s[start + (end - start + 1) // 2 - 1 - 1] > s[end - 1]:
            result[0] += 1

        for i in range(start, end + 1):
            if s2 >= end + 1:
                r1[i - 1] = s[s1 - 1]
                s1 += 1
            elif s1 >= start + (end - start + 1) // 2:
                r1[i - 1] = s[s2 - 1]
                s2 += 1
            elif s[s1 - 1] <= s[s2 - 1]:
                r1[i - 1] = s[s1 - 1]
                s1 += 1
            else:
                r1[i - 1] = s[s2 - 1]
                s2 += 1
        s[start - 1:end] = r1[start - 1:end]


for test_case in range(1, T + 1):
    N = int(input())
    s = list(map(int, input().split()))
    result = [0]
    r1 = [0] * N
    sorting(1, N)
    print('#{} {} {}'.format(test_case, s[N // 2], result[0]))
