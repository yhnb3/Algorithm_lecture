class Node(object):
    def __init__(self, data, n=None):
        self.pre = n
        self.data = data
        self.next = n


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    head, tail = None, None
    for i in range(M):
        a = list(map(int, input().split()))
        if head is None:
            head = Node(a[0])
            p = head
            for j in range(1, N):
                p.next = Node(a[j])
                temp = p
                p = p.next
                p.pre = temp
        else:
            p = head
            if head.data <= a[0]:
                while p.next is not None:
                    p = p.next
                    if p.data > a[0]:
                        p = p.pre
                        break
                tempp = p.next
                for j in range(0, N):
                    p.next = Node(a[j])
                    temp = p
                    p = p.next
                    p.pre = temp
                p.next = tempp
            else:
                tempp = head
                head = Node(a[0])
                p = head
                for j in range(1, N):
                    p.next = Node(a[j])
                    temp = p
                    p = p.next
                    p.pre = temp
                p.next = tempp
            if tempp is not None:
                temp = p
                p = p.next
                p.pre = temp
    p = head
    while p.next is not None:
        p = p.next
    print('#{}'.format(tc), end='')
    for i in range(10):
        print(' {}'.format(p.data), end='')
        p = p.pre
    print()