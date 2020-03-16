T = int(input())
for test_case in range(1, T + 1):
    A, B = input().split()
    a = len(A)
    b = len(B)
    cnt = 0
    num = 0
    skip = [b] * 128
    for i in range(b - 1):
        skip[ord(B[i])] = b - 1 - i
    while cnt < a:
        if cnt + b - 1 > a - 1:
            num += a - cnt
            break
        if A[cnt + b - 1] == B[-1]:
            if A[cnt: cnt + b] == B:
                num += 1
                cnt += b
            else:
                num += skip[ord(A[cnt + b - 1])]
                cnt += skip[ord(A[cnt + b - 1])]
        else:
            num += skip[ord(A[cnt + b - 1])]
            cnt += skip[ord(A[cnt + b - 1])]

    print('#{} {}'.format(test_case, num))







