from header import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = [root]
        c=1
        if not root:
            return 0
        while q:
            temp = []
            for curr in q:
                if curr.left is None and curr.right is None:
                    return c
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
            q = temp
            c+=1
        return c