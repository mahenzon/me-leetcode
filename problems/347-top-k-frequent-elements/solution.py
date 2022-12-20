class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}
        freq = [[] for _ in range((len(nums) + 1))]

        for number in nums:
            if number in seen:
                seen[number] += 1
            else:
                seen[number] = 1

        for number, count in seen.items():
            freq[count].append(number)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result
