# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def is_mirror(self, node1: TreeNode | None, node2: TreeNode | None) -> bool:
        if not node1 and not node2:
            return True

        if not node1 or not node2 or node1.val != node2.val:
            return False

        return (
            self.is_mirror(node1.left, node2.right)
            and self.is_mirror(node1.right, node2.left)
        )

    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.is_mirror(root, root)
