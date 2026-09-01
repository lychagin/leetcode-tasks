# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def addNodeLeft(self, val):
        self.left = TreeNode(val)

    def addNodeRight(self, val):
        self.right = TreeNode(val)

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return (self.val == other.val and
                self.left == other.left and
                self.right == other.right)

    @staticmethod
    def fromList(values):
        """Build binary tree from list [level-order], e.g. [1,null,2,3]."""
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root
        