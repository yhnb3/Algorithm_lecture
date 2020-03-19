T = int(input())
dp = [0] * 14
for tc in range(1, T + 1):
    start, end = map(int, input().split())
    flag = False
    if start < 0:
        flag = True
        start = abs(start)
    r_end = end
    r_start = start
    c_end = end
    c_start = start
    e_cnt = 0
    s_cnt = 0
    while r_end != 0:
        r_end = r_end // 10
        e_cnt += 1
    while r_start != 0:
        r_start = r_start // 10
        s_cnt += 1
    e_sum = 0
    while e_cnt > 0:
        if end // 10 ** (e_cnt - 1) > 4:
            e_sum += 10 ** (e_cnt - 1)
        if e_cnt > 2:
            k = 0
            if dp[e_cnt] != 0:
                if end // (10 ** (e_cnt - 1)) > 4:
                    e_sum += dp[e_cnt] * ((end // 10 ** (e_cnt - 1)) - 1)
                else:
                    e_sum += dp[e_cnt] * (end // 10 ** (e_cnt - 1))
            else:
                for i in range(e_cnt - 1):
                    k += (10 ** (e_cnt - 2 - i)) * (9 ** i)
                dp[e_cnt] = k
                if end // (10 ** (e_cnt - 1)) > 4:
                    e_sum += k * ((end // 10 ** (e_cnt - 1)) - 1)
                else:
                    e_sum += k * (end // 10 ** (e_cnt - 1))
            end = end % (10 ** (e_cnt - 1))
            e_cnt -= 1
        elif e_cnt == 2:
            e_sum += end // 10 ** (e_cnt - 1)
            end = end % (10 ** (e_cnt - 1))
            e_cnt -= 1
        else:
            e_cnt -= 1
    c_end = c_end - 1 - e_sum
    s_sum = 0
    while s_cnt > 0:
        if start // 10 ** (s_cnt - 1) > 4:
            s_sum += 10 ** (s_cnt - 1)
        if s_cnt > 2:
            k = 0
            if dp[s_cnt] != 0:
                if start // (10 ** (s_cnt - 1)) > 4:
                    s_sum += dp[s_cnt] * ((start // 10 ** (s_cnt - 1)) - 1)
                else:
                    s_sum += dp[s_cnt] * (start // 10 ** (s_cnt - 1))
            else:
                for i in range(s_cnt - 1):
                    k += (10 ** (s_cnt - 2 - i)) * (9 ** i)
                dp[s_cnt] = k
                if start // (10 ** (s_cnt - 1)) > 4:
                    s_sum += k * ((start // 10 ** (s_cnt - 1)) - 1)
                else:
                    s_sum += k * (start // 10 ** (s_cnt - 1))
            start = start % (10 ** (s_cnt - 1))
            s_cnt -= 1
        elif e_cnt == 2:
            s_sum += end // 10 ** (s_cnt - 1)
            start = start % (10 ** (s_cnt - 1))
            s_cnt -= 1
        else:
            s_cnt -= 1
    c_start = c_start - 1 - s_sum
    if flag:
        print('#{} {}'.format(tc, c_start + c_end + 1))
    else:
        print('#{} {}'.format(tc, abs(c_start - c_end)))
