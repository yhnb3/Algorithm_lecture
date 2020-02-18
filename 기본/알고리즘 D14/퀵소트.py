s = list(map(int, input().split()))


def quick_sort(l, r):
    if l < r:
        a = partition(l, r)
        quick_sort(a + 1, r)
        quick_sort(l, a - 1)


def partition(l, r):
    a = s[l]
    i = l
    j = r
    while i <= j:
        while s[i] <= a:
            i += 1
            if i == r:
                break
        while s[j] >= a:
            j -= 1
            if j == l:
                break
        if i < j:
            s[i], s[j] = s[j], s[i]

    s[l], s[j] = s[j], s[l]
    return j


quick_sort(0, len(s) - 1)

print(s)

