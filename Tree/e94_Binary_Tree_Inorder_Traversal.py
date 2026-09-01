"""
Name: 94. Binary Tree Inorder Traversal
Ref: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Example 1:
----------
Input: root = [1,null,2,3]
Output: [1,3,2]
Explanation:
1
 \\
  2
 //
3

Example 2:
----------
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]
Explanation:
            1
          // \\
        2       3
      // \\       \\
      4   5       8
        // \\    //
        6   7   9

Example 3:
----------
Input: root = []
Output: []

Example 4:
----------
Input: root = [1]
Output: [1]

Constraints:
------------
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from util import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        #return self.recurseSolution(root)
        return self.iterateSolution(root)

    def recurseSolution(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def iterateSolution(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        curr = root
        
        # Цикл работает, пока мы не обошли все узлы и пока стек не пуст
        while curr is not None or stack:
            # 1. Спускаемся до упора влево, сохраняя путь в стек
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            # 2. Дошли до тупика (левее ничего нет). Достаем узел из стека
            curr = stack.pop()
            res.append(curr.val)  # Добавляем корень/узел в результат
            
            # 3. Переходим к правому поддереву
            curr = curr.right
            
        return res

sol = Solution()

# Example 1: [1,null,2,3] -> [1,3,2]
tree1 = TreeNode.fromList([1, None, 2, 3])
res1 = sol.inorderTraversal(tree1)
print(f"Example 1: {res1}")  # [3,1,2] — wait, let me verify

# Example 2: [1,2,3,4,5,null,8,null,null,6,7,9]
tree2 = TreeNode.fromList([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
res2 = sol.inorderTraversal(tree2)
print(f"Example 2: {res2}")

# Example 3: [] -> []
tree3 = TreeNode.fromList([])
res3 = sol.inorderTraversal(tree3)
print(f"Example 3: {res3}")

# Example 4: [1] -> [1]
tree4 = TreeNode.fromList([1])
res4 = sol.inorderTraversal(tree4)
print(f"Example 4: {res4}")
