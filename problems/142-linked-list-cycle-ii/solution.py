# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode | None = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        while head != slow:
            head = head.next
            slow = slow.next

        return head
