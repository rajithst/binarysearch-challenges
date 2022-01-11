# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        r = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            r.append(node.val)
            dfs(node.right)

        dfs(root)
        return r
