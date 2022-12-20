class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        result = 0
        total_len = len(s)
        for i, sym in enumerate(s):
            current_value = roman_to_int[sym]
            if i + 1 < total_len and (current_value < roman_to_int[s[i + 1]]):
                result -= current_value
            else:
                result += current_value

        return result
