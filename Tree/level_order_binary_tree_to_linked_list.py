from collections import deque


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, root):

        que = deque()
        que.append(root)
        head = None
        root_head = None
        while (que):
            ll = len(que)
            for _ in range(ll):
                cn = que.popleft()
                if head is None:
                    head = LLNode(cn.val)
                    root_head = head
                else:
                    head.next = LLNode(cn.val)
                    head = head.next
                if cn.left:
                    que.append(cn.left)
                if cn.right:
                    que.append(cn.right)
        return root_head
