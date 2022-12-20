class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        results = []
        parts = []

        def k_sum(k, start, inner_target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    i_value = nums[i]
                    parts.append(i_value)
                    k_sum(k - 1, i + 1, inner_target - i_value)
                    parts.pop()
                return

            left = start
            right = len(nums) - 1

            while left < right:
                left_value = nums[left]
                right_value = nums[right]

                total = left_value + right_value
                if total < inner_target:
                    left += 1
                elif total > inner_target:
                    right -= 1
                else:
                    results.append(parts + [left_value, right_value])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        k_sum(4, 0, target)
        return results
