import sys
sys.stdin = open('password.txt')


class Node(object):
    def __init__(self, data, n=None):
        self.data = data
        self.pre = n
        self.next = n


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    a = list(map(int, input().split()))
    head = Node(a[0])
    p = head
    for i in range(1, N):
        temp = p
        p.next = Node(a[i])
        p = p.next
        p.pre = temp
    tail = p
    p = head
    for i in range(K):
        for j in range(M - 1):
            p = p.next
            if p is None:
                p = head
        if p.next is None:
            num = p.data + head.data
        else:
            num = p.data + p.next.data
        temp_pre = p
        temp_next = p.next
        p.next = Node(num)
        p = p.next
        p.pre = temp_pre
        p.next = temp_next
        if temp_next is not None:
            temp_next.pre = p
        else:
            tail = p
    p = tail
    print('#{}'.format(tc), end='')
    for i in range(10):
        print(' {}'.format(p.data), end='')
        p = p.pre
        if p is None:
            break
    print()



