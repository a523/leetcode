# 236. 二叉树的最近公共祖先

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


ans = None


def lowestCommonAncestor(root, p, q):
    def recurse_tree(current_node):
        if not current_node:
            return False

        left = recurse_tree(current_node.left)

        right = recurse_tree(current_node.right)

        mid = current_node == p or current_node == q

        if mid + left + right >= 2:
            global ans
            ans = current_node
        return mid or left or right

    recurse_tree(root)
    global ans
    return ans


#
# def lowestCommonAncestor2(root, p, q):
#     if not root:
#         return
#     if p == q == root:
#         return root
#     elif p == root.left and (q == root or q == root.right):
#         return root
#     elif q == root.left and (p == root or p == root.right):
#         return root
#     else:
#         lowestCommonAncestor(root.left, p, q)
#         lowestCommonAncestor(root.right, p, q)

def lowest_common_ancestor(root, p, q):
    stack = [root]
    parent = {root: None}

    while p not in parent or q not in parent:
        node = stack.pop()

        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]
    return q


BOTH_PENDING = 2
LEFT_DONE = 2
BOTH_DONE = 0


def lowest_common_ancestor2(root, p, q):
    stack = [(root, BOTH_PENDING)]
    one_node_found = False
    LCA_index = -1
    while stack:
        parent_node, parent_state = stack[-1]
        if parent_node != BOTH_DONE:
            if parent_state == BOTH_PENDING:
                if parent_node == p or parent_node:
                    if one_node_found:
                        return stack[LCA_index][0]
                    else:
                        one_node_found = True
                        LCA_index = len(stack) - 1


def lowest_common_ancestor3(root, p, q):
    parents = {}

    def record_parent(curr_node, parent=None):
        if curr_node:
            node_val = curr_node.val
            parents[node_val] = parent
            record_parent(curr_node.left, curr_node)
            record_parent(curr_node.right, curr_node)

    record_parent(root, None)

    # 化开p的路径
    p_path = {p}
    node = p
    while node:
        p_path.add(parents[node])
        node = parents[node]

    # 化开q
    node = q
    while node:
        if node in p_path:
            return node
        node = parents[node]
