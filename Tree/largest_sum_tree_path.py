class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root):
        maxsum = root.val

        def dfs(node):
            nonlocal maxsum
            if node is None:
                return 0
            lsum = dfs(node.left)
            rsum = dfs(node.right)
            maxsum = max(maxsum, lsum + rsum + node.val)
            return max(lsum, rsum) + node.val

        dfs(root)
        return maxsum
