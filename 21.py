class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    pre_head = ListNode(-1)
    prev = pre_head

    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    prev.next = l1 if l1 is not None else l2

    return pre_head.next


def merge_two_lists2(l1, l2):
    """递归版"""
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_lists2(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists2(l1, l2.next)
        return l2

