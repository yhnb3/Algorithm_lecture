import sys
sys.stdin = open('add_num.txt')


class Node(object):
    def __init__(self, data, n=None):
        self.data = data
        self.next = n


def insert(x, idx):
    global head
    p = head
    for i in range(idx - 1):
        p = p.next
    x.next = p.next
    p.next = x


T = int(input())
for tc in range(1, T + 1):
    N, count, idxx = map(int, input().split())
    linked_list = list(map(int, input().split()))
    insert_list = [list(map(int, input().split())) for i in range(count)]
    head = Node(linked_list[0])
    for i in range(1, N):
        n = head
        while n.next is not None:
            n = n.next
        n.next = Node(linked_list[i])
    for i in range(count):
        temp = Node(insert_list[i][1])
        insert(temp, insert_list[i][0])
    result = head
    for i in range(idxx):
        result = result.next
    print('#{} {}'.format(tc, result.data))
