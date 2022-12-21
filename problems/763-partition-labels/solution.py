class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {}

        for index, char in enumerate(s):
            last_index[char] = index

        result = []
        size = 0
        end = 0
        for index, char in enumerate(s):
            size += 1
            end = max(end, last_index[char])

            if index == end:
                result.append(size)
                size = 0

        return result
