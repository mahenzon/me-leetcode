# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:

    def depth_first_search(self, node: TreeNode | None) -> tuple[bool, int]:
        if not node:
            return True, 0

        left_balanced, left_gap = self.depth_first_search(node.left)
        right_balanced, right_gap = self.depth_first_search(node.right)

        balanced = (
            left_balanced
            and right_balanced
            and abs(left_gap - right_gap) <= 1
        )

        return balanced, 1 + max(left_gap, right_gap)

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.depth_first_search(root)[0]
