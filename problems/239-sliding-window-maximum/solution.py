from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Monotonically Decreasing Queue
        output = []
        queue = deque()
        left = 0
        right = 0

        nums_len = len(nums)
        while right < nums_len:
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # remove left value from window
            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= k:
                output.append(nums[queue[0]])
                left += 1

            right += 1

        return output
