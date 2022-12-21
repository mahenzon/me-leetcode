class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        result = 0

        left = 0
        for right, right_value in enumerate(s):
            counts[right_value] = 1 + counts.get(right_value, 0)

            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
