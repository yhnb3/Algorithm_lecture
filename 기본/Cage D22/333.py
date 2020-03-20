T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    start = 1
    end = 10 ** 6
    while start != end:
        if abs(start - end) == 1:
            if start ** 3 == N:
                print('#{} {}'.format(tc, start))
                break
            elif end ** 3 == N:
                print('#{} {}'.format(tc, end))
                break
            else:
                start = end
        temp = (start + end) // 2
        if temp ** 3 == N:
            print('#{} {}'.format(tc, temp))
            break
        elif temp ** 3 < N:
            start = temp
        elif temp ** 3 > N:
            end = temp
    else:
        print('#{} {}'.format(tc, -1))



