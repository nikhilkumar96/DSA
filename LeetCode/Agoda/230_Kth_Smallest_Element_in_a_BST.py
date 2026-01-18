from header import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(curr, box):
            if curr.left:
                dfs(curr.left, box)

            if len(box) < k:
                heapq.heappush(box, curr.val)

            if curr.right:
                dfs(curr.right, box)

        box = []
        dfs(root, box)
        res = None
        while box:
            res = heapq.heappop(box)
        return res