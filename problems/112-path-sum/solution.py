# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def depth_first_search(node: TreeNode, current_sum: int) -> bool:
            if not node:
                return False

            current_sum += node.val
            if not node.left and not node.right:
                return current_sum == targetSum

            return (
                depth_first_search(node.left, current_sum)
                or depth_first_search(node.right, current_sum)
            )

        return depth_first_search(root, 0)
