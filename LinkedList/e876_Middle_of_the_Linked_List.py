"""
Name: 876. Middle of the Linked List
Ref: https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=problem-list-v2&envId=linked-list

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle nod

Example 1:
----------
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
----------
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
------------
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
import logging
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeList(input: list[int]) -> ListNode:
    head = ListNode(0)
    current = head
    for i in input:
        node = ListNode(i)
        current.next = node
        current = node
    return head.next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #return self.sol_direct(head)
        return self.two_pointers(head)

    def two_pointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def sol_direct(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        counter = head
        while counter:
            size += 1
            counter = counter.next

        mid = size // 2;
        target = head
        for _ in range(mid):
            target = target.next

        return target

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

sol = Solution()
input = makeList({1, 2, 3, 4, 5, 6})
res = sol.middleNode(input)
print(f"res: {res.val}")
        