"""
Name: 700. Search in a Binary Search Tree
Ref: https://leetcode.com/problems/search-in-a-binary-search-tree/description/

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:
----------
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
----------
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
------------
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
"""
from typing import Optional
from util import TreeNode

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while current:
            if current.val == val:
                return current
            elif current.val < val:
                current = current.right
            else:
                current = current.left

        return None
    
sol = Solution()

# Example 1: root = [4,2,7,1,3], val = 2 -> [2,1,3]
root = TreeNode.fromList([4, 2, 7, 1, 3])
found = sol.searchBST(root, 2)
assert found == TreeNode.fromList([2, 1, 3])
print(f"Example 1: found subtree with root {found.val}")

# Example 2: root = [4,2,7,1,3], val = 5 -> []
missing = sol.searchBST(TreeNode.fromList([4, 2, 7, 1, 3]), 5)
assert missing is None
print(f"Example 2: {missing}")