class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("List too short")
    curr = head
    first = curr
    second = curr.next
    tail1 = first
    tail2 = second
    curr = curr.next.next
    while curr:
        tail1.next = curr
        tail1 = tail1.next
        curr = curr.next
        if not curr:
            break
        tail2.next = curr
        tail2 = tail2.next
        curr = curr.next
    tail1.next = None
    tail2.next = None
    return Context(first, second)
