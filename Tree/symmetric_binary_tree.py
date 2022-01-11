# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None:
            return True

        def dfs(r, l):
            if r is None and l is None:
                return True
            if r is None and l is not None:
                return False
            if r is not None and l is None:
                return False
            if r.val != l.val:
                return False

            return dfs(l.left, r.right) and dfs(l.right, r.left)

        return dfs(root.left, root.right)
