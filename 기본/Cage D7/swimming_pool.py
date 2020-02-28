import sys
sys.stdin = open('swimming_pool.txt')


def comb(n, sum_num):
    if sum_num > min_num[0]:
        return
    if n > 12:
        min_num[0] = sum_num
        return
    for i in range(2):
        if i == 0:
            if month[n]:
                if month[n] * price[0] < price[1]:
                    comb(n + mon_sep[i], sum_num + month[n] * price[0])
                else:
                    comb(n + mon_sep[i], sum_num + price[1])
            else:
                comb(n + mon_sep[i], sum_num)
        if i == 1 and n != 12:
            c = 0
            if month[n]:
                c += price[1]
            if month[n + 1]:
                c += price[1]
            if month[n + 2]:
                c += price[1]
            if c < (month[n] + month[n + 1] + month[n + 2]) * price[0]:
                pass
            else:
                c = (month[n] + month[n + 1] + month[n + 2]) * price[0]
            if price[2] < c:
                c = price[2]
            comb(n + mon_sep[i], sum_num + c)


T = int(input())
for test_case in range(1, T + 1):
    price = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    month.append(0)
    month.append(0)
    month.append(0)
    month.append(0)
    mon_sep = [1, 3]
    min_num = [0]
    min_num[0] = price[3]

    comb(1, 0)

    print('#{} {}'.format(test_case, min_num[0]))






