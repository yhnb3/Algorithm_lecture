import sys
sys.stdin = open('반복문자지우기.txt')

T = int(input())

for test_case in range(1, T + 1):
    S = input()
    str_test =[1] * (len(S) + 1)
    stackk = []
    idx_list = []

    S = S + '0'
    count = 1
    idx = 0
    while idx < len(S):
        if str_test[idx] == 1:
            if not stackk:
                stackk.append(S[idx])
                idx_list.append(idx)
                idx += 1
                continue

            if S[idx] == stackk[0]:
                if count == 2:
                    for j in range(count):
                        str_test[idx_list[j]] = 0
                    idx = 0
                    stackk.pop()
                    count = 1
                    idx_list = []
                    continue
                count += 1
            else:
                stackk.pop()
                stackk.append(S[idx])
                if count == 2:
                    for j in range(count):
                        str_test[idx_list[j]] = 0
                    idx = 0
                    stackk.pop()
                    count = 1
                    idx_list = []
                    continue
                else:
                    idx_list = []
            idx_list.append(idx)
            idx += 1
        else:
            idx += 1
    print('#{} {}'.format(test_case, sum(str_test) - 1))
