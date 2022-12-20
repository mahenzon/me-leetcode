class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        nums_right = len(nums) - 1

        for i, a in enumerate(nums):
            if i and a == nums[i - 1]:
                # skip dupes
                continue

            left = i + 1
            right = nums_right
            while left < right:
                b = nums[left]
                c = nums[right]
                total = a + b + c
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([a, b, c])

                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
