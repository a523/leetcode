def maxDepth(root) -> int:

    def recurrence(node, cur_len=1):
        if not node.left and not node.right:
            return cur_len
        else:
            if node.left:
                cur_len += 1
                left_len = recurrence(node.left, cur_len)
            else:
                left_len = cur_len

            if node.right:
                cur_len += 1
                right_len = recurrence(node.right, cur_len)
            else:
                right_len = cur_len
            return max(left_len, right_len)
    return recurrence(root, cur_len=1)


def max_depth(root):
    stack = []
    if root:
        stack.append((1, root))
    depth = 0
    while stack:
        current_depth, root = stack.pop()
        if root:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))
    return depth