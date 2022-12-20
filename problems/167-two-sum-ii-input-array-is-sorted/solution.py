class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            left_value = numbers[left]
            right_value = numbers[right]
            amount = left_value + right_value
            if amount == target:
                return [left + 1, right + 1]

            if amount > target:
                right -= 1
            else:
                left += 1
