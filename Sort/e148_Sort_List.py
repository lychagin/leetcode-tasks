"""
148. Sort List
Ref: https://leetcode.com/problems/sort-list/description/

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
----------
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
----------
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
----------
Input: head = []
Output: []

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-10^5 <= Node.val <= 10^5
"""
from typing import Optional
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s", force=True)
logger = logging.getLogger(__name__)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeList(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in arr[1:]:
        current.next = ListNode(i)
        current = current.next
    return head

def printList(l: Optional[ListNode]) -> None:
    next = l
    while next != None:
        logger.debug(f"Node: {next.val}")
        next = next.next

class Solution:
    # Тут будем тренироваться на сортировке слиянием (Merge Sort)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left, right = self.divide(head)
        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)

        return self.merge(sorted_left, sorted_right)

    def divide(self, head: Optional[ListNode]) -> tuple[Optional[ListNode]]:
        fast = head.next
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        idx1 = list1
        idx2 = list2

        result = ListNode(0)
        current = result

        while idx1 is not None and idx2 is not None:
            if idx1.val < idx2.val:
                current.next = idx1
                idx1 = idx1.next
            else:
                current.next = idx2
                idx2 = idx2.next
            current = current.next

        if idx1 is None:
            current.next = idx2
        else:
            current.next = idx1
        return result.next

testList = makeList([1, 2, 3, 4])
printList(testList)

sol = Solution()
res = sol.sortList(testList)
print("Result:")
printList(res)

