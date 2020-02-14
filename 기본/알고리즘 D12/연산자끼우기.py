T = int(input())

s = list(map(int, input().split()))

cal_cul = list(map(int, input().split()))
result = []
max_len = [-1000000001]
min_len = [1000000001]

def calculator(ans, b):
    if b == T - 1:
        if max_len[0] < ans:
            max_len[0] = ans

        if min_len[0] > ans:
            min_len[0] = ans
        return

    for i in range(4):
        if cal_cul[i] > 0:
            cal_cul[i] -= 1
            c = ans
            if i == 0:
                ans = ans + s[b + 1]
            elif i == 1:
                ans = ans - s[b + 1]
            elif i == 3:
                if ans < 0:
                    ans = -(-ans // s[b + 1])
                else:
                    ans = ans // s[b + 1]
            elif i == 2:
                ans = ans * s[b + 1]
            calculator(ans, b + 1)
            cal_cul[i] += 1
            ans = c

calculator(s[0], 0)

print(max_len[0])
print(min_len[0])










