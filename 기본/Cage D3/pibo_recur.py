T = int(input())

def pibo_0(n):
    if S[n] != -1:
        return S[n]

    else:
        S[n] = pibo_0(n - 1) + pibo_0(n - 2)
        return S[n]


def pibo_1(n):
    if M[n] != -1:
        return M[n]

    else:
        M[n] = pibo_1(n - 1) + pibo_1(n - 2)
        return M[n]


for test_case in range(1, T + 1):
    N = int(input())

    if N == 0:
        print('1 0')
    else:
        S = [-1] * (N + 1)
        S[0] = 0
        S[1] = 1

        M = [-1] * (N + 1)
        M[0] = 1
        M[1] = 1
        print('{} {}'.format(pibo_0(N - 1), pibo_1(N - 1)))
