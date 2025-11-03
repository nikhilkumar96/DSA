# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = ""
        queue = []
        if root:
            queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr:
                s += str(curr.val)
                s += ","
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                s += str("#,")
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = data.split(',')[:-1]
        head = None
        node_queue = []
        while queue:
            if node_queue:
                node = node_queue.pop(0)
                left_val = queue.pop(0)
                right_val = queue.pop(0)
                if left_val != "#":
                    left = TreeNode(left_val)
                    node_queue.append(left)
                else:
                    left = None
                if right_val != "#":
                    right = TreeNode(right_val)
                    node_queue.append(right)
                else:
                    right = None
                node.left = left
                node.right = right


            else:
                val = queue.pop(0)
                node = TreeNode(val)
                node_queue.append(node)
                head = node
        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

obj = Codec()
obj.deserialize("1,2,3,#,#,4,5,#,#,#,#,")