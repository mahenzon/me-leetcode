class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        known_numbers = {}
        for idx, num in enumerate(nums):
            desire = target - num
            if desire in known_numbers:
                return [known_numbers[desire], idx]
            known_numbers[num] = idx
