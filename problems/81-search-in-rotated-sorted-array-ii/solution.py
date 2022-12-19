class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # middle_idx = left + (right - left) // 2
            middle_idx = (left + right) // 2

            middle_value = nums[middle_idx]
            if middle_value == target:
                return True

            while left < middle_idx and nums[left] == middle_value:
                left += 1

            while right > middle_idx and nums[right] == middle_value:
                right -= 1

            # !!! sorted

            left_value = nums[left]
            right_value = nums[right]
            if middle_value >= left_value:
                if left_value <= target < middle_value:
                    right = middle_idx - 1
                else:
                    left = middle_idx + 1
            else:
                if right_value >= target > middle_value:
                    left = middle_idx + 1
                else:
                    right = middle_idx - 1

        return False
