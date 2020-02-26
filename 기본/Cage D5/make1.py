import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
s = [1000001] * (10 ** 6 + 1)
s[1] = 0
s[2] = 1
s[3] = 1


# def make1(n):
#     if n == 0:
#         return 1000001
#     if s[n] != 1000001:
#         return s[n]
#     if n % 3 == 0:
#         s[n] = make1(n // 3) + 1
#     elif n % 2 == 0:
#         s[n] = min(make1(n // 2) + 1, s[n])
#     s[n] = min(make1(n - 1) + 1, s[n])
#     return s[n]

# print(make1(N))

if N > 3:
    for i in range(4, N + 1):
        numbers = [s[i - 1]]
        if i % 2 == 0:
            numbers.append(s[i // 2])
        if i % 3 == 0:
            numbers.append(s[i // 3])
        s[i] = min(numbers) + 1
    print(s[N])
else:
    print(s[N])
