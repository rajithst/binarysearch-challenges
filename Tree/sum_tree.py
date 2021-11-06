class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root):

        def dfs(node):
            if node is None:
                return True

            if node.left is None and node.right is None:
                return True

            ls = node.left.val if node.left else 0
            rs = node.right.val if node.right else 0

            return ls + rs == node.val and dfs(node.left) and dfs(node.right)

        return dfs(root)
