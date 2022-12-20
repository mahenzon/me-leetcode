# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:

        result = []

        def depth_first_search(node: TreeNode, node_values: list[int], current_sum: int):
            if not node:
                return

            values = node_values + [node.val]
            current_sum += node.val

            if (
                not node.left
                and not node.right
                and (current_sum == targetSum)
            ):
                result.append(values)
                return

            depth_first_search(node.left, values, current_sum)
            depth_first_search(node.right, values, current_sum)

        depth_first_search(root, [], 0)
        return result

