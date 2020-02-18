# import sys
# sys.stdin = open('최대상금.txt')



def max_money(a, n):
    global max_num
    if a == n:
        s3 = ''.join(s1)
        if max_num < int(s3):
            max_num = int(s3)

        return

    for k in range(len(s1)):
        for h in range(k + 1, len(s1)):
            s1[k], s1[h] = s1[h], s1[k]
            max_money(a + 1, n)
            s1[k], s1[h] = s1[h], s1[k]


for test_case in range(1, int(input()) + 1):
    s, N = map(int, input().split())
    s1 = [x for x in str(s)]
    max_num = 0

    max_money(0, N)

    print('#{} {}'.format(test_case, max_num))




