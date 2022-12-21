class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        count_p = {}
        count_s = {}

        for i in range(len(p)):
            count_p[p[i]] = 1 + count_p.get(p[i], 0)
            count_s[s[i]] = 1 + count_s.get(s[i], 0)

        result = []
        if count_p == count_s:
            result.append(0)

        left = 0
        for right in range(len(p), len(s)):
            count_s[s[right]] = 1 + count_s.get(s[right], 0)
            count_s[s[left]] -= 1

            if count_s[s[left]] == 0:
                count_s.pop(s[left])

            left += 1
            if count_s == count_p:
                result.append(left)

        return result
