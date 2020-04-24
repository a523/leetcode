# 235. 二叉搜索树的最近公共祖先


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p = 2
q = 8


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
    p_val = p.val
    q_val = q.val
    node = root

    while node:
        parent_val = node.val

        if p_val > parent_val and q_val > parent_val:
            node = node.right
        elif p_val < parent_val and q_val < parent_val:
            node = node.left
        else:
            return node