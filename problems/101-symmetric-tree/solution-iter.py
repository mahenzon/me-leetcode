# Definition for a binary tree node.

import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        q1 = queue.Queue()
        q2 = queue.Queue()

        q1.put(root)
        q2.put(root)

        while not q1.empty() and not q2.empty():
            node1: TreeNode | None = q1.get()
            node2: TreeNode | None = q2.get()

            if not node1 and not node2:
                pass
            elif not node1 or not node2 or node1.val != node2.val:
                return False

            if node1 and node2:
                # one side
                q1.put(node1.left)
                q2.put(node2.right)
                # and another
                q1.put(node1.right)
                q2.put(node2.left)

        # both queues should be empty
        return True
