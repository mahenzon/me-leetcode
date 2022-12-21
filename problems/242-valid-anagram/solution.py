class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # return Counter(s) == Counter(t)

        count_s = {}
        count_t = {}

        for char_s, char_t in zip(s, t):
            count_s[char_s] = 1 + count_s.get(char_s, 0)
            count_t[char_t] = 1 + count_t.get(char_t, 0)

        for char, count in count_s.items():
            if count != count_t.get(char, 0):
                return False

        return True
