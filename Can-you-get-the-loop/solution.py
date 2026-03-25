def loop_size(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            current = slow.next
            while current != slow:
                count += 1
                current = current.next
            return count
    return 0
