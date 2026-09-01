"""
Name: 450. Delete Node in a BST
Ref: https://leetcode.com/problems/delete-node-in-a-bst/description/

Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
 - Search for a node to remove.
 - If the node is found, delete the node.

Example 1:
----------
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
----------
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
----------
Input: root = [], key = 0
Output: []

Constraints:
------------
The number of nodes in the tree is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5

Follow up: Could you solve it with time complexity O(height of tree)?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util import TreeNode
from typing import Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Если дерево пустое, то и удалять нечего
        if not root:
            return None
        
        # 1. Поиск нужной ноды
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        else:
            # Сценарий 2.1 и 2.2 (нет левого ребенка -> возвращаем правого, даже если он None)
            if not root.left:
                return root.right
            # Сценарий 2.2 (нет правого ребенка -> возвращаем левого)
            if not root.right:
                return root.left

            # Сценарий 2.3: Два ребенка
            # 1. Находим самый маленький узел в ПРАВОМ поддереве
            min_node = self.findMin(root.right)
            
            # 2. Записываем его значение в текущий узел (заменяем удаляемый узел)
            root.val = min_node.val
            
            # 3. Самое красивое: отправляем команду удалить этот дубликат из правого поддерева!
            # Передаем туда корень правого поддерева и значение, которое нужно стереть
            root.right = self.deleteNode(root.right, min_node.val)
            
        return root
    
    def findMin(self, node: TreeNode) -> TreeNode:
        # Просто бежим влево до упора
        current = node
        while current.left:
            current = current.left
        return current # вернули сам узел с минимальным значением



sol = Solution()
input = TreeNode.fromList([5,3,6,2,4,None,7])
key = 3
expected = TreeNode.fromList([5,4,6,2,None,None,7])
res = sol.deleteNode(input, key)
# assert res == expected


        