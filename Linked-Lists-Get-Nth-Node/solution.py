from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise Exception("Invalid index")
    curr = node
    idx = 0
    while curr is not None:
        if idx == index:
            return curr
        curr = curr.next
        idx += 1
    raise Exception("Invalid index")
