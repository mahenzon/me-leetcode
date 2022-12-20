# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:

    def depth_first_search(self, node: TreeNode | None, current_sum: int):
        if not node:
            return

        current_sum += node.val
        search_sum = current_sum - self.target_sum
        if search_sum in self.sums_count:
            self.result += self.sums_count[search_sum]

        self.sums_count[current_sum] += 1
        self.depth_first_search(node.left, current_sum)
        self.depth_first_search(node.right, current_sum)
        self.sums_count[current_sum] -= 1

    # noinspection PyAttributeOutsideInit
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:

        self.sums_count = defaultdict(int)
        self.sums_count[0] = 1
        self.target_sum = targetSum
        self.result = 0

        self.depth_first_search(root, 0)
        return self.result

