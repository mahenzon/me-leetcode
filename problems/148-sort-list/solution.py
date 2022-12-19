# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not (head and head.next):
            return head

        # split into two lists by half
        left = head
        right = self.getMiddle(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMiddle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left or right

        # remainder = left or right
        # while remainder:
        #     tail.next = remainder
        #     remainder = remainder.next
        #     tail = tail.next

        return dummy.next
