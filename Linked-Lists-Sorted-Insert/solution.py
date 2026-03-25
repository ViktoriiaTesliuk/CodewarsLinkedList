""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    new_node = Node(data)
    if head is None or data <= head.data:
        new_node.next = head
        return new_node
    curr = head
    while curr.next is not None and curr.next.data < data:
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head
