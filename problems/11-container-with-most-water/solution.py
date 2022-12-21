class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0

        left = 0
        right = len(height) - 1

        while left < right:
            left_h = height[left]
            right_h = height[right]
            area = (right - left) * min(left_h, right_h)
            result = max(result, area)
            if left_h < right_h:
                left += 1
            else:
                right -= 1

        return result
