# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode | None:
        if not lists:
            return None
        return self.mergeSubLists(lists, 0, len(lists) - 1)

    def mergeSubLists(self, lists: list[ListNode], start: int, end: int) -> ListNode:
        if start >= end:
            return lists[end]

        middle = start + (end - start) // 2

        left = self.mergeSubLists(lists, start, middle)
        right = self.mergeSubLists(lists, middle + 1, end)

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()
        tail = result

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 or list2

        return result.next
