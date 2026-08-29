"""
Name: 141. Linked List Cycle
Ref: https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=linked-list

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
----------
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
----------
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
----------
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
------------
The number of the nodes in the list is in the range [0, 104].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
# Definition for singly-linked list.
import logging
from typing import Optional

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def makeList(input: list[int]) -> ListNode:
    head = ListNode(0)
    current = head
    for i in input:
        node = ListNode(i)
        current.next = node
        current = node
    return head.next

def getNode(head: ListNode, val: int) -> ListNode:
    while head:
        if head.val == val:
            return head
        head = head.next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #return self.MyFirstSolution(head)
        return self.MyOptimizedSolution(head)
    
    def MyFirstSolution(self, head: Optional[ListNode]) -> bool:
        visitedNodes = set()
        current = head
        while current != None:
            if current in visitedNodes:
                return True
            visitedNodes.add(current)
            logger.debug(f"val: {current.val}")
            current = current.next
        return False

    def MyOptimizedSolution(self, head: Optional[ListNode]) -> bool:
        # делаем решение с O(1) по памяти. Используем два указателя (алогоритм Флойда или "Черепахи и зайца")
        slow = head
        fast = head
        while fast and fast.next is not None:
            logger.debug(f"val: {slow.val}")
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


sol = Solution()
input = makeList({3, 2, 0, -4})
node2 = getNode(input, 2)
logger.debug(f"node2 val: {node2.val}")
node4 = getNode(input, -4)
logger.debug(f"node4 val: {node4.val}")
node4.next = node2
res = sol.hasCycle(input)
logger.debug(f"res: {res}")
