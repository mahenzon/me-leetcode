# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode | None:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            current_lists_len = len(lists)
            for index in range(0, current_lists_len, 2):
                next_idx = index + 1
                list1 = lists[index]
                list2 = lists[next_idx] if next_idx < current_lists_len else None
                merged_lists.append(self.mergeTwoLists(list1, list2))
            lists = merged_lists

        return lists[0]

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
