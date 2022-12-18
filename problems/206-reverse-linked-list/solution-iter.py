# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head

        while current:
            # prev, current, current.next = current, current.next, prev
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
