"""
Name: 234. Palindrome Linked List
Ref: https://leetcode.com/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=linked-list

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
----------
Input: head = [1,2,2,1]
Output: true

Example 2:
----------
Input: head = [1,2]
Output: false

Constraints:
------------
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from utils import ListNode, makeList, printList
from typing import Optional
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now, slow points to the middle element; fast points to the last element
        # start iterating both pointers in reverse order, correcting links to preious pointers
        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        current = prev
        while current:
            logger.debug(f"current: {current.val}; head: {head.val}")
            if current.val != head.val:
                return False
            current = current.next
            head = head.next

        return True

sol = Solution()
res = sol.isPalindrome(makeList([1,2,2,1]))
logger.debug(f"res: {res}")
        