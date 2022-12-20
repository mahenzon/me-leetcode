# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_node(root, float("-inf"), float("inf"))

    def check_node(self, node: TreeNode | None, left: int | float, right: int | float) -> bool:
        if not node:
            return True

        if not (left < node.val < right):
            return False

        return (
            self.check_node(node.left, left, node.val)
            and self.check_node(node.right, node.val, right)
        )
