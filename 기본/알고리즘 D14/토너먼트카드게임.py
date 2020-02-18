import sys
sys.stdin = open('토너먼트카드게임.txt')


def tor_card(start, end):
    if end - start < 2:
        if end - start == 0:
            return start

        else:
            if s[start] == 1:
                if s[end] == 2:
                    return end
                elif s[end] == 3:
                    return start
                elif s[end] == 1:
                    return start

            elif s[start] == 2:
                if s[end] == 2:
                    return start
                elif s[end] == 3:
                    return end
                elif s[end] == 1:
                    return start

            elif s[start] == 3:
                if s[end] == 1:
                    return end
                elif s[end] == 3:
                    return start
                elif s[end] == 2:
                    return start
    else:
        b = tor_card(start, (end + start) // 2)
        c = tor_card((end + start) // 2 + 1, end)
        if s[b] == 1:
            if s[c] == 2:
                return c
            elif s[c] == 3:
                return b
            elif s[c] == 1:
                return b
        elif s[b] == 2:
            if s[c] == 2:
                return b
            elif s[c] == 3:
                return c
            elif s[c] == 1:
                return b
        elif s[b] == 3:
            if s[c] == 1:
                return c
            elif s[c] == 3:
                return b
            elif s[c] == 2:
                return b


for test_case in range(1, int(input()) + 1):
    N = int(input())
    s = list(map(int, input().split()))

    print('#{} {}'.format(test_case, tor_card(0, N - 1) + 1))




