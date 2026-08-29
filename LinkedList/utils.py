from typing import Optional

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
        print(f"val: {head.val}")
        head = head.next