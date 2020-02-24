N = int(input())

S = list(input())

gwal = list(range(0, N - 1, 2))
gwal_check = [0] * (N + 1)
st = []
result = [- (2 ** 31)]


def calc(i):
    while i < N:
        if gwal_check[i] == 1:
            if S[i + 1] == '+':
                st.append(S[i] + S[i + 2])
            elif S[i + 1] == '-':
                st.append(S[i] - S[i + 2])
            elif S[i + 1] == '*':
                st.append(S[i] * S[i + 2])
            i += 3
        else:
            st.append(S[i])
            i += 1


def max_num(a):
    a = st[0]
    for i in range(1, len(st), 2):
        if st[i] == '+':
            a = a + st[i + 1]
        elif st[i] == '-':
            a = a - st[i + 1]
        elif st[i] == '*':
            a = a * st[i + 1]

    if result[0] < a:
        result[0] = a


def add_gwal(a, c):
    if a >= N - 1:
        st.clear()
        calc(0)
        max_num(0)
        return
    if c:
        gwal_check[a] = 1
        if a + 4 >= N - 1:
            add_gwal(a + 4, 1)
        else:
            add_gwal(a + 4, 1)
            add_gwal(a + 4, 0)
    else:
        gwal_check[a] = 0
        if a + 2 >= N - 1:
            add_gwal(a + 2, 1)
        else:
            add_gwal(a + 2, 1)
            add_gwal(a + 2, 0)


for i in range(N):
    if not i & 1:
        S[i] = int(S[i])

add_gwal(0, 1)
add_gwal(0, 0)

print(result[0])




