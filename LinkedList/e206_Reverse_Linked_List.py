"""
Name: 206. Reverse Linked List
Ref: https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=linked-list

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
----------
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
----------
Input: head = [1,2]
Output: [2,1]

Example 3:
----------
Input: head = []
Output: []

Constraints:
------------
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from utils import ListNode, makeList, printList
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #return self.myFirstSolution(head)
        #return self.mySecondSolution(head)
        return self.myThirdSolution(head)

    def myFirstSolution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        begin = head
        tmpList = []
        while head:
            tmpList.append(head.val)
            head = head.next
        head = begin
        tmpList.reverse()
        revList = ListNode()
        beginRev = revList
        for i in tmpList:
            node = ListNode(i)
            revList.next = node
            revList = node

        return beginRev.next

    def mySecondSolution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        current = head
        while current:
            current.next, prev, current = prev, current, current.next
        
        return prev
    
    def myThirdSolution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Базовый случай: если список пустой или мы дошли до ПОСЛЕДНЕЙ ноды
        if not head or not head.next:
            return head

        # 2. Погружение: уходим рекурсией до самого конца списка
        new_head = self.myThirdSolution(head.next)

        # 3. Разворот стрелочки (происходит на выходе из рекурсии)
        head.next.next = head  # Следующая нода теперь указывает на меня

        head.next = None # Я больше не указываю на неё (разрываем старую связь)

        # 4. Возвращаем новую голову списка наверх
        return new_head


sol = Solution()
res = sol.reverseList(makeList([1,2,3,4,5]))
print("reversed list:")
printList(res)