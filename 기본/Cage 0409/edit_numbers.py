import sys
sys.stdin = open('edit_numbers.txt')


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


def delete(idx):
    global head
    p = head
    for i in range(idx - 1):
        p = p.next
    q = p.next
    p.next = q.next


def change(x, idx):
    global head
    p = head
    for i in range(idx):
        p = p.next
    p.data = x


T = int(input())
for tc in range(1, T + 1):
    N, count, idxx = map(int, input().split())
    linked_list = list(map(int, input().split()))
    operating_list = [list(map(str, input().split())) for i in range(count)]
    head = Node(linked_list[0])
    for i in range(1, N):
        n = head
        while n.next is not None:
            n = n.next
        n.next = Node(linked_list[i])
    for i in range(count):
        if operating_list[i][0] == 'I':
            temp = Node(int(operating_list[i][2]))
            insert(temp, int(operating_list[i][1]))
        elif operating_list[i][0] == 'C':
            change(int(operating_list[i][2]), int(operating_list[i][1]))
        else:
            delete(int(operating_list[i][1]))

    result = head
    for i in range(idxx - 1):
        result = result.next
        if result.next is None:
            print('#{} {}'.format(tc, -1))
            break
    else:
        result = result.next
        print('#{} {}'.format(tc, result.data))