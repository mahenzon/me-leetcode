# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy

        remainder = 0
        while l1 or l2:
            a = 0
            b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            num = a + b + remainder
            remainder = num // 10
            num = num % 10
            tail.next = ListNode(num)
            tail = tail.next

        if remainder:
            tail.next = ListNode(remainder)

        return dummy.next
