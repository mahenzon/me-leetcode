class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # middle_idx = left + (right - left) // 2
            middle_idx = (left + right) // 2

            middle_value = nums[middle_idx]
            if target == middle_value:
                return middle_idx

            left_value = nums[left]
            if left_value <= middle_value:
                if target > middle_value or target < left_value:
                    left = middle_idx + 1
                else:
                    right = middle_idx - 1

            else:
                right_value = nums[right]
                if target < middle_value or target > right_value:
                    right = middle_idx - 1
                else:
                    left = middle_idx + 1

        return -1
