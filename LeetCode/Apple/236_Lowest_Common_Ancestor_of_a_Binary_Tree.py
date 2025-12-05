from header import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(curr, target):
    if not curr:
        return None
    if curr in target:
        return curr

    left = dfs(curr.left, target)
    right = dfs(curr.right, target)

    if left and right:
        return curr
    return left if left else right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        target = set([p,q])
        return dfs(root, target)


def array_to_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def find_node(root, value):
    """
    Returns the node in the tree with the given value.
    If the value is not found, returns None.
    """
    if root is None:
        return None
    if root.val == value:
        return root

    # Search in the left subtree
    left_result = find_node(root.left, value)
    if left_result is not None:
        return left_result

    # Search in the right subtree
    return find_node(root.right, value)

arr = [3,5,1,6,2,0,8,None,None,7,4]
root = array_to_tree(arr)

print(Solution().lowestCommonAncestor(root, find_node(root, 5),find_node(root, 1)).val)
