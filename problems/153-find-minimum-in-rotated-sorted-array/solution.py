class Solution:
    def findMin(self, nums: list[int]) -> int:
        # nums is not empty!

        # haha!
        # return min(nums)

        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            left_value = nums[left]
            right_value = nums[right]
            if left_value < right_value:
                result = min(left_value, result)
                break

            # middle_idx = left + (right - left) // 2
            middle_idx = (right + right) // 2
            middle_value = nums[middle_idx]
            result = min(middle_value, result)

            if middle_value >= left_value:
                left = middle_idx + 1
            else:
                right = middle_idx - 1

        return result
