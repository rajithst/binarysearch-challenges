# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def solve(self, root):

        q = deque()
        q.append(root)
        r = []
        while q:
            l = len(q)
            for i in range(l):
                c = q.popleft()
                if i == 0:
                    r.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
        return r
