"""
Name: 21. Merge Two Sorted Lists
Ref: https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=problem-list-v2&envId=linked-list

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
----------
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
----------
Input: list1 = [], list2 = []
Output: []

Example 3:
----------
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
------------
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

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

# Не нужно было писать. По условиям задачи списки уже отсортированные
def sortList(head: Optional[ListNode]):
    if head is None:
        return head

    nodes = []
    curr = head
    while curr:
        nodes.append(curr.val)
        curr = curr.next
    nodes.sort()
    sortedList = ListNode()
    sortHead = sortedList
    for i in nodes:
        newNode = ListNode()
        newNode.val = i
        sortedList.next = newNode
        sortedList = newNode

    return sortHead.next

def printList(head: ListNode):
    while head:
        logger.debug(f"val: {head.val}")
        head = head.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        mergeHead = mergedList
        while list1 and list2:
            newNode = ListNode()
            if list1.val < list2.val:
                newNode.val = list1.val
                list1 = list1.next
            else:
                newNode.val = list2.val
                list2 = list2.next
            mergedList.next = newNode
            mergedList = newNode

        mergedList.next = list1 if list1 else list2

        return mergeHead.next

sol = Solution()
list1 = makeList([5,1,2,4])
sList1 = sortList(list1)
list2 = makeList([1,3,4])
sList2 = sortList(list2)
res = sol.mergeTwoLists(sList1, sList2)
printList(res)