"""
147. Insertion Sort List
Ref: https://leetcode.com/problems/insertion-sort-list/description/?envType=problem-list-v2&envId=sorting

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. 
The partially sorted list (black) initially contains only the first element in the list. 
One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Example 1:
----------
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
----------
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Constraints:
------------
The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        current = head
        while current:
            next_node = current.next # 1. Запоминаем следующий узел

            # 2. Тут мы будем искать место для вставки внутри отсортированного списка
            prev = dummy # Начинаем поиск с самого начала нового списка

            # Подсказка для следующего шага: пока следующий узел в новом списке (prev.next) существует 
            # и его значение МЕНЬШЕ, чем значение нашего текущего узла (current.val) — двигаем prev вперед.
            # ... напишите этот маленький цикл while ...
            while prev.next and prev.next.val < current.val:
                prev = prev.next
    
            # 3. Тут мы будем делать саму вставку узла current между prev и prev.next
            current.next = prev.next
            prev.next = current

             # 4. Переходим к следующему элементу исходного списка
            current = next_node

        return dummy.next