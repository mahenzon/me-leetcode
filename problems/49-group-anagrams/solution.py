from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        for string in strs:
            counts = [0] * 26  # a ... z
            for char in string:
                counts[ord(char) - ord("a")] += 1

            result[tuple(counts)].append(string)

        return list(result.values())
